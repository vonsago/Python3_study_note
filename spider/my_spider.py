#! encoding = utf-8
import requests
import codecs
from bs4 import BeautifulSoup

#test website:http://movie.douban.com/top250
D_URL = input("input url:")
print("current website is:",D_URL)

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
}#user-agent,protect spider

def download_page(url):
	data = requests.get(url,headers=HEADERS).content
	return data

def parse_html(html):
	
	soup = BeautifulSoup(html)
	# use BeautifulSoup parse the html,test using soup.preriffy() 
	movie_list_soup = soup.find('ol',attrs={'class':'grid_view'})
	#get list according to css
	movie_name_list=[]
	for movie_li  in movie_list_soup.find_all('li'):
		detail = movie_li.find('div',attrs={'class':'hd'})

		movie_name=detail.find('span',attrs={'class':'title'}).getText()
		#movie name
		movie_name_list.append(movie_name)
		#append the name to list
	next_page = soup.find('span',attrs={'class':'next'}).find('a')
	#find next page
	if next_page:
		return movie_name_list,D_URL+next_page['href']
		#make up url of next page
	return movie_name_list,None
	#return list of the movie name
def main():
	url = D_URL
	with codecs.open('movies','wb',encoding='utf-8') as fp:
		#open file in utf-8 code
		while url:
			html = download_page(url)
			#get web
			movies,url=parse_html(html)
			#get web data
			fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))

if __name__=='__main__':
	main()