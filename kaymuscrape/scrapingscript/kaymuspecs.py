from bs4 import BeautifulSoup
import urllib.request

field_list=['specs','imgurl']
data_list=list()

def re_scrape(href):   
    p2=urllib.request.urlopen("http://www.kaymu.com.np/smartphones/"+ href +"").read()
    make_soup=BeautifulSoup(p2,"html.parser")
    for product_specification in make_soup.find_all("div",{"class":"hr row"}):
            data_list.append(product_specification)
            for pic in make_soup.find_all("div",{"class":"img vh-center zoom"}):
                picture=pic.get("data-zoom")
                data_list.append(picture)

    dictionary=dict(zip(field_list,data_list))
    return dictionary
    

#re_scrape('/samsung-galaxy-j5-293553.html/')
