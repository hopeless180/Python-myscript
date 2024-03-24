from PIL import Image
import random

def transfer(file):
    im = Image.open(file)
    # if im.width > im.height:
    #     # 4：3
    #     new_width = im.width
    #     new_height = int(im.width * 3/4)
    #     margin = (im.height - new_height) // 2
    #     im = im.crop((0, margin, im.width, im.height - margin))
    # else:
    #     new_height = im.height
    #     new_width = int(im.height * 3/4)
    #     margin = (im.width - new_width) // 2
    #     im = im.crop((margin, 0, im.width - margin, im.height))
    new_height = 2000
    new_width = 1200
    margin = (im.height - new_height) // 2
    im = im.crop((0, margin, new_width, new_height+margin))
    return im

def cropImage(image):
    if image.width<image.height:
        image = image.rotate(-90, expand=True)
        flag_rotate = True
    cropped_images = []
    cropped_images_width = int(image.width / 4)
    cropped_images_height = int(image.height / 2)
    cropped_images_index = []
    for i in range(2):
        for j in range(4):
            crop_area = (cropped_images_width * j, cropped_images_height * i, cropped_images_width * (j + 1), cropped_images_height * (i + 1))
            cropped_images.append(image.crop(crop_area))
    cropped_images = [x for x in enumerate(cropped_images)]
    random.shuffle(cropped_images)
    shuffle_image = Image.new("RGB", (image.width, image.height))
    for i, item in enumerate(cropped_images):
        shuffle_image.paste(item[1], (cropped_images_width * (i % 4), 0 if i < 4 else cropped_images_height))
        cropped_images_index.append(item[0])
    if flag_rotate:
        shuffle_image = shuffle_image.rotate(90, expand=True)

if __name__ == '__main__':
    flag_rotate = False
    image_path = 'image.jpg'
    image = transfer(image_path)

    
    shuffle_image.save("shuffle.jpg")

    if flag_rotate:
        res_image = res_image.rotate(90, expand=True)
    res_image.save('res.jpg')