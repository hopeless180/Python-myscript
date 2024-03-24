from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox
import base64
import sys
import pyperclip



class window(QWidget):
    def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__()
        self.uiAttr = {
        }
        self.data_mapping = {
            "qq": {
                "click_function": self.click_function1,
                "coor": (0, 0),
                "component": QPushButton
            },
            "steam": {
                "click_function": self.click_function2,
                "coor": (0, 1),
                "component": QPushButton
            },
            "gmail": {
                "click_function": self.click_function3,
                "coor": (0, 2),
                "component": QPushButton
            }
        }
        self.initUI()
    
    def initUI(self):
        inst = {
            k: self.data_mapping[k]['component'](k)
            for k in self.data_mapping.keys() 
        }
        grid = QGridLayout()
        grid.setSpacing(10)
        for k in inst.keys():
            grid.addWidget(inst[k], *self.data_mapping[k]['coor'])
        self.setLayout(grid)
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Review')
        x = type(self.data_mapping['qq']['click_function'])
        for k in inst.keys():
            inst[k].clicked.connect(self.data_mapping[k]['click_function'])
        self.show()
    def click_function1(self):
        s = "neun:qq".encode('utf-8')
        __s = base64.b64encode(s).decode()
        pyperclip.copy(__s)
        QMessageBox.about(self, "密码", f"{__s}\n已复制到剪贴区")
    def click_function2(self):
        s = "neun:steam".encode('utf-8')
        __s = base64.b64encode(s).decode()
        pyperclip.copy(__s)
        QMessageBox.about(self, "密码", f"{__s}\n已复制到剪贴区")
    def click_function3(self):
        s = "neun:gmail".encode('utf-8')
        __s = base64.b64encode(s).decode()
        pyperclip.copy(__s)
        QMessageBox.about(self, "密码", f"{__s}\n已复制到剪贴区")


def main():
    app = QApplication(sys.argv)
    ex = window()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()