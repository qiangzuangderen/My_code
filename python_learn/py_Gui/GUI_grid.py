#grid布局管理器
"""
grid布局管理器：
1.row(行)，column(列)均从0计数
2.sticky为同格的位置
"""

from tkinter import *
from tkinter import messagebox

class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.createWidget()

    def createWidget(self):
        self.lebal01 = Label(self, text="用户名").grid(row=0, column=0)
        v1 = StringVar()     #定义v1为局部变量是因为方法调用完成后可以销毁
        v1.set("admin")
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.grid(row=0, column=1)
        self.lebal02 = Label(self, text="密  码").grid(row=1, column=0)
        v2 = StringVar()           #定义v2为局部变量是因为方法调用完成后可以销毁
        self.entry02 = Entry(self, textvariable=v2, show="*")
        self.entry02.grid(row=1,column=1)
        Button(self, text="确定", command=self.create_run).grid(row=2, column=1, sticky=W)
        Button(self, text="退出", command=root.destroy).grid(row=2, column=1, sticky=E)

    def create_run(self):
        usrname = self.entry01.get()
        pwd = self.entry02.get()
        if usrname == "yang" and pwd == "123456":
            messagebox.showinfo("登录提示","登录成功")
        else:
            messagebox.showinfo("登录提示","登录失败，用户名或密码错误")

root = Tk()
root.title("测试grid管理器布局")
root.geometry("600x400+200+200")
app = Application(master=root)
root.mainloop()
