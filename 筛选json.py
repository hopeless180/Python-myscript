import json
import os
import chardet
from datetime import datetime

path = r"C:\Users\neun\Downloads"
# latestFile = ""
# latestTime = 0
# for file in os.listdir(path):
#     __path = os.path.join(path, file)
#     __ctime = int(os.path.getctime(__path))
#     if file.endswith(".json") and __ctime > latestTime:
#         latestTime = __ctime
#         latestFile = __path

files = [os.path.join(path, file) for file in os.listdir(path) if file.endswith('.json')]
latestFile = sorted(files, key=os.path.getctime, reverse=True)[0]

# 读取json文件
with open(latestFile, 'r', encoding="utf8") as f:
    data = json.load(f)

substring = ['新刊', '販売', '進捗', '宣伝', '公開', '会場', 'FANBOX', '例大祭', '新作', 'ログ', '合同', '告知', 'FANZA', 'DLsite']
tag = ['創作BL','女装', 'ケモノ', '男の娘', '女装少年', 'メス堕ち', '僕のヒーローアカデミア', '3D' , 'ハニーセレクト2' ,'HoneySelect2', 'クレヨンしんちゃん', 'コイカツ', "去衣", "剥ぎコラ"]
# 'ロリ'
user = ['12358712', '3729705', '73816870', '2216866', '1678057', '3324210', '99019', '711526']
user.extend(['374466', '182552', '45253485'])


data = [x for x in data if not any(item in x['title'] for item in substring)]
data = [x for x in data if not any(item in x['tags'] for item in tag)]
data = [x for x in data if not any(item in x['userId'] for item in user)]
data = [x for x in data if int(datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S%z").timestamp()) > 1599264000]
# data = [x for x in data if x['likeCount'] > 3000]
# over5 = list(filter(lambda x: x['pageCount'] > 6, data))
# data = list(filter(lambda x: x['pageCount'] <=5, data))
print(len(data))
# print(len(over5))
# 将修改后的数据写回到文件中
with open(latestFile, 'w') as f:
    json.dump(data, f)
# if over5:
#     with open(os.path.join(os.path.dirname(latestFile), 'lastestJsonOver5.json'), 'w+') as f:
#         json.dump(over5, f)