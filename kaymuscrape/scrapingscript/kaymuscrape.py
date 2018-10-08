from bs4 import BeautifulSoup
import urllib.request
from fuzzywuzzy import fuzz


url=["http://www.kaymu.com.np/smartphones/?page=1",
    "http://www.kaymu.com.np/smartphones/?page=2",
    "http://www.kaymu.com.np/smartphones/?page=3",
    "http://www.kaymu.com.np/smartphones/?page=4",
    "http://www.kaymu.com.np/smartphones/?page=5",
    ]

htmltext=list()

for x in url:
    htmlfile=urllib.request.urlopen(x)
    htmltext.append(htmlfile.read())

def scrape(value):
    name_list=list()
    price_list=list()
    href_list=list()
    
    for x in htmltext:
        soup=BeautifulSoup(x,"html.parser")
        for product_name in soup.find_all("a",{"class":"card-overlay block pr"}):
            name=product_name.get('data-track-name')
            price=product_name.get('data-track-price_local')
            href=product_name.get('href')
            output=fuzz.partial_ratio(value,name)
            if (output >80):
                
                name_list.append(name)
                price_list.append(price)
                href_list.append(href)

                
    dictionary=dict(zip(name_list,zip(price_list,href_list)))
    return dictionary
