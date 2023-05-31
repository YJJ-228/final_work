import ttkbootstrap as ttk
import downloader as dl

def download():
    url=entry2.get()
    dl.large_documents(url=url)

def begin_window2():
    root.mainloop()

root = ttk.Toplevel()
style = ttk.Style()
style.theme_use('cerculean')
root.geometry("400x400")
root.title("窗口示例")
lb2=ttk.Label(root,text="请输入链接")
entry2 =ttk.Entry(root, width=40)
bt2=ttk.Button(root,text="下载",width=30,bootstyle="primary-outline",command=download)
lb2.pack()
entry2.pack(pady=30)
bt2.pack(pady=20)

if __name__=='__main__':
    begin_window2()