import socket


class Message:
    def __init__(self, type, content):
        self.type = type
        self.content = content


class Client:
    def __init__(self, ip, port, address):
        self.ip = ip
        self.port = port
        self.address = address
        self.cached_messages = list()


class P2PConnection:
    def __init__(self, client: Client):
        self.client = client

    def check_for_new_messages(self):
        pass

    def send_message(self, message: Message):
       pass

