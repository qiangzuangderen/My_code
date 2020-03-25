#测试下拉框组件

from tkinter import *

root = Tk()
root.title("测试下拉框组件")
root.geometry("200x100+200+200")

v = StringVar(root)
v.set("叫花鸡")
om = OptionMenu(root, v, "叫花鸡", "鱼香肉丝", "钱江肉丝")
om["width"] = 10
om.pack()

def test01():
    print("已点的菜：",v.get())

Button(root, text="确定", command=test01).pack(side="left")
Button(root, text="关闭", command=root.destroy).pack(side="left")

root.mainloop()