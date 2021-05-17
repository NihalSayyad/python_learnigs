import requests

from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

response = requests.get(url)
status = response.status_code
content = response.content
soup = BeautifulSoup(content, 'html.parser')

a = soup.find(id="bodyContent")
table = soup.find_all('table', {'class':'wikitable'})
#print(table[0])
for tr in table[0].find_all('tr'):
    for td in tr.find_all('td'):
        b = td.find('b')
        if b is None:
            continue
        a = b.find('a')
        print(a.text)








