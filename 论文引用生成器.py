
import tkinter as tk
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QTextEdit, QPushButton

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.paperAttr = {
            "index": None,
            "main_author":"",
            "co_author":"",
            "book_title":"",
            "book_symbol":"",
            "book_info":"",
            "version":"",
            "publish_area":"",
            "publisher":"",
            "publish_date":"",
            "page_range":"",
            "url":"",
        }
        self.paperAttrRemark = {
            "index": "序号",
            "main_author":"作者",
            "co_author":"合作作者",
            "book_title":"材料标题",
            "book_symbol":"材料标记",
            "book_info":"材料其他信息",
            "version":"材料版本",
            "publish_area":"出版社所在地区",
            "publisher":"出版社",
            "publish_date":"出版年份",
            "page_range":"页码范围",
            "url":"来源网址",
            "submitButton":"生成"
        }
        self.uiAttr = {
            # "title":"Title",
            # "author":"author",
            # "review":"Review",
            # "titleEdit": None,
            # "authorEdit": None,
            # "reviewEdit": None,
            "submitButton": None,
            "CFLE": None
        }
        # self.uiAttr.update(self.paperAttr)
        self.uiAttrInst = {}
        self.initUI()

    def initUI(self):
        # self.uiAttrInst = {k: QLabel(v) for k, v in self.uiAttr.items()}
        __index = 0
        for k in self.uiAttr:
            if "Button" in k:
                self.uiAttrInst.update({
                    f"QB_{k}": (QPushButton(self.paperAttrRemark[k]), len(self.paperAttr)+3, 1)
                })
                self.uiAttrInst[f"QB_{k}"][0].setObjectName(f"QB_{k}")
            elif "CF" in k:
                self.uiAttrInst.update({
                    f"QTE_{k}": (QTextEdit(), 0, 2, len(self.paperAttr), 2)
                })
                self.uiAttrInst[f"QTE_{k}"][0].setObjectName(f"QTE_{k}")
        for k in self.paperAttr:
            self.uiAttrInst.update({
                f"QL_{k}": (QLabel(self.paperAttrRemark[k]), __index, 0),
                f"QLE_{k}": (QLineEdit(), __index, 1),
            })
            self.uiAttrInst[f"QL_{k}"][0].setObjectName(f"QL_{k}")
            self.uiAttrInst[f"QLE_{k}"][0].setObjectName(f"QLE_{k}")
            __index += 1
        grid = QGridLayout()
        grid.setSpacing(10)

        for widget, *args in self.uiAttrInst.values():
            grid.addWidget(widget, *args)
        
        self.setLayout(grid)
        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('Review')
        for k in self.uiAttrInst:
            if "QLE" in k:
                self.uiAttrInst[k][0].textChanged.connect(self.onChanged)
            elif "QB" in k:
                self.uiAttrInst[k][0].clicked.connect(self.submit)
        self.show()

    def onChanged(self, text):
        sender = self.sender()
        object_name = sender.objectName()
        index = object_name.find('_')  # 找到第一个下划线的位置
        if index != -1:
            attribute_name = object_name[index + 1:]
            self.paperAttr.update({attribute_name: text})

    def submit(self):
        res = generate_citation_formats(**self.paperAttr)
        if "QTE_CFLE" in self.uiAttrInst.keys():
            self.uiAttrInst['QTE_CFLE'][0].setText(res)


def main():
    app = QApplication(sys.argv)
    ex = window()
    sys.exit(app.exec())

def generate_citation_formats(
        index: str = "",
        main_author: str = "",
        co_author: str = "",
        book_title: str = "",
        book_symbol: str = "",
        book_info: str = "",
        version: str = "",
        publish_area: str = "",
        publisher: str = "",
        publish_date: str = "",
        page_range: str = "",
        url: str = "",
) -> str:
    str_citation_formats = append_index("", index)
    str_citation_formats = append_author(str_citation_formats, main_author)
    str_citation_formats = append_co_author(str_citation_formats, co_author)
    str_citation_formats = append_book(str_citation_formats, book_title, book_symbol, book_info)
    str_citation_formats = append_version(str_citation_formats, version)
    str_citation_formats = append_publish(str_citation_formats, publish_area, publisher, publish_date)
    str_citation_formats = append_page(str_citation_formats, page_range)
    str_citation_formats = append_url(str_citation_formats, url)
    return str_citation_formats
    



def append_index(string: str, str_index: int)->str:
    __str = string
    if str_index:
        __str = "[" + str(str_index) + "]"
    return __str

def append_author(str: str, str_main_author: str) -> str:
    assert len(str_main_author)>0, "主作者不能为空"
    authors = []
    __str = str
    
    if "," in str_main_author:
        authors = str_main_author.split(',')
    elif "，" in str_main_author:
        authors = str_main_author.split('，')
    elif " " in str_main_author:
        authors = str_main_author.split()

    authors = [x for x in authors if not x.isspace()]

    if authors and len(authors) > 3:
        __str += ",".join(authors[:2])+"等"
    elif authors and len(authors) <= 3:
        __str += ",".join(authors)
    
    # 分段添加句号
    __str += "."

    return __str

def append_co_author(str: str, str_co_author: str)->str:
    if not str_co_author:
        return str
    __str = str
    __str += str_co_author

    # 分段添加句号
    __str += "."

    return __str

def append_version(str: str, str_version: str)->str:
    if not str_version:
        return str
    __str = str
    __str += str_version

    # 分段添加句号
    __str += "."
    
    return __str

def append_publish(str: str, str_publish_area: str, str_publisher: str, str_publish_date: str)->str:
    if not str_publisher:
        return str
    __str = str
    if str_publish_area:
        __str += str_publish_area + ":"
    __str += str_publisher
    if str_publish_date:
        __str += "," + str_publish_date

    # 分段添加句号
    __str += "."

    return __str
    
    
def append_book(str: str, str_book_title: str, str_book_symbol: str, str_book_info: str) -> str:
    __str = str
    if not str_book_title:
        return __str
    __str += str_book_title
    if str_book_info:
        __str += f":{str_book_info}"
    if str_book_symbol:
        __str += f"[{str_book_symbol}]"
    
    # 分段添加句号
    __str += "."

    return __str

def append_page(str: str, str_pages: str)->str:
    if not str_pages:
        return str
    __str = str[:-1] if str.endswith('.') else str
    __str += ":" + str_pages

    # 分段添加句号
    __str += "."

    return __str

def append_url(str: str, str_url: str)->str:
    if not str_url:
        return str
    __str = str
    __str += str_url

    # 分段添加句号
    __str += "."

    return __str


if __name__ == '__main__':
    main()