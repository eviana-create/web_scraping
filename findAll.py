from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.find_all('span', {'class':{'green','red'}})
for name in nameList:
    print(name.get_text())

nameList = bs.find_all(text='the prince')
print(len(nameList))

title = bs.find(id='title')
title = bs.find_all(id='text')
title = bs.find_all('', {'id':'text'})
