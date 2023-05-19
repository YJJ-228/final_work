import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from project1 import Project1
from ttkbootstrap import Style
from draw_functions import DrawFunctions

class First:
    def __init__(self):
        self.root = ttk.Toplevel()
        self.root.title("股票代码")
        self.root.geometry("400x250")
        
        self.Label1=ttk.Label(self.root,text="行业上市公司及行业财务数据分析及可视化",bootstyle=INFO)
        self.Label1.pack(pady=5)

        self.Label2=ttk.Label(self.root,text="请输入股票代码（sz.xxxxxx）",bootstyle=INFO)
        self.Label2.pack()

        self.entry1 =ttk.Entry(self.root, width=15)
        self.entry1.pack(pady=2)

        self.Label3=ttk.Label(self.root,text="请输入开始的年份",bootstyle=INFO)
        self.Label3.pack()

        self.entry2 =ttk.Entry(self.root, width=15)
        self.entry2.pack(pady=2)
        
        self.btn1 = ttk.Button(self.root, text="查询",bootstyle=PRIMARY,command=self.openproject)
        self.btn1.place(x=135,y=180)

        self.btn2 = ttk.Button(self.root, text="返回",bootstyle=PRIMARY,command=self.root.destroy)
        self.btn2.place(x=210,y=180)

        self.root.mainloop()
    
    def openproject(self):
        code = self.entry1.get()
        year = self.entry2.get()
        self.project1 = Project1(code,year)
        draw_functions_instance = DrawFunctions(code,year)
        draw_functions_instance.get_profit_data()
