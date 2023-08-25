import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from firstttk import First
import sys

# 第一个主界面
class MainWindow:
    def __init__(self):
        self.root = ttk.Window()
        self.root.geometry("300x200")
        self.root.title("窗口示例")

        # Create a ttk.Style() object and set the theme
        self.style = ttk.Style()
        self.style.theme_use('cerculean')

        self.btn1 = ttk.Button(self.root, text="项目一\n财务指标可视化分析", 
                                bootstyle="primary-outline",
                                command=self.open_window1)
        self.btn1.pack(padx=10, pady=20)
        self.btn1.configure(width=25)
        # button.configure(padding=(20, 3))

        self.btn2 = ttk.Button(self.root, text="项目二\n数据下载器",
                               bootstyle="primary-outline",
                              command=self.open_window2)
        self.btn2.pack(padx=10, pady=25)
        self.btn2.configure(width=25)

        self.root.mainloop()

    def open_window1(self):
        self.first = First()

    def open_window2(self):
        sys.path.append("./Download")
        import tk_download
        self.project2 = tk_download.Window()
    

if __name__ == "__main__":
    app = MainWindow()