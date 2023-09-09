import os
import chardet
import ftfy

def convert_filenames_to_utf8(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 构建文件的完整路径
            file_path = os.path.join(root, file)

            try:
                # 使用ShiftJIS解码文件名，并使用UTF-8重新编码
                decoded_name = file.encode('gbk').decode('shiftjis')
                new_name = decoded_name.encode('utf-8')

                # 构建新的文件路径
                new_file_path = os.path.join(root, new_name)

                # 重命名文件
                os.rename(file_path, new_file_path)

                print(f'Renamed file: {file} -> {new_name}')
            except UnicodeDecodeError:
                print(f'Error decoding filename: {file}')


def detect_encoding(byte_data):
    detector = chardet.UniversalDetector()

    for line in byte_data:
        detector.feed(line)
        if detector.done:
            break

    detector.close()
    encoding = detector.result['encoding']
    confidence = detector.result['confidence']
    return encoding, confidence

def encode_to_bytes(text):
    # 将乱码字符串进行修复和处理
    fixed_text = ftfy.fix_text(text)
    
    # 编码为字节序列
    byte_data = fixed_text.encode()
    return byte_data

text = '鎯旀叝鍋村亶鏄夋鍌絾鍋楀仺鍌滀宫鍌滃倗鍌滃倗濯炊涔仢鍌熷伆涓勫亖鍌戝亖鍌戝亶鍌戝偒鍋欏儐鍍剛鍋婂伃鍋仧鏇绘垼鍋靛伌鍌炴儣濡朵緭'
byte_data = encode_to_bytes(text)
detected_encoding, confidence = detect_encoding(byte_data)
text.encode(detected_encoding)


# 指定目录路径
directory_path = 'g:/[同人音声] 清楚なお姫様を助けたら“らぶらぶ求婚”されて、あまあまおまんこオナホえっちし放題になる生活♪【バイノーラル】'

# 调用函数来进行重命名
convert_filenames_to_utf8(directory_path)