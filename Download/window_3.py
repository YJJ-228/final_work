import ttkbootstrap as ttk
import downloader as dl

def download():
    url=entry1.get()
    urllist=url.split(",")
    dl.multi_link(urllist)

def begin_window3():
    root.mainloop()

root = ttk.Toplevel()
style = ttk.Style()
style.theme_use('cerculean')
root.geometry("400x400")
root.title("窗口示例")
lb1=ttk.Label(root,text="请输入链接,以逗号分开")
entry1 =ttk.Entry(root,width=40)
entry1.place(width=300,height=120,x=50,y=50)
bt1=ttk.Button(root,text="下载",width=30,bootstyle="primary-outline",command=download)
lb1.pack()
bt1.pack(pady=160)

if __name__=='__main__':
    begin_window3()