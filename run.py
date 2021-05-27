#! coding=utf-8
import time
import asyncio
import aiohttp
from create_data.create_data_search import CreateDataSearch


def clinic_request(data):
    """将每个门店的请求进行分组, 按照门店维度，取每个门店一个请求，进行分组"""
    clinic_req = []
    for x in range(len(data[0])):
        tmp = []
        for i in data:
            tmp.append(i[x])
        clinic_req.append(tmp)
    return clinic_req


async def request(req):
    async with aiohttp.ClientSession() as session:
        async with session.request(**req) as response:  # 发起请求
            print(await response.text())  # 运行时，不用等待


async def start_request(data):
    tasks = []
    for req in data:
        task = asyncio.create_task(request(req))
        tasks.append(task)
    for task in tasks:
        await task


if __name__ == "__main__":

    # 生成测试请求, clinic_count 同时请求多少家诊所；req_count：每家诊所多少个请求
    req_list = CreateDataSearch(env='test').create_data(clinic_count=3, req_count=2)  # 生成搜索模块数据
    data = clinic_request(req_list)  # 将数据进行按门店分组

    req_cost = []  # 所有响应耗时
    req_count = []
    n = 1
    count = 0  # 将所有请求发完后，循环发送
    while True:
        for i in data:
            status_list = []
            start_time = time.time()
            asyncio.get_event_loop().run_until_complete(start_request(i))
            end_time = time.time()
            req_cost.append(end_time - start_time)
            req_count.append(len(i))
            n += 1
        count += 1
        if count == 1:  # 将所有请求循环发送的次数
            break
    print(f"总共请求数: {sum(req_count)}")
    print(f"平均一秒处理请求数 ===>: {sum(req_count) / sum(req_cost)}")
