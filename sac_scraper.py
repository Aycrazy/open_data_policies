import bs4
import urllib
import urllib3
#import urllib2
import re
import pandas as pd

'''
url_west_sac = 'https://westsacramento.demo.socrata.com/browse'
pattern_west = r'.+(?=/browse)'
url_pre = re.findall(pattern_west,url_west_sac)[0]

soup = bs4.BeautifulSoup(urllib2.urlopen(url_west_sac).read(),'html.parser')

all_results = [url_pre+x['href'] for x in soup.find_all('a','pageLink') if x['href']]

west_sac = [[x['href'] for x in bs4.BeautifulSoup(urllib2.urlopen(results).read(),'html.parser').find_all('a','browse2-result-name-link') if x['href']] for results in all_results]


#------------------------------------------Evanston--------------------------------------------------------------

url_evanston = 'https://data.cityofevanston.org/browse'
pattern_ev = r'.+(?=/browse)'
url_pre = re.findall(pattern_ev, url_evanston)[0]

soup = bs4.BeautifulSoup(urllib2.urlopen(url_evanston).read(),'html.parser')

all_results = [url_pre+x['href'] for x in soup.find_all('a','pageLink') if x['href']]

ev_data = [[x['href'] for x in bs4.BeautifulSoup(urllib2.urlopen(results).read(),'html.parser').find_all('a','browse2-result-name-link') if x['href']] for results in all_results]
'''

def scrape_datasets(main_url):
	pattern_ev = r'.+(?=/browse)'
	url_pre = re.findall(pattern_ev, main_url)[0]

	pm = urllib3.PoolManager()
	def make_html(pm,url):
		return pm.urlopen(url= url, method="GET").data

	soup = bs4.BeautifulSoup(make_html(pm,main_url),'html.parser')

	all_results = [url_pre+x['href'] for x in soup.find_all('a','pageLink') if x['href']]

	return [[x['href'].strip(url_pre) for x in bs4.BeautifulSoup(make_html(pm,results),'html.parser').find_all('a','browse2-result-name-link') if x['href']] for results in all_results]

