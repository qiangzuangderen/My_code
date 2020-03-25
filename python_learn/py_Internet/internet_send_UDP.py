#测试UDP协议发送数据
"""
步骤：
1.创建socket套接字，UDP协议使用SOCK_DGRAM；
2.创建目的IP地址，端口号；
3.输入要发送的内容；
4.sendto()方法，发送内容，规定接收端的数据格式和接收地址；
5.关闭发送套接字
"""

from socket import *

#创建UDP协议套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)
#创建目的地址，端口号
addr = ("192.168.3.2",8080)
#输入要发送的内容
data = input("please input message:")
#发送内容，sendto()方法，规定接收端的数据格式，地址
udp_socket.sendto(data.encode("gb2312"),addr)
#关闭socket
udp_socket.close()