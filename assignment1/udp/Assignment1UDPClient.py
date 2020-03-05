import socket
import time
import os
import pathlib
from datetime import datetime

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
#MESSAGE = "ping"

def send(id=0):
    filename = './upload.txt'
    #path = os.path.realpath('cmpe273-spring20-master/assignment1/udp/')
    #print(path)
    #os.chdir(path)
    
    with open(filename, "r") as f:
        lines =   f.readlines()
        for i in range(0, len(lines)):
            MESSAGE = lines[i] + ":" + datetime.now().strftime("%H:%M:%S")
            #MARK = str(i + 1)
            while True:
                try:
                    while True:
                        try:
                            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                            s.sendto(f"{id}:{MESSAGE}".encode(), (UDP_IP, UDP_PORT))
                            s.settimeout(1.0)
                            data, ip = s.recvfrom(BUFFER_SIZE)
                            break
                        except OSError:
                            print("No package received")
                            continue
                    #print("received data: {}: {}".format(ip, data.decode()))
                    dataList = data.decode()
                    #print(dataList)
                    if dataList.__contains__(MESSAGE.split(':')[0]):
                        print("received data: {}: {}".format(ip, data.decode()))
                        break
                    else:
                        time.sleep(1)
                        print("Wrong message received")
                        continue
                except socket.error:
                    print("Error! {}".format(socket.error))
                    exit()
        s.sendto(f"{id}:{'Upload successfully completed.'}".encode(), (UDP_IP, UDP_PORT))
        print('Upload successfully completed.')
    f.close()

def get_client_id():
    id = input("Enter client id:")
    return id

send(get_client_id())