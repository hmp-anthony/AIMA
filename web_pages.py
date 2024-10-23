import requests
from bs4 import BeautifulSoup
  
url = 'http://CNN.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
print(soup.find('title').text)
