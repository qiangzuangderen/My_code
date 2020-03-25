#测试TCP客户端收发消息，假设是客户端先给服务器端发送信息
"""
操作流程：
1.创建client_socket;
2.创建与服务器端连接：connect()方法，服务器地址和端口号，元组形式；
3.建立发送和接收。
"""

from socket import *

TCP_client_socket = socket(AF_INET,SOCK_STREAM)
TCP_client_socket.connect(("192.168.3.2",8899))
while True:
    msg = input(">>:")
    TCP_client_socket.send(msg.encode("utf-8"))
    recv_data = TCP_client_socket.recv(1024)
    print("server said:{0}".format(recv_data.decode("utf-8")))
    if msg == "结束":
        break
TCP_client_socket.close()