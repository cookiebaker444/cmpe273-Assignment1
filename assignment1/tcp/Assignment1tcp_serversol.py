import socket
from _thread import *
import threading

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024


def threaded(conn):
    while True:
        data = conn.recv(BUFFER_SIZE)
        if data:
            print("Received data from client No. " + data.decode())
            conn.send("pong".encode())
        if not data:
            print('No data received.')
            break
        #print(f"received data:{data.decode()}")

    conn.close()

def listen_forever():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    print("socket binded to port", TCP_PORT)
    s.listen(5)
    print("socket is listening")
    while True:
        conn, addr = s.accept()
        print(f'Connection address:{addr}')

        start_new_thread(threaded,(conn,))

    s.close()


listen_forever()
