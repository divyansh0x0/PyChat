import socket

connections = list()
class Message:
    def __init__(self, type, content):
        self.type = type
        self.content = content


class Client:
    def __init__(self, client_socket, address, name):
        self.socket = client_socket
        self.address = address
        self.name = name
        self.cached_messages = list()
        self.id = hash(self.address)

    def __hash__(self):
        return self.id


class P2PConnection:
    def __init__(self, client: Client):
        self.client = client

    def check_for_new_messages(self):
        pass

    def send_message(self, message: Message):
        pass


def start_server():
    # Here we made a socket instance and passed it two parameters.
    # The first parameter is AF_INET and the second one is SOCK_STREAM.
    # AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol. 
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1" #localhost
    port = 0 #0 means any available port
    server_socket.bind((host, port)) 
    
    while True:
        server_socket.listen(1)
        con,addr = server_socket.accept()
        client = Client(client_socket=con, address=addr, name="Unknown")
        connections.append(P2PConnection(client, server_socket))
        