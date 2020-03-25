#测试os.shutil模块
import os
import shutil
import zipfile

os.remove("file/new_pp.txt")
shutil.copyfile("file/pp.txt","file/new_pp.txt")
os.rmdir("new_file")

#拷贝file目录到new_file目录，过滤原目录中的*.dat文件和*.csv文件
shutil.copytree("file","new_file",ignore=shutil.ignore_patterns("*.dat","*.csv"))

#压缩和解压缩
#1.使用shutil模块
shutil.make_archive("file/new_zip","zip","new_file")     #shutil.make_archive()方法使用三个参数：目的文件、压缩格式、源文件

#2.使用zipfile模块Zipfile()方法

zip_file = zipfile.ZipFile(r"file/data.zip","w")        #确定目标文件
zip_file.write("file/data.dat")                         #确定源文件并写入
zip_file.close()                                        #关闭文件


#3.解压缩
unzip_file = zipfile.ZipFile(r"file/data.zip","r")      #确定源文件
unzip_file.extractall(r"file/zip")                      #确定目标目录
unzip_file.close()                                      #关闭文件


