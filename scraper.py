# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

#import unicodedata
import urllib3
#from lxml.html import fromstring, tostring
#import lxml.html
from bs4 import BeautifulSoup

for i in range(1842, 1847):
    ngo_index = i
    ngo_url = "http://npo.moi.gov.tw/npom/homepage/detail/26888" + str(ngo_index)
    http = urllib3.PoolManager()
    r = http.request('GET', ngo_url)
    root = BeautifulSoup(r.data, 'html.parser')
    ngo_table = root.find('table')
    for j in ngo_table.find_all('tr'):
        print(j.find_all('td')[1].string.strip())
    print('-------------------------------------------------')
    
