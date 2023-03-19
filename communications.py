import socket
import ssl

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



