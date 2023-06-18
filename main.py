from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.thenationalnews.com/travel/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.prettify()
    data = {'content': content}
    json_data = json.dumps(data)
    with open('data.json', 'w') as json_file:
        json_file.write(json_data)
with open('data.json', 'r') as json_file:
    json_data = json.load(json_file)
content = json_data['content']
soup = BeautifulSoup(content, 'html.parser')
publications_count = len(soup.find_all('div', class_='container layout-section section -front-layout'))
print("Количество публикаций на странице:", publications_count)
title = soup.title.string.strip()
print(title)
element = soup.find_all('p')
print(element)
