import socket
import ssl

def main():
    HOST = '172.18.152.246'
    print(HOST)
    PORT = 9090

    sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sender.bind((HOST, PORT))


    sender.listen(5)

    
    while True:
        communication_socket, address = sender.accept()
        print(f"Connected to {address}")
        message = communication_socket.recv(1024).decode('utf-8')
        print(f"Message from client: is{message}")
        communication_socket.send(f"Got you message! Thanks!".encode('utf-8'))
        communication_socket.close()
        print(f"Connection with {address} ended!".decode('utf-8'))







if __name__ == "__main__":
    main()