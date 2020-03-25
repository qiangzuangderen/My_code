#测试消息的发送和接收

from socket import *

udp_socket = socket(AF_INET,SOCK_DGRAM)
"""绑定发送端口：8899"""
udp_socket.bind(("",8899))
addr = ("192.168.3.2",8080)
send_data = input("please input a message:")
"""发送时为编码，格式为"gb2312""""
udp_socket.sendto(send_data.encode("gb2312"),addr)
"""本次最大接收字长为1024"""
recv_data = udp_socket.recvfrom(1024)
"""接收是为解码，格式为"gb2312",接收数据为元组格式(数据内容,"发送方IP地址，端口号")"""
print("recive a message from {0}:{1}".format(recv_data[1],recv_data[0].decode("gb2312")))
udp_socket.close()