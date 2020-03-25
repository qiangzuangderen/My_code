#多线程TCP聊天客户端
"""
客户端的作用：
1.连接服务器端；
2.发送内容；
3.接收内容；
4.终止动作。
"""

from socket import *
from threading import Thread

TCP_client_socket = socket(AF_INET,SOCK_STREAM)
TCP_client_socket.connect(("192.168.3.2",8899))
username = input("please input username:")
#判断下线的标志
flag = True

"""接收内容"""
def readMsg(TCP_client_socket):
    while flag:
        data_recv = TCP_client_socket.recv(1024)
        print("收到信息：",data_recv.decode("utf-8"))

"""发送内容"""
def writeMsg(TCP_client_socket):
    global flag
    while flag:
        msg = input(">>：")
        msg = username + "said：" + msg
        data_send =TCP_client_socket.send(msg.encode("utf-8"))
        #判断输入字符串是否以"结束"结尾
        if msg.endswith("结束") :
            flag = False
            break


t_client_read = Thread(target=readMsg,args=(TCP_client_socket,))
t_client_read.start()
t_client_write = Thread(target=writeMsg,args=(TCP_client_socket,))
t_client_write.start()
t_client_read.join()
t_client_write.join()
TCP_client_socket.close()
