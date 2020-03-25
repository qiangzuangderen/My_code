#打印工作目录中类型为"py"的文件

import os

path = os.getcwd()           #获取工作目录
print(path)

print("########方法一：####################")
file_list = [filename for filename in os.listdir(path) if filename.endswith("py")]
#print(file_list)
for f in file_list:
    print(f)


print("###############方法二：#################")
file_list2 = os.listdir(path)
for file_name in file_list2:
    if file_name.endswith("py"):
        print(file_name)