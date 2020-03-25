#多线程聊天服务器端
"""
服务器端的作用：
1.创建客户端连接；
2.创建客户端发送内容的缓存区；
3.管理客户端client_socket；
4.中转客户端发送的内容；
"""

from socket import *
from threading import Thread
#创建client_socket接收客户端输入的容器
sockets = []

def TCP_server_read(client_socket):
    while True:
        data_recv = client_socket.recv(1024)
        if data_recv.decode("utf-8").endswith("结束"):
            sockets.remove(client_socket)  #清除accept中当前客户端socket
            client_socket.close()
            break

        if len(data_recv) > 0:   #不能发空字符串
            #遍历接收到客户端所有输入的内容，转发到另外的客户端
            for socket in sockets:
                socket.send(data_recv)

def main():
    TCP_server_socket = socket(AF_INET,SOCK_STREAM)
    TCP_server_socket.bind(("",8899))
    TCP_server_socket.listen(1024)
    while True:
        client_socket,client_info = TCP_server_socket.accept()
        sockets.append(client_socket)
        t_read = Thread(target=TCP_server_read,args=(client_socket,))
        t_read.start()

if __name__ == "__main__":
    main()