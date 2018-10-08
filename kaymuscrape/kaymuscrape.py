import urllib.request
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz

url="http://www.kaymu.com.np/smartphones"

htmlfile=urllib.request.urlopen(url)
htmltext=htmlfile.read()
soup=BeautifulSoup(htmltext,'html.parser')

def scrape(a):
    name_list=list()
    reference_list=list()
    for div in soup.findAll('h3',{"class":"ellipsis phm"}):
         result=div.contents[0]
         fratio=fuzz.partial_ratio(a,result)
         if (fratio>90):
             name_list.append(result)
             reference_list.append(1)
         else:
             reference_list.append(0)

    price_list=list()
    k=0
    
    for x in soup.findAll('div',{"class":"full-width pbs"}):
         if reference_list[k]==1:
             result=x.contents[1].contents[0]
             price_list.append(result)
         k=k+1
             
    dictionary=dict(zip(name_list,price_list))
    return dictionary
    
