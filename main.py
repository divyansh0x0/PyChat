import gui
import pychat_network as network
import time
import threading


def create_connection(ip, port, name):
    pass


def p2p_connector():
    available_connections: list[network.P2PConnection] = list()

    while True:
        for connection in available_connections:
            connection.check_for_new_messages()
        print("Background thread")
        time.sleep(1)


def begin_p2p_connection_thread():
    t1 = threading.Thread(target=p2p_connector)
    t1.start()
    return t1

gui.init()

if __name__ == "__main__":
    bg_thread = begin_p2p_connection_thread()
    gui.show()
    bg_thread.join()
