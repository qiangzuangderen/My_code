#模拟多线程聊天
"""
操作流程：
1.创建socket，绑定端口（端口是元组形式）；
2.创建接收方法，确定接收缓冲区，规定解码格式；
3.创建发送方法，确定接收方IP地址、端口号，规定编码格式；
4.创建线程，启动线程，线程等待。
"""

from threading import Thread
from socket import *

udp_socket = socket(AF_INET,SOCK_DGRAM)
udp_socket.bind(("",8899))   #端口号为元组形式

def udp_recv():
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print("{0}:{1}".format(recv_data[1],recv_data[0].decode("gb2312")))

def udp_send():
    while True:
        addr = ("192.168.3.2",8080)
        send_data = input(">>:")
        udp_socket.sendto(send_data.encode("gb2312"),addr)

if __name__ == "__main__":
    T_send = Thread(target=udp_send)
    T_recv = Thread(target=udp_recv)
    T_send.start()
    T_recv.start()
    T_send.join()
    T_recv.join()