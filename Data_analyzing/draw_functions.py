import baostock as bs
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

class DrawFunctions:
    
    def __init__(self,code,beginning,ending):
        self.code=code
        self.beginning=beginning
        self.ending=ending

    def get_profit_data(self):
        lg = bs.login() # 登录系统
        result_list = []
        year_list = pd.date_range(self.beginning+'1231', periods=int(self.ending)-int(self.beginning)+1, freq='1Y').strftime("%Y")
        for year in tqdm(year_list): # 在这里使用tqdm显示进度条
            return_data = bs.query_profit_data(code=self.code, year=year, quarter=4)
            while (return_data.error_code == '0') & return_data.next():
                result_list.append(return_data.get_row_data())
        result_table = pd.DataFrame(result_list, columns=return_data.fields)
        bs.logout() #退出系统
        result_table.rename(columns={'code':'证券代码','pubDate':'发布日期','statDate':'财报日期','roeAvg':'净资产收益率','npMargin':'销售净利率','gpMargin':'销售毛利率','netProfit':'净利润','epsTTM':'每股收益','MBRevenue':'主营营业收入','totalShare':'总股本','liqaShare':'流通股本'},inplace = True)
        profit_data = result_table.iloc[:, 0:9]
        profit_data = profit_data.astype({'净资产收益率':'float','销售净利率':'float','销售毛利率':'float','净利润':'float','每股收益':'float','主营营业收入':'float'})
        pd.options.display.float_format = '{:.4f}'.format # 保留4位小数
        profit_data.to_csv('./chart', index=False, encoding ='utf-8')
        # growth_data = result_table.astype({'净资产同比增长率':'float','总资产同比增长率':'float','净利润同比增长率':'float','基本每股收益同比增长率':'float','归属母公司股东净利润同比增长率':'float'})
        # # 将文本格式转化为数值格式
        # pd.options.display.float_format = '{:.2f}'.format#保留2位百分数小数
        return (profit_data)
    
    def printresult(self):
        profit_data=self.get_profit_data()
        print(profit_data)

    def draw_picture1(self):
        profit_data=self.get_profit_data()
        plt.rcParams['font.family'] = 'SimHei'#设置中文字体为黑体
        plt.rcParams['axes.unicode_minus'] = False#中文状态下负号正常显示
        profit_data.plot(x='财报日期',y=['净资产收益率','销售净利率','销售毛利率'],kind='barh',title='{}-{}'.format(self.beginning,self.ending),figsize=(40,25))
        plt.show()

    def draw_picture2(self):
        profit_data=self.get_profit_data()
        plt.rcParams['font.family'] = 'SimHei'#设置中文字体为黑体
        plt.rcParams['axes.unicode_minus'] = False#中文状态下负号正常显示
        profit_data.plot('财报日期',['主营营业收入','净利润'],secondary_y=['净利润'],kind='bar',title='{}-{}'.format(self.beginning,self.ending),figsize=(12,4),rot=0)
        plt.show()

    def draw_picture3(self):
        profit_data=self.get_profit_data()
        plt.rcParams['font.family'] = 'SimHei'#设置中文字体为黑体
        plt.rcParams['axes.unicode_minus'] = False#中文状态下负号正常显示
        figure,axes = plt.subplots(2,1,figsize=(12,8),sharex=True)
        ax0 = profit_data.plot('财报日期',['净资产收益率','销售净利率','销售毛利率'],title='{}-{}'.format(self.beginning,self.ending),ax=axes[0])
        ax1 = profit_data.plot('财报日期','主营营业收入',kind='bar',title='{}-{}'.format(self.beginning,self.ending),color='gold',ax=axes[1])
        ax2 = profit_data.plot('财报日期','净利润',secondary_y=True,color='orangered', ax=axes[1],style='--',marker='o',linewidth=2)
        plt.show()

