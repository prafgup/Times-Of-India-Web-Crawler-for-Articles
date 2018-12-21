import requests
from bs4 import BeautifulSoup
import os
import datetime


def scrappy(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.find('title').text.split('|')[0]
        time =soup.find('span', attrs={'class':'time_cptn'}).find_all('span')[2].contents[0]
        full_text =soup.find('div', attrs={'class':'article_content'}).text.replace('Download The Times of India News App for Latest India News','')
    except:
        return ('','','','')
    else:
        return (title,time,url,full_text)

def pathmaker(name):   
    path = "/home/hackit/Desktop/Web_Crawler/CRAWLED_DATA/{}".format(name)

    try:  
        os.makedirs(path)
    except OSError:  
        pass
    else:  
        pass


folders_links=[('India','https://timesofindia.indiatimes.com/india'),('World','https://timesofindia.indiatimes.com/world'),('Business','https://timesofindia.indiatimes.com/business')]

for x,y in folders_links:
	pathmaker(x)
	r = requests.get(y)
	soup = BeautifulSoup(r.text, 'html.parser')
	links =soup.find('div', attrs={'class':'main-content'}).find_all('span', attrs={'class':'twtr'})
	links_all=['https://timesofindia.indiatimes.com'+links[x]['data-url'].split('?')[0] for x in range(len(links))]
	k=1

	for link in links_all:
		scrapped=scrappy(link)
		
		textfile=open('/home/hackit/Desktop/Web_Crawler/CRAWLED_DATA/{}/text{}.txt'.format(x,k),'w')
		k+=1
		textfile.write('Title\n{}\n\nLink\n{}\n\nDate & Time\n{}\n\nText\n{}'.format(scrapped[0],scrapped[2],scrapped[1],scrapped[3]))
		textfile.close()
