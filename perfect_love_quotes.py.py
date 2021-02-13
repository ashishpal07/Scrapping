import requests
from bs4 import BeautifulSoup
import pandas as pd

l = []
r = requests.get('https://quote.com/blog/77-perfect-love-quotes/')
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('blockquote',{'class':'pull-quote'}):
    c = link.find('p').text
    l.append(c)

df = pd.DataFrame({'Love Quotes':l})
df.to_excel('77-perfect-love-quotes.xlsx', index=False)




