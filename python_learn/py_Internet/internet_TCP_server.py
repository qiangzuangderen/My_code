#测试TCP服务器端接收数据
"""
操作流程：
1.创建服务器socket；
2.绑定端口，端口表示为元组形式；
3.建立监听，请求等待缓存区；
4.创建客户端与服务器连接（三次握手），返回client_socket对象，用于读取客户端信息；
5.创建消息接收缓存区；
6.接收消息，解码；
7.关闭客户端连接，关闭服务器端连接。
"""

from socket import *

TCP_server_socket = socket(AF_INET,SOCK_STREAM)
TCP_server_socket.bind(("",8899))
TCP_server_socket.listen(10)
client_socket,client_info = TCP_server_socket.accept()    #client_socket为客户端对象，client_info为客户端地址与端口号
try:
    while True:
        recv_data = client_socket.recv(1024)
        print("client said:{0}".format(recv_data.decode("utf-8")))
        msg = input(">>:")
        client_socket.send(msg.encode("utf-8"))
        if msg == "结束":
            break
except Exception as e:
    print("客户端已关闭")
finally:
    TCP_server_socket.close()