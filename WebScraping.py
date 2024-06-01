from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
# import time

pageNos = ["1", "2", "3", "4", "5", "6", "7", "8"]
for pageNo in pageNos:
    #  r = urlopen('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts').read()
    r = urlopen('http://www.irobotec.com/shop/page/'+pageNo).read()
    soup = BeautifulSoup(r, "html.parser")
    products = soup.findAll("li", re.compile("^post"))
    print('Page No {} .'.format(pageNo))
    # print(products[0].a.h2)
    print(len(products))
    #  findAll returns a set (even if the return is one item). "find" returns a one result
    for product in products:
        title = product.a.h2.text
        # .findALL("h2", {"class": "woocommerce-loop-product__title"})
        price = product.findAll("span", {"class": "woocommerce-Price-amount amount"})
        print(title)
        if len(price) != 0:
            print(price[0].text)
        else:
            print("Read More")
    # time.sleep(5)
