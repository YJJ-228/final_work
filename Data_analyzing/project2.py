# project2.py

import tkinter as tk
from draw_functions import DrawFunctions

class Project2():
    def __init__(self):
        self.project_window = tk.Toplevel()
        self.project_window.title("项目2")

        self.btn1 = tk.Button(self.project_window, text="画图1", command=self.draw_picture1)
        self.btn1.pack(padx=10, pady=10)

        self.btn2 = tk.Button(self.project_window, text="画图2", command=self.draw_picture2)
        self.btn2.pack(padx=10, pady=10)

    def draw_picture1(self):
        draw_funcs = DrawFunctions()
        draw_funcs.draw_picture1()

    def draw_picture2(self):
        draw_funcs = DrawFunctions()
        draw_funcs.draw_picture2()