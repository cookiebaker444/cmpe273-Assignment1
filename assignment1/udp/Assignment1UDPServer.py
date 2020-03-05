import socket
import os

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
#MESSAGE = "pong"

def listen_forever():
    #path = os.path.realpath('cmpe273-spring20-master/assignment1/udp/')
    #print(path)
    #os.chdir(path)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    with open("./udp_sever_out.txt", "a") as f:
        while True:
        # get the data sent to us
            data, ip = s.recvfrom(BUFFER_SIZE)
            if data.decode(encoding="utf-8").__contains__('Upload successfully completed.'):
                print('Upload successfully completed.')
                f.close()
            else:
                print("{}: {}".format(ip, data.decode(encoding="utf-8").strip()))
                
                f.write(data.decode(encoding="utf-8").split(':')[2] + '\n')
            
            dataList = data.decode(encoding = "utf-8").split(":")
            MESSAGE = "Received ".encode() + dataList[1].encode()
            s.sendto(MESSAGE, ip)
        


listen_forever()