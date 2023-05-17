import asyncio

async def async_func1():
    print("Start async_func")
    await asyncio.sleep(1)
    print("End async_func")

async def async_func2():
    print("开始程序")
    await asyncio.sleep(1)
    print("结束程序")

async def main():
    print("Start main")
    task_list=[
        asyncio.create_task(async_func1()),
        asyncio.create_task(async_func2())
    ]
    await asyncio.wait(task_list)
    print("End main")

asyncio.run(main())
