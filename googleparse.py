# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:47:03 2017

@author: nitheesh
"""

from bs4 import BeautifulSoup
import urllib, urllib2

def google_scrape(query):
	address = "http://www.google.com/search?q=%s&num=5&hl=en&start=0" % (urllib.quote_plus(query))
	request = urllib2.Request(address, None, {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
	#proxy_handler = urllib2.ProxyHandler({})
	#opener = urllib2.build_opener(proxy_handler)	
	#urllib2.install_opener(opener)
	urlfile = urllib2.urlopen(request)
	page = urlfile.read()
	soup = BeautifulSoup(page)

	linkdictionary = {}

	for div in soup.findAll('div', attrs={'class':'g'}):
		sLink = div.find('a')
		#print sLink['href']
		sSpan = div.find('span', attrs={'class':'st'})
		if sSpan is not None:
			#[em.replaceWithChildren() for em in sSpan.findAll('em')]
			linkdictionary[sLink['href']] = sSpan.text
			#print sSpan.text
			
	return linkdictionary

if __name__ == '__main__':
	links = google_scrape('beautifulsoup')
	print links
