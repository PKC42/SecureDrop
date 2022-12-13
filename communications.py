import socket
import ssl
import socket
import datetime
import time

# remember to reinsert ip address
def send(ip_address):
    PORT = 9000

    # create a context
    context = ssl.SSLContext()
    context.verify_mode = ssl.CERT_REQUIRED

    # load certificate authority to verify the server's certificate
    context.load_verify_locations("ca.crt")

    # load the client certificate
    context.load_cert_chain(certfile = "user1.crt", keyfile = "user1.key")

    # create a socket for the client 
    client_socket = socket.socket()

    # wrap the client socket
    secure_client = context.wrap_socket(client_socket)

    # bind ip and port
    secure_client.connect((ip_address, PORT))

    print("HERE")

    pass


def listen():

    #automatically get host and port
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 9000
    print (HOST)

    # creating a server socket 
    serverSocket = socket.socket()
    serverSocket.bind((HOST, PORT))


    print(serverSocket)
    serverSocket.listen()
    print("Server listening:")

    while(True):
        pass
    







if __name__ == "__main__":
    pass
    send("172.17.0.2")
    #listen()