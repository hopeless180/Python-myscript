import os
import codecs
import sys

from PyQt6.QtWidgets import QFileDialog, QApplication
from pathlib import Path


def change_encoding(input_file, output_file, new_encoding, old_encoding = "utf-8"):
    try:
        with codecs.open(input_file, 'r', encoding=old_encoding) as f:
            content = f.read()
    except:
        print(f'{input_file}找不到对应编码')
    else:
        with codecs.open(output_file, 'w', encoding=new_encoding, errors = 'replace') as f:
                f.write(content)



def main():
    return 0

dst_encoding = ["shift_jis", "iso-2022-jp", "euc-jp", "big5"]
src_encoding = ["utf-8"]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    input_file = Path(QFileDialog.getOpenFileName()[0])
    old_name = input_file.name
    old_suffix = input_file.suffix
    for i in dst_encoding:
        new_file = old_name + "_" + i + old_suffix
        output_file = input_file.with_name(new_file)
        kwargs = {
            'input_file': input_file,
            'output_file': output_file,
            'old_encoding': src_encoding[0],
            'new_encoding': i
        }
        change_encoding(**kwargs)
    sys.exit(app.exec())
