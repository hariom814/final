import time
from random import randint
# import undetected_chromedriver as uc
import pandas as pd
import os
from scrapy import Selector
from urllib.parse import quote
import  csv

path = "E:/My_official _folder/pythonProject/yellowpages_getlead/"
input_data = pd.read_csv(path+'Input_location.csv')
location_data = input_data['Location']
company_data = input_data['Industry']

import requests
base_url = 'https://www.yellowpages.ca'

cookies = {
    '_gcl_au': '1.1.1129655243.1730011168',
    '_gid': 'GA1.2.2043054771.1730011171',
    'yp.ssa': '%7B%22id%22%3A%221730019918025%22%7D',
    'yp.ss': '%7B%22e%22%3Afalse%7D',
    'yp.analytics': '%7B%22id%22%3A%22750491f2-1488-4ae9-bf4e-bc06671d929b%22%2C%22iwa%22%3A%22Demolition+company%22%2C%22iw%22%3A%22Toronto+ON%22%2C%22sc%22%3A198%2C%22si%22%3A%22750491f2-1488-4ae9-bf4e-bc06671d929b_RGVtb2xpdGlvbiBjb21wYW55_VG9yb250byBPTg%22%7D',
    'yp.theme': 'yellowpages',
    'yp.engagement': '%5B%7B%22id%22%3A%22102792663%22%2C%22ts%22%3A1730022345533%7D%2C%7B%22id%22%3A%22102703100%22%2C%22ts%22%3A1730015211062%7D%2C%7B%22id%22%3A%227242109%22%2C%22ts%22%3A1730015021397%7D%5D',
    '_dc_gtm_UA-126563938-4': '1',
    '__gads': 'ID=d5359a593a088bd3:T=1730011171:RT=1730022549:S=ALNI_MZaw1IRCTy1jksnR8bF-kpJxffQ5Q',
    '__gpi': 'UID=00000f567a07aeb4:T=1730011171:RT=1730022549:S=ALNI_MZM7hHSCa21DnHjqtDxzOr8z-iLSw',
    '__eoi': 'ID=9270a4445336b90d:T=1730011171:RT=1730022549:S=AA-AfjYBpnLC_VQLyRAZqRavz9NN',
    'JSESSIONID': 'EDAE195FE84AFF32A3E7780D67310782',
    'yp.campaign': '%7B%22serpCampaign%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1730022561919%7D%2C%22thirdAdMobile%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1730022561919%7D%2C%22fiveResults%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1730022561919%7D%2C%22folSizeRedcue%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1730022561919%7D%2C%22folRulesMobile%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1730022561919%7D%2C%22noneGroupingEnd%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1730022561919%7D%7D',
    'yp.prefs': '%7B%22w%22%3A%22Toronto+ON%22%2C%22loc%22%3A%22Toronto+ON%22%2C%22locla%22%3A43.6485%2C%22loclo%22%3A-79.3853%2C%22po%22%3Atrue%2C%22rws%22%3A%5B%22Toronto+ON%22%5D%2C%22rwtsm%22%3A%7B%22YP%22%3A%5B%22Demolition+company%22%5D%7D%2C%22ts%22%3A1730022562232%7D',
    'yp.survey': '%7B%22page_type%22%3A%22page_type_serp%22%2C%22traffic%22%3A%22traffic_internal%22%2C%22loggedin%22%3A%22loggedin_false%22%2C%22search_type%22%3A%22search_type_si%22%2C%22headings%22%3A%5B%22heading_00411950%22%5D%7D',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sun+Oct+27+2024+15%3A19%3A20+GMT%2B0530+(India+Standard+Time)&version=202308.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=IN%3BBR',
    'OptanonAlertBoxClosed': '2024-10-27T09:49:20.580Z',
    'FCNEC': '%5B%5B%22AKsRol8rB4ilB9_8qYZRYSttWROYfo7B6JybRpAui58kvOR3hteIK2yj6YX4aLaR2DkxwkxvBoENVWvmoVLsKZvp5dt-NyrmRaFtpdG0WP0z07uXxo7mroWl7_zYquJ7MHBo82JB3wOAApcdr1oaV-otlSlAqSbWng%3D%3D%22%5D%5D',
    '_ga': 'GA1.2.1854101301.1730011171',
    '_ga_WC7YVRLFQD': 'GS1.1.1730019883.2.1.1730022579.27.0.0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=5E37E545FCBC6FA97EC4951083909684; _gcl_au=1.1.1129655243.1730011168; _gid=GA1.2.2043054771.1730011171; yp.ssa=%7B%22id%22%3A%221730019918025%22%7D; yp.ss=%7B%22e%22%3Afalse%7D; yp.analytics=%7B%22id%22%3A%22750491f2-1488-4ae9-bf4e-bc06671d929b%22%2C%22iwa%22%3A%22Demolition+company%22%2C%22iw%22%3A%22Toronto+ON%22%2C%22sc%22%3A198%2C%22si%22%3A%22750491f2-1488-4ae9-bf4e-bc06671d929b_RGVtb2xpdGlvbiBjb21wYW55_VG9yb250byBPTg%22%7D; yp.engagement=%5B%7B%22id%22%3A%22102792663%22%2C%22ts%22%3A1730022345533%7D%2C%7B%22id%22%3A%22102703100%22%2C%22ts%22%3A1730015211062%7D%2C%7B%22id%22%3A%227242109%22%2C%22ts%22%3A1730015021397%7D%5D; __gads=ID=d5359a593a088bd3:T=1730011171:RT=1730023248:S=ALNI_MZaw1IRCTy1jksnR8bF-kpJxffQ5Q; __gpi=UID=00000f567a07aeb4:T=1730011171:RT=1730023248:S=ALNI_MZM7hHSCa21DnHjqtDxzOr8z-iLSw; __eoi=ID=9270a4445336b90d:T=1730011171:RT=1730023248:S=AA-AfjYBpnLC_VQLyRAZqRavz9NN; yp.campaign=%7B%22serpCampaign%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1730023298296%7D%2C%22thirdAdMobile%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1730023298296%7D%2C%22fiveResults%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1730023298296%7D%2C%22folSizeRedcue%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1730023298296%7D%2C%22noneGroupingEnd%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1730023298296%7D%7D; yp.prefs=%7B%22w%22%3A%22Toronto%2C+ON%22%2C%22loc%22%3A%22Toronto+ON%22%2C%22locla%22%3A43.6485%2C%22loclo%22%3A-79.3853%2C%22po%22%3Atrue%2C%22rws%22%3A%5B%22Toronto+ON%22%5D%2C%22rwtsm%22%3A%7B%22YP%22%3A%5B%22Demolition+company%22%5D%7D%2C%22ts%22%3A1730023298619%7D; yp.theme=yellowpages; yp.survey=%7B%22page_type%22%3A%22page_type_serp%22%2C%22traffic%22%3A%22traffic_internal%22%2C%22loggedin%22%3A%22loggedin_false%22%2C%22search_type%22%3A%22search_type_si%22%2C%22headings%22%3A%5B%22heading_00411950%22%5D%7D; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Oct+27+2024+15%3A31%3A33+GMT%2B0530+(India+Standard+Time)&version=202308.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=IN%3BBR; OptanonAlertBoxClosed=2024-10-27T10:01:33.321Z; FCNEC=%5B%5B%22AKsRol9ZI4nXEJlCiA_IwjXKPzn9EPIPcOCArm4tC8iXQd7GArm-iCFSMAsw2KpUomk_Iv70G0s2UHlc5SdtTrh7XQbaubMu7E-eqtuIpKbyColXjHpKHbOl3uZ8JNYJHAyzcHiQi3ehoVEhuLpEiBW3ovWRehe1EQ%3D%3D%22%5D%5D; JSESSIONID=2C78E2A4660DE3809A515FF33142626A; _ga=GA1.2.1854101301.1730011171; _dc_gtm_UA-126563938-4=1; _ga_WC7YVRLFQD=GS1.1.1730019883.2.1.1730023348.6.0.0',
    'Referer': 'https://www.yellowpages.ca/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
with open(path+'yellopage_CA_output.csv', 'w', newline='',encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerows(['Company Name','Address','Industry','Phone Number','Website','Company Description','Social Media Facebook','Social Media Instagram','Company','Country'])

    for i in range(0,len(location_data)):
        location = quote(location_data[i])
        for j in range(0,len(company_data)):
            company = quote(company_data[i])
            print(location)
            print(company)
            for page in range(0,10):
                print(page)
                resp = requests.get('https://www.yellowpages.ca/search/si/{}/{}/{}'.format(page,company,location), cookies=cookies, headers=headers)

                response = Selector(text=resp.text)

                url_response = response.xpath('//h3[@class="listing__name jsMapBubbleName"]')
                for u in url_response:
                    url_link = u.xpath('.//a//@href').extract_first()
                    resp_url  = requests.get(base_url + url_link, headers=headers)
                    page_response = Selector(text=resp_url.text)
                    title = ''.join(page_response.xpath('//h1[contains(@class, "merchantInfo-title") and contains(@class, "merchant__title")]//text()').extract())
                    print(title)
                    direction = ', '.join(page_response.xpath('//div[@class="merchant__item merchant__address"]//span/text()').extract())
                    description = ' '.join(page_response.xpath('//article[@itemprop="description"]//text()').extract())
                    industry = ''.join(page_response.xpath('//div[@class="business__details jsParentContainer"]//ul//text()').extract())
                    ph_no = page_response.xpath('//ul[@class="mlr__submenu jsMlrSubMenu"]/li/span/text()').extract_first()
                    website = base_url + url_link
                    social_media = page_response.xpath('//li[@class="mlr__submenu__item mlr__submenu__itemnotprint mlr__submenu__item__social "]/a/@href').extract()
                    if len(social_media) > 0:
                        for social in social_media:
                            if 'facebook' in social:
                                facebook = 'www.facebook.com' + social
                            elif 'instagram' in social:
                                instagram = 'www.instagram.com'+social
                    else:
                        facebook = "NA"
                        instagram = "NA"

                    writer.writerows([title,direction,industry,ph_no,website,description,facebook,instagram,company,location])

                    print("Hi")
                break
            break
        break
print("Hi")