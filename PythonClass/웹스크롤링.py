'''

웹스크롤링 : beautiful soup 모듈
           - html 문서에 특정 데이터를 검색하는데 사용하는 파이썬 모

* html(Hyper Text Markup Language, 여러개의 태그를 연결해서 모은 문서)의 구조
 
- html 태그 표 참조

'''

# from bs4 import BeautifulSoup
# with open("d:/data/aa.html") as aa:
#     soup = BeautifulSoup(aa, "lxml")     # Beautifulsoup 클래스의 매개변수
# # print('1---------------------------------------------------------------------------------------------------------------------------')
# # print(soup.p)   # p 입력 부분 출력
# # print('2---------------------------------------------------------------------------------------------------------------------------')
# # print(soup.find('p'))   # p 태그 부분 출력(기능은 위랑 동일하나 이쪽을 사용. p 구문이 한군데만 있는게 아니므로 p 있는 부분을 다 가져오기 위해 사용)
# # print('3---------------------------------------------------------------------------------------------------------------------------')
# # print(soup.find_all('p'))   # p 태그 전체를 가져옴
# # print('4---------------------------------------------------------------------------------------------------------------------------')
# # print(soup.find('a'))
# # print('5---------------------------------------------------------------------------------------------------------------------------')
# # print(soup.find_all('a'))   # a 태그 전체를 가져옴 -> a 태그는 url 주소를 담고 있기 때문에 크롤링에서 매우 중요한 부분이다.
# # print('6---------------------------------------------------------------------------------------------------------------------------')
# # for soup in soup.find_all('a'):
# #     print(soup.get('href'))
# print('7---------------------------------------------------------------------------------------------------------------------------')
# for link in soup.find_all('a'):
#     print(link.get('href'))
#     print(link)


import urllib.request
from bs4 import BeautifulSoup
import re
import os


def fetch_list_url():
    list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
    url = urllib.request.Request(list_url)
    res = urllib.request.urlopen(url).read().decode("utf-8")
    soup_packtpage = BeautifulSoup(res, "html.parser")
    # 위의 ebs 게시판 url 로 접속했을때 담긴 html 코드를
    # soup_packpage 에 담겠다
    e_reg = re.compile("(완젼)")
    a = soup_packtpage.find(text=e_reg)
    print(a)


fetch_list_url()




import urllib.request
from bs4 import BeautifulSoup
import re
import os

def fetch_list_url(z):
    z = str(z)
    # print('page', z)
    list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page="+z+"&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&"
    url = urllib.request.Request(list_url)
    res = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(res, "html.parser")
    a = soup.find_all('p', class_='con')
    # b = soup.find_all('span',class_="date")
    # print(a)
    # print(b)
    for i in a:
        print(i.get_text(strip=True))


for i in range(1,16,1):
    fetch_list_url(i)

