#测试tftp客户端

import struct
from socket import *

filename = "aa.jpg"
server_ip = "127.0.0.1"
send_data = struct.pack("!H{0}sb5sb".format(len(filename)),1,filename.encode(),0,"octet".encode(),0)
udp_socket = socket(AF_INET,SOCK_DGRAM)
udp_socket.sendto(send_data,(server_ip,69))
f = open(filename,"ab")
while True:
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data)
    caozuoma,ack_num = struct.unpack("!HH",recv_data[0][:4])
    if caozuoma == 5:
        print("文件不存在")
        break
    f.write(recv_data[0][4:])
    if len(recv_data[0]) < 516:
        break
    ack_data = struct.pack("!HH",4,ack_num)
    rand_port = recv_data[1][1]
    udp_socket.sendto(ack_data,(server_ip,rand_port))
