
from tkinter import *
from tkinter import messagebox

class Application(Frame):                #继承父类"Frame"
    def __init__(self,master=None):
        super().__init__(master)          #调用父类的定义
        self.master = master
        self.pack()
        self.createWidget()       #窗体初始化时装入组件

    def createWidget(self):
        """创建组件"""
        self.btn01 = Button(self)
        self.btn01["text"] = "点我送花"     #字典方式返回
        self.btn01["command"] = self.songhua         #确定组件事件触发的方法
        self.btn01.pack()
        """"关闭"按钮"""
        self.btnquit = Button(self, text="关闭", command=root.destroy)
        self.btnquit.pack()

    def songhua(self):
        messagebox.showinfo("送花","就送一朵花")



root = Tk()
root.title("经典的面向对象GUI程序")
root.geometry("500x300+200+200")
app = Application(master=root)

root.mainloop()
