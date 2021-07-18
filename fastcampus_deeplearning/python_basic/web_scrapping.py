#web scrapping 단계
#1.scraping - 데이터 가져오기
#2.parsing - 데이터 구분
#3.manipulation - 데이터 가공

#web scrapping 도구
#1.Beautiful Soup
#2.Url lib
#3.Requests

#먼저 스크래핑하고자 하는 웹페이지에 접속
#들어가서 오른쪽 클릭 후 페이지 소스보기

#1. Scrapping
import requests
#원하는 url을 가져다 쓰면 됨
url = "https://www.kric.go.kr/jsp/industry/rss/operatingReportList.jsp?q_fdate=2021"

html_text = requests.get(url).text
#이렇게 하면 페이지소스 내용들이 다 날라온다

#2. Parsing
from bs4 import BeautifulSoup

#html tag를 기준으로 하나하나 parsing
soup = BeautifulSoup(html_text, "html.parser")


#3. Manipulation

#갖고와야할 테이블 찾아오기
tab = soup.find("table",{"class":"listtbl_c100"})

#우리가 필요한건 <thead>쪽이 아닌 <tbody>의 내용들을 리스트 형식으로 가져옴
trs = tab.find("tbody").find_all("tr")
#원하는 내용은 리스트형식으로 되어 있기때문에 리스트 원소를 뽑아내면됨
#print(trs[1])

#특정 coloumn내용인 을 갖고 오고 싶다면 coloumn의 이름인 tdcol을 이용
tdcols = trs[1].find("td",{"class":"tdcol"})
#여기서 .find()를 하면 위에 한가지만 갖고온다. 다 갖고 올려면 find_all()사용
tds = trs[1].find_all("td")
#print(tds[0])
#여기서 text만 가지고 오고 싶으면 .text를 하면됨
#print(tds[0].text)==>국가철도공단 나옴

#여러 역들에 대해서 하고싶을때
stationpassengers = []
for tr in trs[1:]:
    dic = {}
    tds = tr.find_all("td")
    dic['station'] = tds[0].text
    dic['2021'] = tds[1].text
    dic['2020'] = tds[2].text
    stationpassengers.append(dic)
print(stationpassengers)


