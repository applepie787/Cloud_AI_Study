from bs4 import BeautifulSoup
from urllib import request

# *** Terminology ***
# Event : 사건
# Event Source : Event 발생 원인
# Event Hendler : Event 처리
# --> Event 처리 
#               1. Event 선택
#               2. Event Hendler 구현
#               3. Event Source에 Event Hendler 등록 


# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <h1> 1-Hello External Module 수프 </h1>
# <h1> 2-Hello External Module 수프 </h1>
# <h1> 3-Hello External Module 수프 </h1>
# <h1> 4-Hello External Module 수프 </h1>

# <p class="title"><b>The Dormouse's story</b></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>

# </body>
# </html>
# """


# soup = BeautifulSoup(html_doc, 'html.parser') # Beautifulsoup 객체 생성

# # print(soup.prettify())
# print(soup.find_all('h1'))


html_doc = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
soup = BeautifulSoup(html_doc, 'html.parser') # Beautifulsoup 객체 생성

for location in soup.select("location"):

    #내부의 city, wf, tmn, tmx 태그를 찾아 출력합니다.
    print("도시 : ", location.select_one("city").string)
    print("날씨 : ", location.select_one("wf").string)
    print("최저기온 : ", location.select_one("tmn").string)
    print("최고기온 : ", location.select_one("tmx").string)
    print()