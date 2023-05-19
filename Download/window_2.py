import ttkbootstrap as ttk
import downloader as dl

def download():
    url=entry1.get()
    dl.large_documents(url=url)

root = ttk.Window()
root.geometry("400x400")
root.title("窗口示例")
lb1=ttk.Label(root,text="请输入链接")
entry1 =ttk.Entry(root, width=40)
bt1=ttk.Button(root,text="下载",width=30,command=download)
lb1.pack()
entry1.pack()
bt1.pack(pady=50)
root.mainloop()