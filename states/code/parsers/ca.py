"""
Script to extract plain text laws for CA
from URLS
@author soph
"""
import re
import requests
from bs4 import BeautifulSoup as BS 

r = requests.get('http://projects.csail.mit.edu/legalgenome/states_smalldata/ca.bill_urls.txt')
urls = r.text.split()
total = len(urls)

i = 1
for url in urls:
    bill_id = re.findall('.*bill_id=(.*)', url)[0]
    print "SCRAPING", bill_id, str(i), "/", total
    page = requests.get(url)
    soup = BS(page.text)
    all_texts = soup.findAll(text=True)
    body = soup.findAll('div', {'id': 'bill_all'})
    texts = [t.text.strip() for t in body]
    encoded = [t.encode('utf8') for t in texts]        
    
    out_file = open('../../data/ca/' + bill_id + '.txt', 'w')
    for t in encoded:
        out_file.write(t)
    out_file.close()
    i += 1
