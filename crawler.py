import requests
import csv

from bs4 import BeautifulSoup 

from datetime import datetime

def get_html(url):
	response = requests.get(url)
	return response.text

def get_all_links(html):
	soup = BeautifulSoup(html, 'lxml')

	table_data_list = soup.find('table', id='currencies-all').find_all('td', class_='currency-name')

	links = []

	for td in table_data_list:
		a = td.find('a').get('href') 													# string type
		link = 'https://coinmarketcap.com{0}'.format(a)			# /currencies/bitcoin/
		links.append(link)

	return links 

def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')

	try:
		name = soup.find('h1', class_='text-large').text.strip()

	except:
		name = ''

	try:
		price = soup.find('span', id='quote_price').text.strip()
	except:
		price = ''

	data = {'name' : name,
					'price' : price}

	return data

def write_csv(data):
	with open('coinmarketcap.csv', 'a') as f:
		writer = csv.writer(f)

		writer.writerow( (data['name'],
											data['price']) )
		print(data['name'], 'parsed')



def main():
	
	#---------------------
	start = datetime.now()
	#---------------------
	url = 'https://coinmarketcap.com/all/views/all'

	all_links = get_all_links( get_html(url) )

	for index, url in enumerate(all_links):
		html = get_html(url)
		data = get_page_data(html)
		write_csv(data)
		print(index)

	#---------------------
	end = datetime.now()

	total = end - start
	#---------------------
	print(str(total))

if __name__ == '__main__':
	main()