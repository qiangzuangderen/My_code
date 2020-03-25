#使用lambda函数在事件中传递参数及三种绑定事件的方法

from tkinter import *

root = Tk()
root.title("使用lambda函数传递参数")
root.geometry("500x300+200+200")

def mouse_Test1(event):
    print("使用获取event事件方式")
    print(event.widget)

def mouse_Test2(a,b):
    print("使用command方式，用lambda函数传递参数：a={0},b={1}".format(a,b))

def mouse_Text3(event):
    print("使用bind_class方式，把组件类中所有组件都绑定事件")
    print(event.widget)

"""1.通过bind()方法绑定（适合需要获取event对象，鼠标、键盘事件等）"""
btn01 = Button(root, text="测试test1")
btn01.pack(side="left")
btn01.bind("<Button-1>",mouse_Test1)

"""2.使用command方式绑定事件，用lambda函数传参，语法：lambda:函数名称（参数1，参数2，…………）适合不需要获取事件的情况"""
Button(root, text="测试text2", command=lambda: mouse_Test2("yang", "lin")).pack(side="left")
Button(root, text="关闭", command=root.destroy).pack(side="left")

"""3.通过调用对象的bind_class函数，将该组件类所有的组件绑定事件"""
btn01.bind_class("Button", "<Button-3>", mouse_Text3)

root.mainloop()