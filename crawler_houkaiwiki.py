from urllib.parse import quote, unquote
import requests
from lxml import etree
import pandas as pd
import lxml.html as lh
import webbrowser
import json

url_ = 'https://api-static.mihoyo.com/common/blackboard/sr_wiki/v1/home/content/list?app_sn=sr_wiki&channel_id=17'

header_ = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Referer': 'https://bbs.mihoyo.com/'
}

response_ = requests.get(url_, headers=header_)
data_ = response_.content
data_ = json.loads(data_)
print(data_)
pass
