
from tkinter import *
from tkinter import messagebox

class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):

        """创建组件，使用关键字参数(传入为字典方式)：
        (text为组件内容，width为宽度字节数，height为高度字节数，
        bg为背景色，fg为前景色，font为字体(表示为元组，("字体"，字号)))"""
        self.btn01 = Button(self, text="登录", command=self.login)
        self.btn01.pack()
        self.label01 = Label(self, text="测试文本框", width=10, height=2, bg="white", fg="red")
        self.label01["text"] = "第一个文本框"
        self.label01.configure(bg="yellow", fg="blue")
        self.label01.pack()
        self.label02 = Label(self, text="python3.7", width=10, height=2, bg="white", fg="red", font=("仿宋",33))
        self.label02.pack()
        self.btn01 = Button(self, text="关闭", command=root.destroy)
        self.btn01.pack()

        """插入图片，photo为局部变量，方法执行完后销毁，须将photo定义为全局变量，image为插入的图片"""
        global photo
        photo = PhotoImage(file="imgs/ztg.gif")     #imgs/ztg.gif为图片相对路径
        self.label03 = Label(self, image=photo)
        self.label03.pack()

    def login(self):
        messagebox.showinfo("登录提示","登录成功")


if __name__=="__main__":           #程序运行入口
    root = Tk()
    root.title("测试窗口")
    root.geometry("600x400+200+200")
    app = Application(master=root)
    root.mainloop()