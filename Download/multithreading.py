# 导入所需的库
import requests
import time
import asyncio

class Downloader:

    # 初始化方法，接受文件链接和线程数作为参数
    def __init__(self, url, num):
        self.url = url  # 文件链接
        self.num = num  # 线程数
        self.name = url.split('/')[-1]  # 文件名
        self.downloaded = 0  # 已下载的字节数
        self.start_time = 0  # 开始时间

        # 获取文件大小，并创建一个同样大小的空文件
        response = requests.head(self.url)
        self.size = int(response.headers['Content-Length'])  # 文件大小

    # 定义一个下载方法，接受开始位置和结束位置作为参数
    async def download(self, start, end):
        # 设置请求头，指定要下载的范围
        headers = {'Range': f'bytes={start}-{end}'}
        # 发起请求，获取响应内容
        response = requests.get(self.url, headers=headers, stream=True)
        # 打开文件，并移动指针到开始位置
        with open('Download/file/video_D.mp4','wb')as f:
            # 写入响应内容到文件中
            for chunk in response.iter_content(1024):
                f.write(chunk)
                # 更新已下载的字节数
                self.downloaded += len(chunk)

    # 定义一个主方法，执行多线程下载
    async def main(self):
        # 计算每个线程要下载的字节数
        part = self.size // self.num
        # 记录开始时间
        self.start_time = time.time()
        print(f'开始下载 {self.name} ...')
        tasks = []
        for i in range(self.num):
            start = part * i  # 开始位置
            if i == self.num - 1:  # 最后一个线程
                end = self.size - 1  # 结束位置
            else:
                end = start + part - 1  # 结束位置 
            task = asyncio.create_task(self.download(start=start,end=end))  # 创建任务
            tasks.append(task)  # 添加到任务列表
        await asyncio.wait(tasks)  # 等待所有任务完成
        print(f'下载完成 {self.name} !')
        
        # 计算并显示总耗时和平均速度
        end_time = time.time()  # 结束时间
        total_time = end_time - self.start_time  # 总耗时
        average_speed = self.size / total_time / 1024 / 1024  # 平均速度
        
        print(f'总耗时：{total_time:.2f} 秒')
        print(f'平均速度：{average_speed:.2f} MB/s')

# 测试代码，使用一个视频文件作为示例
if __name__ == '__main__':
    url = 'https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/1250921_c7af3a2b73d03604f6421ef11134af72.mp4'
    downloader = Downloader(url, 10)  # 创建一个下载器对象，使用10个线程
    asyncio.run(downloader.main())  # 调用主方法开始下载

