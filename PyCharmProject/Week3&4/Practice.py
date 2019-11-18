import requests
from bs4 import BeautifulSoup

#############################################
# 추가1

# naverebook.csv 파일을 쓰기(w) 모드로 열어줍니다.
f = open("naverebook.csv", "w")

# 데이터의 헤더 부분을 써줍니다.
f.write("제목,저자\n")
#############################################


for p in range(1, 6):
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(p),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    books = html.select("div.lst_thum_wrap li")
    for b in books:
        title = b.select_one("a strong").text
        author = b.select_one("span.writer").text

        print(title, author)
        #############################################
        # 추가2

        # ,로 데이터가 구분되지 않도록 수집한 제목/저자에서 ,를 삭제해줍니다.
        title = title.replace(",", "")
        author = author.replace(",", "")

        # 수집한 제목/저자를 파일에 써줍니다.
        f.write(title + "," + author + "\n")
        #############################################

#############################################
# 추가3

# naverebook.csv파일을 닫아줍니다.
f.close()
#############################################