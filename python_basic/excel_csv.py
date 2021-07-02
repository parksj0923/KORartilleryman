#파이썬 외부 파일 처리
#파이썬 Excel, CSV 파일 읽기 및 쓰기
#CSV : MIME = text/csv==> text나 csv는 둘다 csv

#ex1
import csv
with open('./resource/sample1.csv','r',encoding='CP949') as f:
    reader = csv.reader(f)
    
    #첫번째줄 Header줄 없얘기
    next(reader)
    #확인
    #print(reader)# <_csv.reader object at 0x7fc46ad952d0>
   # print(type(reader)) # <class '_csv.reader'>
    #print(dir(reader)) #dir을 통해서 해당 클래스에 어떤 메소드가 있는지 확인할 수 있음
    '''['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__
', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__i
ter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__redu
ce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
'dialect', 'line_num']'''
    #이때 __iter_라는 메소드가 있으면 반복문 사용가능
    for c in reader:
        print(c)

#ex2
import csv
with open('./resource/sample2.csv','r',encoding='CP949') as f:
    reader = csv.reader(f, delimiter='|') #|구분을 없얘주는 옵션 delimiter
    
    #첫번째줄 Header줄 없얘기
    next(reader)

    for c in reader:
        print(c)


#ex3 (Dict 변환) 키-벨류인 딕셔너리로 바꿔주기 때문에 편하게 사용이 가능함
with open('./resource/sample1.csv','r',encoding='CP949') as f:
    reader = csv.DictReader(f)
    
    for c in reader:
        for k, v in c.items(): # .items()는 키와 벨류값을 다 가져오는 메소드
            print(k,v)
        print('----------------------------')




#ex4 # csv 파일 만들기
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('./resource/sample3.csv','w',newline='') as f: #줄 띄움 안하기
    wt = csv.writer(f)
    
    for v in w:
        wt.writerow(v)
        
        

#ex5 
with open('./resource/sample4.csv','w',newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)# for 문 안돌리고 한번에 쓰기


print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
print('----------------------------------------------------------------------')


#XSL, XLSX
#openpyxl, xlswriter, xlrd, xlwt, xlutils
# pandas를 주로 사용(openpysl,xlrd를 내부에서 사용)
# pip install xlrd
# pip install openpyxl
# pip isntall pandas

import pandas as pd

#옵션을 넣어줄 수 있음 sheetname='시트명'(엑셀내에 원하는시트가져올수있음),또는 숫자, header=숫자, skiprow= 숫자
#ex xlsx = pd.read_excel('./resource/sample.xlsx', sheetname='dfljd')
xlsx = pd.read_excel('./resource/sample.xlsx')

#상위 데이터 확인-상위 5개만 확인
print(xlsx.head())
print('')

#꼬리 데이터 확인-하위 5개 확인
print(xlsx.tail())

#데이터 확인
print(xlsx.shape) #행,열

#엑셀 or csv 변환해서 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index =False)
xlsx.to_csv('./resource/result.csv', index =False)








