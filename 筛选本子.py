import os
import re
import shutil

input_path = r'e:/红字本'
dictionary = {}
books = {}
books2 = {}
# res = {}

for folder in os.listdir(input_path):
    match = re.findall(r'(?:(?:\([^\(\)]+\))|(?:\[[^\[\]]+\]))*([^\[\(\)\]]+)(?:(?:\([^\(\)]+\))|(?:\[[^\[\]]+\]))*', folder)
    if not match:
        continue
    match = [x.lstrip().rstrip() for x in match]
    title = [x for x in match if x]
    if not title:
        continue
    else:
        title = title[0]
    tags = re.findall(r'\(([^\(\)]+)\)', folder)
    tags += re.findall(r'\[([^\[\]]+)\]', folder)
    if not title in dictionary and any('中国翻訳' in x or 'chinese' in x or '汉化' in x for x in tags):
        dictionary[title] = "!@#".join(tags)
        books[title] = os.path.join(input_path, folder)
    elif title in dictionary:
        set_a = set(tags)
        set_b = set(dictionary[title].split('!@#'))
        shutil.move(os.path.join(input_path, folder), "e:/test")
        books2[title] = books[title]
        # res[title] = ''.join(list(set_a-set_b) + list(set_b-set_a))

for i in books2.values():
    shutil.move(i, 'e:/test')
# with open('e:/翻译.txt', 'w+', encoding='utf-8') as f:
#     for k, v in res.items():
#         f.write(f'{k}\n\t\t{v}\n')

