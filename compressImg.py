import threading
import time
from PIL import Image
from PyQt6.QtCore import Qt
import webp
import os
from subprocess import run
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QTextEdit, QPushButton, QFileDialog
import sys
from pathlib import Path
import json


# 多线程测试后cwebp最佳，pil其次但相差不多

DST = ""
JSON = ""

class test_compression_with_time():
    def __init__(self) -> None:
        self.testTime()
        pass
    
    def convert_with_pil(image_path: str)->None:
        start_time = time.time()
        __img = Image.open(image_path)
        if image_path.endswith(".jpg"):
            __img = __img.convert('RGB')
        __img.save("test1.webp", 'webp', quality = 50)
        print("convert_with_pil: ", time.time()-start_time)


    def convert_with_pywebp(image_path: str)->None:
        start_time = time.time()
        __img = Image.open(image_path)
        webp.save_image(__img, "test2.webp", quality = 50)
        print("convert_with_pywebp: ", time.time()-start_time)

    def convert_with_cwebp(image_path: str)->None:
        start_time = time.time()
        run(["cwebp", "-q", "50", "-short", image_path.encode(), "-o", "test3.webp".encode()],universal_newlines=True,encoding="utf8")
        print("convert_with_cwebp: ", time.time()-start_time)

    # 多线程测试后cwebp最佳，pil其次但相差不多
    def testTime(self):
        src_path = "G:\\暂时下载\\1月\\[R-18&R-18G]\\芬兰翼骑兵-崩壊スターレイル 抱き枕-115668225-0_3111x3974.png"
        thread1 = threading.Thread(target=self.convert_with_pil, args=(src_path, ))
        thread2 = threading.Thread(target=self.convert_with_pywebp, args=(src_path, ))
        thread3 = threading.Thread(target=self.convert_with_cwebp, args=(src_path, ))
        thread3.start()
        thread2.start()
        thread1.start()
        thread3.join()
        thread2.join()
        thread1.join()

class mainWindow(QWidget):
    def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__()
        self.cache = {}
        self.load_from_cache()
        self.initUI()
    
    def initUI(self):
        grid = QGridLayout()
        # grid.setSpacing()
        walkDir_btn = QPushButton('遍历整个目录的文件')
        listDir_btn = QPushButton('只压缩目录下的文件')
        saveCache_btn = QPushButton('保存缓存')
        grid.addWidget(walkDir_btn, 1, 0)
        grid.addWidget(listDir_btn, 2, 0)
        grid.addWidget(saveCache_btn, 3, 0)
        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        walkDir_btn.clicked.connect(self.click_walkdir_btn)
        listDir_btn.clicked.connect(self.click_listdir_btn)
        self.show()

    def click_walkdir_btn(self):
        home_dir = self.cache['home_dir'] if self.cache else str(Path.home())
        fName = QFileDialog.getExistingDirectory(self, 'Open file', home_dir)

    def click_listdir_btn(self):
        home_dir = self.cache['home_dir'] if self.cache else str(Path.home())
        fName = QFileDialog.getExistingDirectory(self, "Open file", home_dir)

    def save_to_cache(self):
        data = self.cache
        json_path = Path(__file__).absolute().parent.parent / "cache.json"
        with open(json_path, 'w+') as f:
            json.dump(data, f)
    
    def load_from_cache(self):
        json_path = Path(__file__).absolute().parent.parent / "cache.json"
        if os.path.exists(json_path):
            with open(json_path, 'r') as f:
                data = json.load(f)
                self.cache = data.copy()

    
def main():
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec())