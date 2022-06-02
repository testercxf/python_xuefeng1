import  requests
from bs4 import BeautifulSoup

url =  'http://www.ip33.com/area_code.html'
res = requests.get(url)
res.encoding = 'utf-8'

bs = BeautifulSoup(res.text,"html.parser")
# print(bs.find_all('class=ip'))
for i in bs.find_all(class_='ip'):
    print(i.text)