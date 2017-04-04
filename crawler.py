import requests

from bs4 import BeautifulSoup 

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

def main():
	url = 'https://coinmarketcap.com/all/views/all'


	all_links = get_all_links( get_html(url) )
	
	for i in all_links:
		print(i)

if __name__ == '__main__':
	main()