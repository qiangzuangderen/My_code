#测试简单对话框

from tkinter import *
from tkinter.simpledialog import *

root = Tk()
root.title("测试窗口")
root.geometry("500x300+200+200")

def simple_test():
    """simpleDialog输入框3个类型，使用方法相同
    1.askinteger:输入整型数据；
    2.askfloat:输入浮点型数据；
    3.askstring:输入字符串。"""
    a = askinteger(title="年龄输入框", prompt="请输入年龄", initialvalue=18, minvalue=1, maxvalue=160)    #对象返回输入的内容
    show["text"] = a

Button(root, text="登记年龄", command=simple_test).pack()
show = Label(root, width=200, height=100, bg="white", fg="blue")
show.pack()

root.mainloop()
