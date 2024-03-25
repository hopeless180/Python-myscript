import os
import re

my_test_path =  r"e:\红字本"
files = os.listdir(my_test_path)
authors = []

for file in files:
    author = re.findall(r'^\[(.+?)\(.+?\)\]', file)
    if type(author) == list and len(author) > 0:
        author = author[0]
    if author and not author in authors:
        print(author)
        authors.append(author)

with open(r'e:\作者.txt', 'w+', encoding='utf-8') as f:
    for author in authors:
        f.write(f'{author}\n')