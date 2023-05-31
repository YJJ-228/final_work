import ttkbootstrap as ttk

class Window():
    def __init__(self):
        self.root = ttk.Toplevel()
        self.style = ttk.Style()
        self.style.theme_use('cerculean')
        self.root.geometry("400x400")
        self.root.title("窗口示例")

        self.style = ttk.Style()
        self.style.theme_use('cerculean')
        self.btn1 = ttk.Button(self.root, text="单链接", 
                                bootstyle="primary-outline",
                                command=self.open_window1)
        self.btn2 = ttk.Button(self.root, text="大文件", 
                                bootstyle="primary-outline",
                                command=self.open_window2)
        self.btn3 = ttk.Button(self.root, text="多链接", 
                                bootstyle="primary-outline",
                                command=self.open_window3)
        self.btn1.pack(pady=20)
        self.btn2.pack(pady=25)
        self.btn3.pack(pady=30)
        self.btn1.configure(width=25)
        self.btn2.configure(width=25)
        self.btn3.configure(width=25)
        self.root.mainloop()

    # 打开下载窗体
    def open_window1(self):
        import window_1
        window_1.begin_window1()
    
    def open_window2(self):
        import window_2
        window_2.begin_window2()
    def open_window3(self):
        import window_3
        window_3.begin_window3()
