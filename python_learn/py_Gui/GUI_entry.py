#测试文本框Label、输入框Entry、单选框RadioButton、复选按钮CheckButton

from tkinter import *
from tkinter import messagebox

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):

        """创建文本框（"用户名"）"""
        self.label01 = Label(self, text="用户名")
        self.label01.pack()
        """创建输入框，设置对象v1，将输入框的内容传递给v1"""
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()
        v1.set("yang")

        self.label02 = Label(self, text="密  码")
        self.label02.pack()

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2, show="*")
        self.entry02.pack()

        """"创建单选按钮"""
        self.v = StringVar()
        self.v.set("F")
        self.r1 = Radiobutton(self, text="男性", value="M", variable=self.v)
        self.r2 = Radiobutton(self, text="女性", value="F", variable=self.v)
        self.r1.pack(side="left");self.r2.pack(side="left")

        """创建复选按钮"""
        self.codeHobby = IntVar()        #复选框以int值的形式返回，0表示未选中，1表示选中
        self.vadioHobby = IntVar()
        self.c1 = Checkbutton(self, text="敲代码", variable=self.codeHobby, onvalue=1, offvalue=0)
        self.c2 = Checkbutton(self, text="看视频", variable=self.vadioHobby, onvalue=1, offvalue=0)
        self.c1.pack(side="left");self.c2.pack(side="left")

        Button(self, text="登录", command=self.login).pack(side="left")
        Button(self, text="关闭", command=root.destroy).pack(side="left")

    def login(self):
        usrname = self.entry01.get()
        psw = self.entry02.get()
        if usrname=="yang" and psw=="123456" and self.codeHobby.get()==1:
            messagebox.showinfo("登录提示","登录成功,居然喜欢敲代码")
            print("用户名：", self.entry01.get())
            print("密  码：", self.entry02.get())
            print("性  别：",self.v.get())
            print("兴趣爱好：",self.c1["text"])          #打印复选按钮的内容，为字典形式，key="text"
        elif usrname=="yang" and psw=="123456" and self.vadioHobby.get()==1:
            messagebox.showinfo("登录提示","登录成功，懒人看视频")
            #print("兴趣爱好：",self.c2.getvar())
        else:
            messagebox.showinfo("登录提示","登录失败，用户名或密码错误！")

if __name__=="__main__":
    root = Tk()
    root.title("测试窗体")
    root.geometry("600x400+200+200")
    app = Application(master=root)
    root.mainloop()