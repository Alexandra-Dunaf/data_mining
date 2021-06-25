from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

main_link = 'https://gb.ru/'
response = requests.get(f'{main_link}posts/').text
soup = bs(response, 'lxml')

posts = soup.find_all('div',{'class':'post-items-wrapper'})

posts_list = []
for post in posts:
    post_data = {}
    main_data = post.find_all('a',{'class':'post-item__title h3 search_text'})
    name_post = main_data.find_all('href')
    print(name_post)
    break

