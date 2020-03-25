#测试鼠标和键盘事件

from tkinter import *

root = Tk()
root.title("测试鼠标和键盘事件")
root.geometry("600x400+200+200")
c1 = Canvas(root, width=300, height=200, bg="blue")
c1.pack()

"""打印鼠标左键点击的当前位置"""
def mouseTest(event):
    print("鼠标单击位置（相对于父容器）：{0},{1}".format(event.x,event.y))
    print("鼠标左键单击位置（相对于屏幕）：{0},{1}".format(event.x_root,event.y_root))
    print("事件绑定的组件：{0}".format(event.widget))

"""打印鼠标左键移动的位置"""
def testDrag(event):
    c1.create_oval(event.x,event.y,event.x+1,event.y+1)

"""打印按键的属性"""
def keyboardTest(event):
    print("键的keycode:{0},键的char:{1},键的keysym:{2}"
          .format(event.keycode, event.char, event.keysym))
"""打印按键a的属性"""
def press_a_test(event):
    print("press a")

"""打印释放按键a的属性"""
def release_a_test(event):
    print("release a")

"""绑定左键按下和拖动触发的事件"""
c1.bind("<Button-1>",mouseTest)
c1.bind("<B1-Motion>",testDrag)

"""绑定键盘触发的事件"""
root.bind("<KeyPress>",keyboardTest)
root.bind("<KeyPress-a>",press_a_test)
root.bind("<KeyRelease-a>",release_a_test)

root.mainloop()