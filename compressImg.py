import threading
import time
from PIL import Image
from PyQt6.QtCore import Qt
import webp
import os
from subprocess import run
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QTextEdit, QPushButton


# 多线程测试后cwebp最佳，pil其次但相差不多

DST = ""

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
        self.initUI()
    
    def initUI():

    
def main():
    pass

if __name__ == '__main__':
    pass
