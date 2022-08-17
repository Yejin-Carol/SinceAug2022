import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://USER:PASSWORD@cluster0.irsirur.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20220816',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    a = movie.select_one('td.title > div > a')
    if a is not None: #가로줄 처리
        title = a.text
        rank = movie.select_one('td.ac > img')['alt']
        star = movie.select_one('td.point').text
        # print(rank, title, star)
        doc = {
            'title':title,
            'rank':rank,
            'star':star
        }
        db.movies.insert_one(doc)
