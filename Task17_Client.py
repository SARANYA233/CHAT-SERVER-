import socket
import threading 
from threading import Thread

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_ip="192.168.43.177"
server_port=1234

client_ip="192.168.43.45"
client_port=10050

s.bind( (client_ip,client_port) )
print("CHAT SERVER".center(60))

def send():

    while True:
        string=input("\n send>> ")
        s.sendto(bytes(string.encode()),(server_ip,server_port))
        if string == "bye":
            exit()

def recv():

    while True:
        x=s.recvfrom(1024)
        data=x[0].decode()
        print("\n receive>> "+data)
        if data == "bye":
            exit()


Thread(target=send).start()

Thread(target=recv).start()
