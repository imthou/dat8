import requests
from bs4 import BeautifulSoup


YELP_URL = 'http://www.yelp.com/biz/wills-jamaican-cuisine-inglewood?hrid=lFvP6CD1LgMYInElXwpsEQ'
GOOGLE_URL = 'https://news.google.com'

r = requests.get(YELP_URL)
bs = BeautifulSoup(r.text)

name = bs.select('h1.biz-page-title')[0].text.strip()
address = bs.select('address')[0].text.strip()
reviews = [review.text for review in bs.select('p[itemprop="description"]')]

rating_tags = bs.select('meta[itemprop="ratingValue"]')
ratings = [float(tag.attrs['content']) for tag in rating_tags]

hours_open_today = bs.select('span.hour-range')[0].get_text()

biz_info_tags = bs.select('div.short-def-list > dl')

biz_info = {}
for tag in biz_info_tags:
	key = tag.select('dt')[0].text.strip()
	value = tag.select('dd')[0].text.strip()
	biz_info[key] = value


print('Business Name: ', name)
print('Address: ', address)
print('Reviews (list): ', reviews)
print('Ratings (list): ', ratings)
print('Hours open today: ', hours_open_today)
print('Business info (dictionary): ', biz_info)