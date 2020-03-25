#测试画布Canvas

from tkinter import *
import random

class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建画布组件"""
        self.canvas = Canvas(self, width=400, height=300, bg="blue")
        self.canvas.pack()
        """画直线"""
        line = self.canvas.create_line(10,15,30,35)         #直线确定起始点、终点坐标
        """画矩形"""
        rect = self.canvas.create_rectangle(20,20,60,60)     #矩形确定对角坐标
        """画椭圆"""
        oval = self.canvas.create_oval(20,20,60,60)          #椭圆确定外切矩形的对角坐标
        """画布中插入图片"""
        global photo
        photo = PhotoImage(file="imgs/ztg.gif")
        self.canvas.create_image(150,170, image=photo)        #插入图片确定终点坐标

        self.btn01 = Button(self, text="随机画10个矩形", command=self.create_run)
        self.btn01.pack(side="left")
        Button(self, text="关闭", command=root.destroy).pack(side="left")

    def create_run(self):
        """随机画10个矩形"""
        for i in range(0,10):
            x1 = random.randrange(int(self.canvas["width"])/2)        #起点坐标x1小于画布宽度的一半
            y1 = random.randrange(int(self.canvas["height"])/2)       #起点坐标y1小于画布高度的一半
            x2 = x1 + random.randrange(int(self.canvas["width"])/2)
            y2 = y1 + random.randrange(int(self.canvas["height"])/2)
            self.canvas.create_rectangle(x1,y1,x2,y2)

root = Tk()
root.title("画布测试窗口")
root.geometry("600x400+200+200")
app = Application(master=root)
root.mainloop()
