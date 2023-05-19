import ttkbootstrap as ttk
import downloader as dl

def download():
    url=entry2.get()
    dl.large_documents(url=url)

root = ttk.Window()
root.geometry("400x400")
root.title("窗口示例")
lb2=ttk.Label(root,text="请输入链接")
entry2 =ttk.Entry(root, width=40)
bt2=ttk.Button(root,text="下载",width=30,command=download)
lb2.pack()
entry2.pack(pady=30)
bt2.pack(pady=20)
root.mainloop()