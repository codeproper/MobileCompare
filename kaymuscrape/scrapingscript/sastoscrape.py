import urllib.request
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz



url=["http://www.sastodeal.com/category/mobiles/?page=1",
     "http://www.sastodeal.com/category/mobiles/?page=2",
     "http://www.sastodeal.com/category/mobiles/?page=3",
     "http://www.sastodeal.com/category/mobiles/?page=4"
     ]
htmltext=list()
for x in url:
    htmlfile=urllib.request.urlopen(x)
    htmltext.append(htmlfile.read())


    
def scrape2(value):
        count=0
        name_list=list()
        price_list=list()
        imglink_list=list()
        href_list=list()
        reference_list=list()
        k=0
        r=0
        v=0
        
        for x in htmltext:
                 soup=BeautifulSoup(x,'html.parser')
                 for product_box in soup.find_all("div",{"class":"pure-u-1-3 product_box item_box size-hover"}):
                        for name in product_box.findAll("div",{"class":"one_product_title"}):
                                product_name=name.text
                                actual_name=product_name.split()
                                comp_value=fuzz.partial_ratio(actual_name,value)
                                if (comp_value>70):
                                    name_list.append(" ".join(actual_name))
                                    reference_list.append(1)
                                else:
                                    reference_list.append(0)

                    

                        
                        for price in product_box.find_all('div',{"class":"one_product_price"}):
                                product_price= price.text
                                if (reference_list[k]==1):
                                    q=price_list.append(" ".join(product_price.split()))

                                k=k+1

                                                      
                        for link in product_box.find_all("img"):
                                ilink=link.get('src')
                                if (reference_list[r]==1):
                                    imglink_list.append(" ".join(ilink.split()))
                                r+=1
              
                        
                        for href_link in product_box.find_all("a"):
                                p=href_link.get('href')
                                if (reference_list[v]==1):
                                    href_list.append(" ".join(p.split()))
                                v+=1
              
        k=zip(price_list,imglink_list,href_list)
        dictionary=dict(zip(name_list,k))
        return dictionary
    

    
