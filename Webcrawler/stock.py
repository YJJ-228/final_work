import requests
import json
import schedule

#沪A股单日排行
url='https://push2.eastmoney.com/api/qt/clist/get?fid=f62&po=1&pz=50&pn=1&np=1&fltt=2&invt=2&fs=m:1+t:2+f:!2,m:1+t:23+f:!2&fields=f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124,f1,f13'
#沪A股三日排行
# url='https://push2.eastmoney.com/api/qt/clist/get?fid=f267&po=1&pz=50&pn=1&np=1&fltt=2&invt=2&fs=m:1+t:2+f:!2,m:1+t:23+f:!2&fields=f12,f14,f2,f127,f267,f268,f269,f270,f271,f272,f273,f274,f275,f276,f257,f258,f124,f1,f13'
header={
    'Referer':'http://quote.eastmoney.com/',
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
}
cookie = {
    'qgqp_b_id': 'b58c84940e1f10c814c3c4c76b892770',
    'HAList': 'ty-0-002156-%u901A%u5BCC%u5FAE%u7535%2Cty-1-688361-N%u98DE%u6D4B-U%2Cty-1-600519-%u8D35%u5DDE%u8305%u53F0'}

def stock_taking():
    pagelist = input('请输入页数，多个页码用逗号分隔：').split(',')
    pagelist = [int(p) for p in pagelist]  # 将输入的字符串转换为整数列表
    table = [] #定义储存列表
    print("\n{:<7}{:<7}{:<8}{}".format('股票代码','公司名称','涨幅','最新价'))
    for i in pagelist:
        param={'pn':i}
        response = requests.get(url, headers=header, cookies=cookie, params=param)
        if response.status_code == 200:
            j = json.loads(response.text)
            for item in j['data']['diff']:
                name = item['f14']
                data = item['f12']
                increase='%'+str(item['f3'])
                new_price=item['f2']
                table.append([data,name,increase,new_price])
                print('{:<11}{:<6}{:<11}{}'.format(data,name,increase,new_price))
                with open('D:/Code/final_work/Webcrawler/file.csv','w',encoding='utf-8')as f:
                    for row in table:
                        line = ','.join([str(elem) for elem in row]) + '\n'
                        f.write(line)
    return table

def job():
    table=[]
    response = requests.get(url, headers=header, cookies=cookie, params={'pn':1})
    if response.status_code == 200:
        j = json.loads(response.text)
        with open('D:/Code/final_work/Webcrawler/file.csv','w',encoding='utf-8')as f:
            for item in j['data']['diff']:
                name = item['f14']
                data = item['f12']
                increase='%'+str(item['f3'])
                new_price=item['f2']
                table.append([data,name,increase,new_price])
            for row in table:
                line = ','.join([str(elem) for elem in row]) + '\n'
                f.write(line)
            

def every_day_job():
    schedule.every().day.at("08:46").do(job)
    while True:
        schedule.run_pending()

if __name__ == '__main__':
    # every_day_job()
    stock_taking()