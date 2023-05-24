import sys
sys.path.append("D:/Code/final_work/Data_analyzing/")
import draw_functions as df

def stock_list_making():
    codelist=[]
    with open('D:/Code/final_work/Webcrawler/file.csv','r',encoding='utf-8')as f:
        while True:
            table=f.readline().split(',')
            if len(table)<2:
                break
            codelist.append((str(table[0]),table[1]))
    return codelist

def get_exchange(code):
    if code.startswith("600") or code.startswith("601") or code.startswith("603") or code.startswith("605"):
        return "sh."
    elif code.startswith("000") or code.startswith("002") or code.startswith("300") or code.startswith("301"):
        return "sz."
    else:
        return ""
        
def main():      
    stocklist=stock_list_making()
    num=int(input("请输入股票序号：\n"))
    stock=stocklist[num][0]
    name=stocklist[num][1]
    codes=get_exchange(code=stock)+stock
    print(codes,name)
    me=df.DrawFunctions(code=codes,beginning=str(2017),ending=str(2022))
    i=5
    while i!=0:
        i=int(input('请输入图表类型：1.条形图，2.柱状图，3.折线图,0.退出\n'))
        if i==1:
            me.draw_picture1()
        elif i==2:
            me.draw_picture2()
        elif i==3:
            me.draw_picture3()
        elif i==0:
            break

if __name__=='__main__':
    main()

