from PIL import Image
import os

MEGABYTE = 1<<20
KILOBYTE = 1<<10
GIGABYTE = 1<<30
def get_newName(fileName, suffix):
    last_dot_index = fileName.rfind('.')
    if last_dot_index > -1:
        newName = fileName[:last_dot_index] + suffix + fileName[last_dot_index:]
    else:
        newName = fileName + suffix
    
    return newName


def resize_image(source_directory, target_directory, file_name, border = 2 * MEGABYTE):
    # 打开图像文件
    input_path = os.path.join(source_directory, file_name)
    output_path = os.path.join(target_directory, file_name)
    image = Image.open(input_path)
    ori_fileSize = os.path.getsize(input_path)
    # 假设是一次相关
    # 和边界大小做比求压缩比例
    for i in range(100):
        width_ratio = ori_fileSize / (border*pow(0.9, i))
        # 计算缩放比例宽高比
        ratio = image.size[0] / image.size[1]
        # 计算缩放后的尺寸
        new_width = int(image.width / width_ratio)
        new_height = int(new_width / ratio)
        resized_image = image.resize((new_width, new_height))
        resized_image_filePath = get_newName(os.path.join(target_directory, file_name), "-resized")
        resized_image.save(resized_image_filePath)
        first_img_fileSize = os.path.getsize(resized_image_filePath)
        if first_img_fileSize < border:
            break

    # 关闭图像
    image.close()


def main():
    return 0


if __name__ == "__main__":
    src = "C:\\Users\\neun\\Documents\Tencent Files\\474527440\\FileRecv\\MobileFile"
    resize_image(src, src, "IMG_20210322_155737.jpg")
