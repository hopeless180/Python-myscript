import shutil
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

PROXY = "localhost:7890"
cookies_ =[
{
    "domain": ".exhentai.org",
    "expirationDate": 1720655305.508556,
    "hostOnly": False,
    "httpOnly": False,
    "name": "igneous",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "ba4be986b",
    "id": 1
},
{
    "domain": ".exhentai.org",
    "expirationDate": 1720655305.12921,
    "hostOnly": False,
    "httpOnly": False,
    "name": "ipb_member_id",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1788404",
    "id": 2
},
{
    "domain": ".exhentai.org",
    "expirationDate": 1720655305.12924,
    "hostOnly": False,
    "httpOnly": False,
    "name": "ipb_pass_hash",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "21e4f7ba30f6f8b00d4b2dc96549514f",
    "id": 3
},
{
    "domain": ".exhentai.org",
    "expirationDate": 1689162505.12925,
    "hostOnly": False,
    "httpOnly": False,
    "name": "yay",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "louder",
    "id": 4
}
]

def browser_init():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    browser  = webdriver.Chrome(options = chrome_options)
    return browser
    pass

if __name__ == '__main__':
    browser = browser_init()
    browser.get('https://exhentai.org')
    for cookie in cookies_:
        browser.add_cookie(cookie)
    browser.refresh()
    pass
