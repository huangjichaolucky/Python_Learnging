#-*- coding=utf-8 -*-
#爬取妹子图

import urllib.request
import os
from bs4 import BeautifulSoup

def getUrlData():
	url = 'http://jandan.net/ooxx/page-138#comments'

	req = urllib.request.Request(url)
	html = urllib.request.urlopen(req)
	result = html.read().decode('utf-8')
	# print (result)
	return result

if __name__ == '__main__':
	getUrlData()