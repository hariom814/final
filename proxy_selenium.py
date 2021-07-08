import os
import zipfile
import pandas as pd
import random

from selenium import webdriver
path = '/Users/hari/Documents/hari/'
proxy_list = ['us-wa.proxymesh.com:31280','jp.proxymesh.com:31280']
# proxy = random.choice(proxy_list)
# proxy = proxy.split(":")[0]

PROXY_HOST = 'zproxy.lum-superproxy.io'  # rotating proxy
PROXY_PORT = 22225
PROXY_USER = 'lum-customer-c_ffcfe734-zone-data_center'
PROXY_PASS = 'mz96ihm38ncv'


manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
          },
          bypassList: ["localhost"]
        }
      };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)


def get_chromedriver(use_proxy=False, user_agent=None):
    path = os.path.dirname(os.path.abspath(__file__))
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        # chrome_options.add_extension(pluginfile)
    if user_agent:
        chrome_options.add_argument('--user-agent=%s' % user_agent)
    driver = webdriver.Chrome(
        os.path.join('/Users/hari/Documents/hari/', 'chromedriver'),
        chrome_options=chrome_options)
    return driver

def main():
    driver = get_chromedriver(use_proxy=True)
    #driver.get('https://www.google.com/search?q=my+ip+address')
    a = ['https://www.browserstack.com/guide/set-proxy-in-selenium']
    for i in a:
        driver.get(i)
        data = driver.find_element_by_xpath('/html/body/div[1]/main/section/article/div[1]/div/div/div[1]/h1').text
        print(data)
        print("hi")

if __name__ == '__main__':
    main()