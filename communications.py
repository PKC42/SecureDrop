import socket
import ssl
from pathlib import Path
import json
import sys
import time
import platform
import netifaces
import time

# takes data and ip address to send to the other socket
def send_file(ip_address, data):

    print("Sending File")
    PORT = 9000

    # create a context
    context = ssl.SSLContext()
    context.verify_mode = ssl.CERT_REQUIRED

    # load certificate authority to verify the server's certificate
    context.load_verify_locations("ca.crt")

    # load the client certificate
    context.load_cert_chain(certfile = "user.crt", keyfile = "user.key")

    # create a socket for the client 
    client_socket = socket.socket()

    # wrap the client socket
    secured_client = context.wrap_socket(client_socket)

    # bind ip and port
    secured_client.connect((ip_address, PORT))

    # get certificate from the server
    server_certificate = secured_client.getpeercert()
    
    print("BREAK")



def receive_file():

    #automatically get host and port
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 9000
    print (HOST)
    # creating a server socket
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))

    print(server_socket)

    # listen for new connections
    server_socket.listen()
    print("Server listening:")

    while True:
        # accept connections
        client_connection, client_address = server_socket.accept()
        # wrap client socket
        secured_client_socket = ssl.wrap_socket(client_connection, server_side=True, ca_certs= "ca.crt", certfile="user.crt", keyfile="user.key", cert_reqs=ssl.CERT_REQUIRED, ssl_version=ssl.PROTOCOL_TLSv1_2)

        #  get the client's certificate
        client_cert = secured_client_socket.getpeercert()
        print(client_cert)
        if not client_cert:
                print("Unable to get the peer's certificate")


def broadcast(end_flag):

    broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    ip_addresses = []

    while not end_flag.is_set():
        file = Path('contacts.json')
        if file.is_file():
            fp = open('contacts.json', "r")
            data = json.load(fp)
        for contacts in data:
            ip_addresses.append(data[contacts]["IP"])

        file = Path('users.json')
        if file.is_file():
            fp = open('users.json', "r")
            user_data = json.load(fp)
        
        message = "Name: " + user_data["Name:"] + " Email: " + user_data["Email"]

        # send upd broadcast of the users email to the ip addresses
        message = message.encode('utf-8')

        for ip in ip_addresses:
            address = (ip, 20004)
            broadcast_socket.sendto(message, address)
        time.sleep(5)
    
    print("Closing Broadcast socket")
    broadcast_socket.close()
    fp.close()


def listen(end_flag, online_user_emails):

    interfaces = netifaces.interfaces()

    for interface in interfaces:
        if interface.startswith("lo"):
            continue
        addrs = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addrs:
            ip_address = addrs[netifaces.AF_INET][0]['addr']
            break

    port = 20004

    listening_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    listening_socket.bind((ip_address, port))

    start_time = time.time()
    time_reset = 60

    while not end_flag.is_set(): 
        
        elapsed_time = time.time() - start_time

        print(elapsed_time)

        if elapsed_time >= time_reset:
            start_time = time.time()
            elapsed_time = 0
            online_user_emails = []


        try:
            listening_socket.settimeout(1.0)
            data, address = listening_socket.recvfrom(1024)  
            # print("Received data from {}: {}".format(address, data.decode('utf-8')))
            
            user_email = data.decode('utf-8')
            
            online_user_emails.append(user_email)
            online_user_emails = list(set(online_user_emails))

            for item in online_user_emails:
                print(item)


        except socket.timeout:
            pass
        

    print("Closing Listening Socket")
    listening_socket.close()


