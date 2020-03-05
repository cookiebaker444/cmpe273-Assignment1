import socket
import sys
import time
def getArgs():
    try:
        arg1 = sys.argv[1]
    except IndexError:
        print(-1, -1, -1)
        return -1, -1, -1
    try:
        arg2 = sys.argv[2]
    except IndexError:
        print(arg1, -1, -1)
        return arg1, -1, -1
    try:
        arg3 = sys.argv[3]
    except IndexError:
        print(arg1, arg2, -1)
        return arg1, arg2, -1
    print(arg1, arg2, arg3)
    return arg1, arg2, arg3

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
#MESSAGE = "ping"

def send(tempTup):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.connect((TCP_IP, TCP_PORT))
    if tempTup[0] == -1:
        communicationGen(get_client_id(), s)
    elif tempTup[0] != -1 and tempTup[1] == -1:
        communicationGen(tempTup[0], s)
    elif tempTup[0] != -1 and tempTup[1] != -1 and tempTup[2] == -1:
        communicationSep(tempTup[0], s, tempTup[1])
    elif tempTup[0] != -1 and tempTup[1] != -1 and tempTup[2] != -1:
        communicationFou(tempTup[0], s, tempTup[1], tempTup[2])

def communicationSep(id, s, d):
    s.connect((TCP_IP, TCP_PORT))
    amount = 0
    while True:
        MESSAGE = "ping"
        s.send(f"{id}:{MESSAGE}".encode())
        data = s.recv(BUFFER_SIZE)
        print('Received from the server :', str(data.decode('ascii')))
        if amount == 100:
            break
        time.sleep(int(d))
    s.close()
    print("received data:", data.decode())

def communicationFou(id, s, d, t):
    s.connect((TCP_IP, TCP_PORT))
    for i in range(int(t)):
        MESSAGE = "ping"
        s.send(f"{id}:{MESSAGE}".encode())
        data = s.recv(BUFFER_SIZE)
        print('Received from the server :', str(data.decode('ascii')))
        time.sleep(int(d))
    s.close()
    print("received data:", data.decode())
        
def communicationGen(id, s):
        s.connect((TCP_IP, TCP_PORT))
        while True:
            MESSAGE = input('Please input the message to be sent:')
            s.send(f"{id}:{MESSAGE}".encode())
            data = s.recv(BUFFER_SIZE)
            print('Received from the server :', str(data.decode('ascii')))
            ans = input('\nDo you want to continue(y/n) :')
            if ans == 'y':
                continue
            else:
                break
        s.close()
        print("received data:", data.decode())

def get_client_id():
    id = input("Enter client id:")
    return id

if __name__ == "__main__":
    tempTup = getArgs()
    send(tempTup)