# project1.py
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from draw_functions import DrawFunctions

class Project1():
    def __init__(self,code,beginning,ending):
        self.code=code
        self.beginning=beginning
        self.ending=ending
        self.project_window = ttk.Toplevel()
        self.project_window.title("股票查询结果")
        self.project_window.geometry("400x300")

        self.btnn1 = ttk.Button(self.project_window, text="绘制财报指标比较条形图", bootstyle="success-outline",command=self.draw_picture1)
        self.btnn1.pack(padx=10, pady=10)
        self.btnn1.configure(width=45)
        # Checkbutton(bootstyle="square-toggle")

        self.btn2 = ttk.Button(self.project_window, text="绘制主营营业收入与净利润比较柱形图",bootstyle="info-outline", command=self.draw_picture2)
        self.btn2.pack(padx=10, pady=10)
        self.btn2.configure(width=45)
        
        self.btn3 = ttk.Button(self.project_window, text="绘制不同类型的子图", bootstyle="primary-outline",command=self.draw_picture3)
        self.btn3.pack(padx=10, pady=10)
        self.btn3.configure(width=45)

        self.btn5 = ttk.Button(self.project_window, text="打印\保存到本地桌面",bootstyle="dark-outline", command=self.draw_picture5)
        self.btn5.pack(padx=10, pady=10)
        self.btn5.configure(width=45)

        self.btn6 = ttk.Button(self.project_window, text="返回",command=self.project_window.destroy)
        self.btn6.pack(padx=10, pady=10)

    def draw_picture1(self):
        draw_funcs = DrawFunctions(self.code,self.beginning,self.ending)
        draw_funcs.draw_picture1()

    def draw_picture2(self):
        draw_funcs = DrawFunctions(self.code,self.beginning,self.ending)
        draw_funcs.draw_picture2()

    def draw_picture3(self):
        draw_funcs = DrawFunctions(self.code,self.beginning,self.ending)
        draw_funcs.draw_picture3()

    def draw_picture5(self):
        draw_funcs = DrawFunctions(self.code,self.beginning,self.ending)
        draw_funcs.printresult()