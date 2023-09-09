modify_global_val = "nonsense"

# 第一问，一行求1到100的总和
# 应该是没有除了sum函数以外的答案
def calc_sum_1to100():
    res = sum([x for x in range(1,101)])
    print(res)

# 第二问，修改全局变量，没什么好说的
def modify_global_val():
    global modify_global_val
    modify_global_val = "it is!"
    print(modify_global_val)

# 第三问，列举出5个常用的python库
# os，用于文件系统，操作系统相关的操作
# time，用于获取时间等信息
# random，用于随机从范围内取出数字
# re，用于正则表达式相关
# request，用于网络连接的request和response
## 补充，sys系统操作
## math，数学运算

# 第四问，如何删除其中一个键，或者合并两个字典
def dict_dosomething():
    dict = {"what ever it is": "1", "del": 2}
    dict.pop("del")
    dict2 = {"how ever it is": "2"}
    new_dict = {}
    old_dict_list = [d.copy() for d in [dict, dict2]]
    for i in old_dict_list:
        new_dict.update(i)
    print(new_dict)

# 第六问，列表去重
def del_duplicate_in_list():
    import random
    duplicate_list = []
    for i in range(1,11):
        duplicate_list.append(random.randint(1, 100))
    for i in range(random.randint(1,10)):
        duplicate_list.append(duplicate_list[random.randint(0, 9)])
    new_list = duplicate_list[:]

    # 这里开始是正式处理
    new_list.sort()
    for i in range(len(new_list)-1):
        if i+1 >= len(new_list):
            break
        if new_list[i] == new_list[i + 1]:
            duplicate_list.remove(new_list[i])

    # 实际上，集合set就可以做到
    # 这两个语法都是on
    s = set(duplicate_list)
    not_duplicate_list = [x for x in s]

# 第七问，*args和**kwargs分别代表什么
# 答：*args匹配可变数量的参数列表，本质是列表，而**kwargs匹配不定长度键值对，本质是字典

# 第八问，range（100）在py2和py3中有什么不同
# 答：py3中返回迭代器，py2返回数字

# 第九问，一句话解释什么样的语言能用装饰器


# 第十问，python的数据类型都有哪些
# int，str，dict，list，tuple，bool

# 第十一问，简述面向对象中__new__和__init__区别
# __init__是初始化方法，创建对象后，就立刻被默认调用了，可接收参数
# __new__至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别
# __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类（通过super(当前类名, cls)）__new__出来的实例，或者直接是object的__new__出来的实例
# __init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
# 如果__new__创建的是当前类的实例，会自动调用__init__函数，通过return语句里面调用的__new__函数的第一个参数是cls来保证是当前类实例，如果是其他类的类名，；那么实际创建返回的就是其他类的实例，其实就不会调用当前类的__init__函数，也不会调用其他类的__init__函数。

# 第十二问，with方法都做了什么
# with用两个函数实现了上下文的管理，在上下文管理器对象中，__enter__在执行with中语句前被调用，他的返回值会被传递给as后的变量
# __exit__在执行完with语句后被调用，用于清理

# 第十三问，列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
# 列表推导式包含三部分：输出表达式、循环变量、源列表
def func_map():
    test_list = [1,2,3,4,5]

    res_list =[x for x in list(map(lambda x: x*x, test_list)) if x > 10]
    print(res_list)

# 第十四问，python中生成随机整数，随机小数，0-1之间小数的方法
def rand():
    import random
    print(random.random())
    print(random.randint(1,10))
    print(random.uniform(1,10))

# 第十五问，避免转义字符的话，需要给字符串加什么表示原始字符串
# r"原\始\字\符\串"

# 第十六问，<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
def match_html():
    import re
    lines = [r'<div class="nam">中国</div>']
    for line in lines:
        res = re.findall(r'<div class=".+?">(.+?)</div>', line)
    print(res)

# 第十七问，python中断言方法举例
# my_list = []
# assert my_list, "Error: List is empty"

# 第十八问，数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句
# DELETE FROM student WHERE id NOT IN (SELECT MIN(id) FROM student GROUP BY name)

# 第十九问，10个Linux常用命令
# ls pwd cd touch rm mkdir tree cp mv cat more grep echo

# 第二十问，python2和python3区别？列举5个
# print，range
# py2使用ascii，py3使用utf-8

# 第二十一问，列出python中可变数据类型和不可变数据类型，并简述原理

# 第二十二问，s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
def dupl_str_sort():
    str = "ajldjlajfdljfddd"
    s = set(str)
    s_2_list = [x for x in s]
    s_2_list.sort()
    print("".join(s_2_list))

# 第二十三问，用lambda函数实现两个数相乘
def lambda_test():
    func = lambda x, y: x*y 
    print(func(2,3))

# 第二十四问，字典根据键从小到大排序
def dict_sort():
    dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
    new_dic = sorted(dic.items(), key=lambda x:x[0])
    print(new_dic)

# 第二十五问，利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
def count_str_letter():
    wrong_str = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
    from collections import Counter
    print(Counter(wrong_str))

# 第二十六问，字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三 深圳"
def filter_str_with_num_letter():
    import re
    origin_str = "not 404 found 张三 99 深圳"
    res = re.findall(r"([^ 0-9A-Za-z])", origin_str)
    print(res)

# 第二十七问，filter方法求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def filter_in_list():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = list(filter(lambda x:x%2 == 1, a))
    print(res)

# 第二十八问，列表推导式求列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def list_comprehension_odd():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = [x for x in a if x%2==1]
    print(res)

# 第二十九问，正则re.complie作用
# re.compile是将正则表达式编译成一个对象，加快速度，并重复使用

# 第三十问，a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
# 只有括号中出现逗号才会被识别为元组

# 第三十一问，两个列表[1,3,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]

# 第三十二问，用python删除文件和用linux命令删除文件方法
# os.remove()
# rm 

# 第三十三问，log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
def show_datetime():
    import datetime
    str_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(str_time)

# 第三十九问，[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
def expand_list():
    l = [[1,2],[3,4],[5,6]]
    print(list(j for i in l for j in i))

# 第四十问，x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果

# 第四十一问，举例说明异常模块中try except else finally的相关意义

# 第四十二问，交换两个数
def exchange_two_num():
    a = 114514
    b = 1919810
    print("ori:", a, b)
    a = a + b
    b = a - b
    a = a - b
    print("加减：",a, b)
    a = 114514
    b = 1919810
    a = a*b
    b = a/b
    a = a/b
    print("乘除：",a, b)
    a = 114514
    b = 1919810
    a = a^b
    b = a^b
    a = a^b
    print("位运算：",a, b)

# 第四十四问，a="张明 98分"，用re.sub，将98替换为100
# re.sub(r' ([0-9]+?)分')

# 第四十六问，a="hello"和b="你好"编码成bytes类型
def str_encode():
    a="hello"
    b="你好"
    print("ori:", a, b)
    a.encode()
    b.encode()
    print("bytes:", a, b)

# 第五十一问，正则匹配，匹配日期2018-03-20
# re.findall(r"\d{4}-\d{2}-\d{2}")

# 第五十二问，list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
def my_sort(arr):
    if len(arr) > 1:
        # 首先把列表平分成两部分
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # 递归在这里
        my_sort(left)
        my_sort(right)

        # 合并两个排好序的数组
        # 双循环，循环比较左右两个列表里最小的值泵入arr，谁小就index+1，泵入后arr的index也进1
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # 如果有剩余，将它们添加到结果数组中
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# 第五十六问，列出常见的状态码和意义

# 200 OK

# 请求正常处理完毕

# 204 No Content

# 请求成功处理，没有实体的主体返回

# 206 Partial Content

# GET范围请求已成功处理

# 301 Moved Permanently

# 永久重定向，资源已永久分配新URI

# 302 Found

# 临时重定向，资源已临时分配新URI

# 303 See Other

# 临时重定向，期望使用GET定向获取

# 304 Not Modified

# 发送的附带条件请求未满足

# 307 Temporary Redirect

# 临时重定向，POST不会变成GET

# 400 Bad Request

# 请求报文语法错误或参数错误

# 401 Unauthorized

# 需要通过HTTP认证，或认证失败

# 403 Forbidden

# 请求资源被拒绝

# 404 Not Found

# 无法找到请求资源（服务器无理由拒绝）

# 500 Internal Server Error

# 服务器故障或Web应用故障

# 503 Service Unavailable

# 服务器超负载或停机维护

# 第五十七问，分别从前端、后端、数据库阐述web项目的性能优化
# 前端：可以减少后台的访问次数
# 后端：
# 数据库：可以考虑使用非关系数据库，也可以靠索引快速查询

# 第五十八问，使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
# dic.pop("name") del dic['name']

# 第六十一，简述同源策略
# 需要同时满足，协议相同， 域名相同，端口相同

# 第六十二，cookie存储在浏览器，session存储在后台

# 66、python中copy和deepcopy区别
# copy对于元素采用的是直接赋值，所以如果元素是复杂数据类型，会出现问题，deepcopy没这个问题

# 67、列出几种魔法方法并简要介绍用途

# __init__:对象初始化方法

# __new__:创建对象时候执行的方法，单列模式会用到

# __str__:当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据

# __del__:删除对象执行的方法

# 68、C:\Users\ry-wu.junya\Desktop>python 1.py 22 33命令行启动程序并传参，print(sys.argv)会输出什么数据？
# 脚本名称加 参数构成的列表，这道题的话就是 【1.py 22 33】

# 71、举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
def sort_and_sorted():
    list=[0,-1,3,-10,5,9]
    list1 = list.copy()
    list2 = list.copy()
    list1.sort()
    sorted(list2)
    print(list1, list2)

# 72、对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序

# 使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为
# [0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小
def sort_by_lambda():
    foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
    a = sorted(foo,key=lambda x:(x<0,abs(x)))
    print(a)

# 74、列表嵌套字典的排序，分别根据年龄和姓名排序

# foo = [{"name":"zs","age":19},{"name":"ll","age":54},

# {"name":"wa","age":17},{"name":"df","age":23}]
def sort_by_lambda_dict_in_list():
    foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]
    res = sorted(foo, key = lambda x : (x['age'], x["name"]))
    print(res)

# 75、列表嵌套元组，分别按字母和数字排序
# lambda x:x[0]

# 生成器
# def generator_my():
#     def infinite_sequence():
#         i = 1
#         while True:
#             yield i
#             i += 1

#     # 使用生成器
#     for number in infinite_sequence():
#         print(number)

# 101、求两个列表的交集、差集、并集
def lists_intersection_union_differenceset():
    import random
    list1 = [random.randint(1,7) for x in range(10)]
    list2 = [random.randint(1,7) for x in range(10)]

    intersection = []
    union = []
    difference = []
    i = j = 0
    list1.sort()
    list2.sort()
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            union.append(list1[i])
            difference.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            union.append(list2[j])
            difference.append(list2[j])
            j += 1
        else:
            intersection.append(list1[i])
            union.append(list1[i])
            i += 1
            j += 1
    
    print("ori:", list1, list2)
    print("difference:", difference)
    print("union:", union)
    print("intersection:", intersection)

if __name__ == "__main__":
    # calc_sum_1to100()
    # modify_global_val()
    # dict_dosomething()
    # del_duplicate_in_list()
    # func_map()
    # rand()
    # match_html()
    # dupl_str_sort()
    # lambda_test()
    # dict_sort()
    # count_str_letter()
    # filter_str_with_num_letter()
    # filter_in_list()
    # list_comprehension_odd()
    # show_datetime()
    # expand_list()
    # exchange_two_num()
    # str_encode()
    # my_sort(arr)
    # sort_and_sorted()
    # sort_by_lambda()
    # sort_by_lambda_dict_in_list()
    # generator_my()
    # lists_intersection_union_differenceset()