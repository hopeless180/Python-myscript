from urllib.parse import quote, unquote
import requests
from lxml import etree
import pandas as pd
import lxml.html as lh

url_ = 'https://wiki.biligame.com/blhx/%E8%88%B0%E8%88%B9%E5%9B%BE%E9%89%B4'

header_ = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Referer': 'https://wiki.biligame.com/'
}

response_ = requests.get(url_, headers=header_)
data_ = response_.content
html_ipg = etree.HTML(data_)
elems_ = html_ipg.xpath('//span[@class="jntj-4"]/a/.')
shipnames = [x.text for x in elems_ if not x.text.count('.改')]
test_shipnames = '新泽西'

url_ship = f'https://wiki.biligame.com/blhx/{test_shipnames}'
response_ship = requests.get(url_ship, headers=header_)
data_ship = response_ship.content
html_ = etree.HTML(data_ship)

elems_ = html_.xpath('//table[contains(@class,"sv-general")]')[0]
general_title = elems_.xpath('./tbody/tr[1]')[0].xpath('string(.)')
general_elems = elems_.xpath('./tbody/tr[position()>1 and not(contains(@style, "display:none;"))]')
general_dict = {}
rowspan = []
for tr in general_elems:
    # print(x.xpath('./td/img'))
    if len(tr.xpath('./td/img')) > 0:
        continue
    tds = tr.xpath('./td')
    key_ = [rowspan.pop()] if rowspan else []
    value_ = []
    for td in tds:
        if td.xpath('./@rowspan'):
            rowspan = rowspan + [td.xpath("string(.)")] * (int(td.xpath('./@rowspan')[0]) - 1)
        if td.xpath('.//b'):
            key_.append(td.xpath('string(.)'))
        elif td.xpath('following-sibling::node()[1] and not(.//b)'):
            general_dict[''.join(key_)] = ''.join(td.xpath('string(.)'))
            key_ = []
        else:
            value_.append(td.xpath('string(.)'))

    general_dict[''.join(key_)] = ''.join(value_)
    # for i in range(0, len(tds), 2): 
    #     general_dict[tds[i].xpath('string(.)')] = tds[i+1].xpath('string(.)')

elems_ = html_.xpath('//table[contains(@class, "sv-category")]')[0]
category_title = elems_.xpath('./tbody/tr[1]')[0].xpath('string(.)')
df = pd.read_html(lh.tostring(elems_), header=0)[0]
category_dict = df.to_dict(orient='split')

elems_ = html_.xpath('//table[contains(@class, "sv-performance")]')[0]
sixattr_title = elems_.xpath('./tbody/tr[1]')[0].xpath('string(.)')
## 这里局限于两列表格，如果原页面修改就只返回空
sixattr_elems = elems_.xpath('.//table/tbody/tr[count(td)=2]')
sixattr_dict = {}
for tr in sixattr_elems:
    td = tr.xpath('./td')
    sixattr_dict[td[0].xpath('string(.)')] = td[1].xpath('string(.)')

elems_ = html_.xpath('//table[contains(@class, "sv-performance")]')[1]
stat_title = elems_.xpath('.//tr[1]')[0].xpath('string(.)')
stat_elems = elems_.xpath('./tbody/tr[position()>1]')
stat_dict = {}
for tr in stat_elems:
    if tr.xpath('.//table'):
        break
    tds = tr.xpath('./td')
    for i in range(0, len(tds), 2):
        td = tds[i]
        if td.xpath('.//b'):
            stat_dict[td.xpath('string(.)')] = tds[i+1].xpath('string(.)')

elems_ = html_.xpath('//table[preceding-sibling::table[contains(@class, "sv-general")] and contains(@class, "sv-breakthrough")]')[0]
LB_title = elems_.xpath('./tbody/tr[1]')[0].xpath('string(.)')
LB_elems = elems_.xpath('./tbody/tr[count(td)=2]')
LB_dict = {}
for tr in LB_elems:
    tds = tr.xpath('./td')
    LB_dict[tds[0].xpath('string(.)')] = tds[1].xpath('string(.)')

elems_ = html_.xpath('//table[preceding-sibling::table[contains(@class, "sv-general")] and contains(@class, "sv-equipment")]')
equip1_title = elems_[0].xpath('./tbody/tr[1]')[0].xpath('string(.)')
equip2_title = elems_[1].xpath('./tbody/tr[1]')[0].xpath('string(.)')
df = pd.read_html(lh.tostring(elems_[0]), header=0)[0]
equip1_dict = df.to_dict(orient='split')
equip2_elems = elems_[1].xpath('./tbody/tr[position()>1 and count(td)=2]')
equip2_dict = {}
for tr in equip2_elems:
    tds = tr.xpath('./td')
    equip2_dict[tds[0].xpath('string(.)')] = tds[1].xpath('string(.)')

elems_ = html_.xpath('//table[preceding-sibling::table[contains(@class, "sv-general")] and contains(@class, "sv-skill")]')[0]
skill_title = elems_.xpath('./tbody/tr[1]')[0].xpath('string(.)')
skill_elems = elems_.xpath('./tbody/tr[position()>1 and count(td)=2 and not(contains(@style, "display:none"))]')
skill_dict = {}
for tr in skill_elems:
    tds = tr.xpath('./td')
    skill_dict[tds[0].xpath('string(.)')] = tds[1].xpath('string(.)')

elems_ = html_.xpath('//*[contains(@class, "jntj-right")]/table[contains(@class, "sv-portrait")]/tbody/tr[./td[contains(@class, "decisive")]]')
portrait_dict = []
for i in range(0, len(elems_)):
    title_ = elems_[i].xpath('string(.)')
    if i == len(elems_) - 1:
        cur_elems = elems_[i].xpath('following-sibling::tr')
    else:
        cur_elems = list(set(elems_[i].xpath('following-sibling::tr')) & set(elems_[i+1].xpath('preceding-sibling::tr')))
    if '立绘' in title_:
        portrait_dict.append({'title': title_, 'elements': cur_elems[0].xpath('.//img/@src')})
    elif '角色信息' in title_:
        dict_ = {}
        for tr in cur_elems:
            tds = tr.xpath('./td')
            dict_[tds[0].xpath('string(.)')] = tds[1].xpath('string(.)')
        portrait_dict.append({'title': title_, 'elements': dict_})
    elif 'CV' in title_:
        portrait_dict.append({'title': title_, 'elements': cur_elems[0].xpath('string(.)')})
    elif '画师' in title_:
        dict_ = {}
        for tr in cur_elems:
            tds = tr.xpath('./td')
            if len(tds) != 2:
                dict_['画师名称'] = tds[0].xpath('string(.)')
            else:
                dict_[tds[0].xpath('string(.)')] = tds[1].xpath('string(.)')
        portrait_dict.append({'title': title_, 'elements': dict_})





