import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#순위 / 곡 제목 / 가수
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    rank = song.select_one('td.number').text[0:2]
    for span_tag in song.findAll('span'):
        span_tag.replace_with('')
    title = song.select_one('td.info > a.title.ellipsis').text
    singer = song.select_one('td.info > a.artist.ellipsis').text
    print(rank.strip(),'.', title.strip(), '-', singer)