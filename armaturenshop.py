# -*- coding: utf-8 -*-


from scrapy import Selector
from datetime import datetime
import os
import time
import pandas as pd
import requests
import random
import traceback

path = "/home/master/Ibex/armaturenshop"

date = datetime.now().strftime("%Y-%m-%d")
outpath = path + "/Output/" + date

proxy_list = pd.read_excel(path+"/proxy.xlsx")['proxy'].tolist()

def get_proxy():
    proxy = random.choice(proxy_list)

    http_proxy = "http://{}".format(proxy)
    https_proxy = "https://{}".format(proxy)


    proxyDict = {
                  "http": http_proxy,
                  "https": https_proxy
                }
    return proxyDict

all_product_url = pd.read_excel(path+"finall_armaturenshop_url.xlsx")['Product_url'].tolist()
import csv
with open(path+'/armaturenshop.csv', 'w', newline='',encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Item_no","EAN","Price","Shiping_time","Description","Link","Brand","Article no"])
    for i in range(0,len(all_product_url)):
        retry = 0
        while retry < 10:
            try:
                response = requests.get(all_product_url[i],verify=False,proxies=get_proxy())
                # time.sleep(random.randint(0,2))
                print("Using proxy")
                break
            except:
                traceback.print_exc()
                retry += 1
                print(retry)
            if retry == 10:
                print("from normal request")
                response = requests.get(all_product_url[i], verify=False)
        response = Selector(text=response.text)
        title = response.xpath('//h1[@class="fn product-title"]//text()').extract_first()
        item_no = response.xpath('//span[@itemprop="sku"]//text()').extract_first()
        ean = response.xpath('//span[@itemprop="gtin13"]//text()').extract_first()
        try:
            price = response.xpath('//strong[@class="price text-nowrap"]/span/text()').extract_first().replace('€','')
        except:
            price = "NA"
        try:
            shiping_time = response.xpath('//p[@class="estimated-delivery"]/span/text()').extract_first()
        except:
            shiping_time = "NA"
        try:
            model = response.xpath('//div[@class="shortdesc"]/text()').extract_first().strip()
        except:
            model = "NA"
        try:
            article = response.xpath('//*[@id="AktuellerkArtikel"]/@value').extract_first()
        except:
            article = "NA"
        writer.writerow([title,item_no,ean,price,shiping_time,model,all_product_url[i],all_brands[i],article])




