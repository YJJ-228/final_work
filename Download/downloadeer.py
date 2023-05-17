import requests
from tqdm import tqdm
import asyncio

# 单链接下载
class downloader(object):
    def __init__(self,url):
        self.url=url
    
    # 小文件下载
    def simple_download(self):
        response=requests.get(self.url)
        name = self.url.split("/")[-1]
        with open('D:/Code/Download/file/'+name,'wb')as f:
            if response.status_code==200:
                f.write(response.content)
                print('下载完成')
            else:
                print('下载失败！')
    
    # 大文件下载
    def large_download(self):
        response=requests.get(self.url,stream=True)
        total = int(response.headers.get('content-length', 0)) #得到文件长度，初始化为0
        name = self.url.split("/")[-1]
        with open('D:/Code/Download/file/'+name,'wb')as f,tqdm(    #初始化tqdm
            desc='下载进度：',
            total=total,
            unit='KB',
            unit_scale=True,
            unit_divisor=256,
            ) as bar:
            for chunk in response.iter_content(chunk_size=1024*1024*8):
                if response.status_code==200: #判断网络是否连通                                       
                    if chunk:  #如果不是空文件
                        f.write(chunk)
                        bar.update(f.write(chunk))
                else:
                    print('下载失败！')

# 多链接下载 
class multi_link_downloader(object):
    def __init__(self,urllist):
        self.urllist=urllist

    # 异步下载
    async def asyncio_download(self,url_new):
        response=requests.get(url_new)
        name = url_new.split("/")[-1]
        with open('D:/Code/Download/file/'+name,'wb')as f:
            if response.status_code==200:
                f.write(response.content)
                print('下载完成')
            else:
                print('下载失败！')
    ()
    async def asyncio_main(self):
        task_list=[]
        for i in self.urllist:
            task_list.append(asyncio.create_task(self.asyncio_download(url_new=i)))
        await asyncio.wait(task_list)
        print('结束')
    
    
def multi_link():
    urllist=[]
    print('请输入要下载的链接，输入0结束：')
    while True:
        url=input("")
        if url!='0':
            urllist.append(url)
        else:
            break
    me=multi_link_downloader(urllist=urllist)
    asyncio.run(me.asyncio_main()) # 运行异步主函数


if __name__=='__main__':
    multi_link()
    
