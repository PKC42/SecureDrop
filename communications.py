import socket
import ssl
from pathlib import Path
import json
import sys
import time
import platform
import netifaces
import time
from utilities import online_user_emails
import threading
from utilities import is_contact



online_user_lock = threading.Lock()
# ----------------------------------------------------------------------------------------
def listen(end_flag):

    global online_user_emails

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
    time_reset = 10

    

    while not end_flag.is_set(): 
        
        elapsed_time = time.time() - start_time

        #print(elapsed_time)

        if elapsed_time >= time_reset:
            with online_user_lock:
                online_user_emails.clear()
            start_time = time.time()
            elapsed_time = 0
        

        try:
            listening_socket.settimeout(1.0)
            data, address = listening_socket.recvfrom(1024)  
            
            user_email = data.decode('utf-8')
            
            online_user_emails.append(user_email)
            online_user_emails = list(set(online_user_emails))


        except socket.timeout:
            pass
        

    print("Closing Listening socket")
    listening_socket.close()
# ----------------------------------------------------------------------------------------
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

# ----------------------------------------------------------------------------------------

# takes data and ip address to send to the other socket
def send_file(ip_address, file):

    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_cert_chain("cert.pem")
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    try:
        with socket.create_connection((ip_address, 21001)) as sock:
                with context.wrap_socket(sock, server_hostname = ip_address) as ssock:
                    ssock.sendall(file.encode())

                    with open(file, "rb") as f:
                        while True:
                            data = f.read(1024)
                            if not data:
                                break
                            ssock.sendall(data)
    except ConnectionRefusedError:
        print("Connection refused! The receiver may be offline or unreachable.")
# ----------------------------------------------------------------------------------------

def receive_file(end_flag):
    interfaces = netifaces.interfaces()

    for interface in interfaces:
        if interface.startswith("lo"):
            continue
        addrs = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addrs:
            ip_address = addrs[netifaces.AF_INET][0]['addr']
            break
    
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain("cert.pem")
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    

    while not end_flag.is_set():

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.settimeout(10.0)
                sock.bind((ip_address, 21001))
                sock.listen()
                connection, address = sock.accept()

                

                with context.wrap_socket(connection, server_side = True) as ssock:
                    filename = ssock.recv(1024).decode()

                    with open(filename, "wb") as f:
                        while True:
                            data = ssock.recv(1024)
                            if not data:
                                break
                            f.write(data)

                    ssock.close()
                    sock.close()
               
            except socket.timeout:
                sock.close()
                # print("Connection timed out!")
                pass

    print("Closing receive file socket")
        

                
            

        
        
    
