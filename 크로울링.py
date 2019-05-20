from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

html = "http://battlelog.battlefield.com/bf4/ko/soldier/Sharqia/stats/1042896933/pc/"

req = Request(html, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# HTML 분석하기 --- (※1)
soup = BeautifulSoup(webpage, 'html.parser')
emblem = soup.find_all("div",{"class":"emblem-image"})
print(i.find('img')['src']for i in emblem)
# find() 메서드로 원하는 부분 추출하기 --- (※2)
#title = soup.find(id="title")
#body  = soup.find(id="body")

# 텍스트 부분 출력하기
#print("#title=" + title.string)
#print("#body="  + body.string)
