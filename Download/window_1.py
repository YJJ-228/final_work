import ttkbootstrap as ttk
import downloader as dl


def download():
    url=entry1.get()
    dl.single_link(url=url)

def begin_window1():
    root.mainloop()

root = ttk.Toplevel()
style = ttk.Style()
style.theme_use('cerculean')
root.geometry("400x400")
root.title("窗口示例")
lb1=ttk.Label(root,text="请输入链接")
entry1 =ttk.Entry(root, width=40)
bt1=ttk.Button(root,text="下载",width=30,bootstyle="primary-outline",command=download)
lb1.pack()
entry1.pack(pady=30)
bt1.pack(pady=35)

if __name__=='__main__':
    begin_window1()
