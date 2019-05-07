import requests as re
from bs4 import BeautifulSoup as bs

def main():
	url = "http://time.com/"
	a = re.get(url)
	soup = bs(a.content, 'lxml')
	class1 = "column text-align-left visible-desktop visible-mobile last-column"
	class2 = "column-tout "
	class3 = "headline heading-3 heading-content margin-8-bottom media-heading"
	
	lst = soup.find("div", class_=class1).find_all("div", class_=class2)
	
	data = {}
	for i in lst:
		temp = i.find('div', class_=class3)
		data[temp.text.strip()] = temp.find('a')['href']
	print(data)
	

if __name__=='__main__':
	main()
