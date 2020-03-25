#测试颜色选择框、文件选择框

from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *

root = Tk()
root.title("测试颜色选择框")
root.geometry("400x300+200+200")

def window01():
    a1 = askcolor(color="red", title="选择背景色")
    print(a1)
    l1.config(bg=a1[1])

def window02():
    """askopenfilename方法的返回值为文件的路径"""
    f = askopenfilename(title="上传文件", initialdir="d:/学习资料", filetypes=[("视频文件",".mp4")])
    l1["text"] = f
    print(f)

def window03():
    with askopenfile(title="读取文本文件", initialdir="d:/学习资料", filetypes=[("文本文件",".txt")]) as f:
        l1["text"] = f.read()

Button(root, text="选择颜色", command=window01).pack(side="left")
Button(root, text="选择视频文件",command=window02).pack(side="left")
Button(root, text="选择读取的文件", command=window03).pack(side="left")

l1 = Label(root, width=200, height=100, bg="black", fg="white")
l1.pack()

root.mainloop()