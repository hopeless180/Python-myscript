from mysql import connector
from pymongo import MongoClient
import os
import mutagen
import hashlib

input_path = "e:\\红字本"

def sqlModel():
    print("正在连接数据库")
    con = connector.connect(user='root', password = '19930405' , database = 'erobooks')
    cur = con.cursor()

    subfolders = os.listdir(input_path)
    for folder in subfolders:
        book_path = os.path.join(input_path, folder)
        if not os.path.isdir(book_path) or not book_path:
            continue
        image_count = len(os.listdir(book_path))
        cur.execute('insert into erobooks (book_path,image_count,book_name) values(%s,%s,%s)', (book_path, image_count,folder))
    try:
        con.commit()
    except:
        con.rollback()
    cur.close()
    con.close()

def nosqlModel():
    print("正在连接非关系数据库")
    CONNECTION_STRING = "mongodb://localhost:27017/erobooks"
    client = MongoClient(CONNECTION_STRING)
    current_collection = client['erobooks']['erobooks']
    subfolders = os.listdir(input_path)
    for folder in subfolders:
        book_path = os.path.join(input_path, folder)
        image_name_list = ""
        if not os.path.isdir(book_path) or not book_path:
            continue
        files = os.listdir(book_path)
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".webp"):
                image_name_list += "|" + file if image_name_list else file
        item = {
            "book_name" : folder,
            "book_path" : book_path,
            "image_name_list" : image_name_list
        }
        current_collection.insert_one(item)

def insertvideo(path):
    con = connector.connect(user='root', password = '19930405' , database = 'erovideos')
    cur = con.cursor()

    for (root, dirs, files) in os.walk(path):
        for file in files:
            cur_video_path = os.path.join(root, file)
            if not mutagen.File(cur_video_path):continue
            cur_video_name = os.path.splitext(file)[0]
            hash_id = getHashId(cur_video_path)
            cur.execute('update erovideos set hash_id = %s where path = %s', (hash_id, cur_video_path))
            # cur.execute('insert into erovideos (path,name) values(%s,%s)', (cur_video_path, cur_video_name))
        try:
            con.commit()
        except:
            con.rollback()
    cur.close()
    con.close()

def refreshDatabase(path):
    con = connector.connect(user='root', password = '19930405' , database = 'erovideos', charset = 'utf8mb4', collation = "utf8mb4_general_ci")
    con.set_charset_collation('utf8mb4', 'utf8mb4_general_ci')
    cur = con.cursor()

    for (root, dirs, files) in os.walk(path):
        for file in files:
            # 三个变量依次赋值
            cur_video_path = os.path.join(root, file)
            if not mutagen.File(cur_video_path):
                continue
            cur_video_name = os.path.splitext(file)[0]
            hash_id = getHashId(cur_video_path)


            cur.execute('select name,path from erovideos where hash_id = %s', (hash_id,))
            print(cur.statement)
            fetch1 = cur.fetchone()
            if fetch1 and fetch1[0] == cur_video_name and fetch1[1] == cur_video_path:
                continue
            if fetch1 and fetch1[0] != cur_video_name:
                # 如果找到了hashid对应的，就更新name
                update_query = "update erovideos set name=%s where hash_id=%s"
                update_values = [cur_video_name, hash_id]
                cur.execute(update_query, update_values)
                print(cur.statement)
                con.commit()
            else:
                # 如果没找到hashid对应的，就按照name查找
                cur.execute('select path from erovideos where name = %s COLLATE utf8mb4_unicode_ci', (cur_video_name,))
                print(cur.statement)
                fetch2 = cur.fetchone()

                if fetch2:
                    # 第二次找到了，就说明只是单纯移动了位置，只需要更新hashid和path即可
                    update_query = "UPDATE erovideos SET hash_id=%s, path=%s WHERE name=%s COLLATE utf8mb4_unicode_ci"
                    update_values = [hash_id, cur_video_path,cur_video_name]
                    cur.execute(update_query, update_values)
                    print(cur.statement)
                    con.commit()
                else:
                    # 第二次没找到，只可能是新增或者改变幅度过大，这样已经无法根据这个更新了
                    update_query = "insert into erovideos (path,name,hash_id) values(%s,%s,%s)"
                    update_values = [cur_video_path, cur_video_name, hash_id]
                    cur.execute(update_query, update_values)
                    print(cur.statement)
                    con.commit()


    cur.close()
    con.close()

def getHashId(path):
    unhashed = "neun" + str(os.stat(path).st_ctime)
    hash_object = hashlib.md5()
    hash_object.update(unhashed.encode())
    return hash_object.hexdigest()

if __name__ == "__main__":
    path = r"E:\车"
    # insertvideo(path)
    refreshDatabase(path)
