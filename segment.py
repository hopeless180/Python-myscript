# using_colab = False

# if using_colab:
#     import torch
#     import torchvision
#     print("PyTorch version:", torch.__version__)
#     print("Torchvision version:", torchvision.__version__)
#     print("CUDA is available:", torch.cuda.is_available())
#     import sys
#     !{sys.executable} -m pip install opencv-python matplotlib
#     !{sys.executable} -m pip install 'git+https://github.com/facebookresearch/segment-anything.git'
    
#     !mkdir images
#     !wget -P images https://raw.githubusercontent.com/facebookresearch/segment-anything/main/notebooks/images/dog.jpg
        
#     !wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth

import numpy as np
import torch
import matplotlib.pyplot as plt
import cv2
import os

def show_anns(anns):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)
    polygons = []
    color = []
    for ann in sorted_anns:
        m = ann['segmentation']
        img = np.ones((m.shape[0], m.shape[1], 3))
        color_mask = np.random.random((1, 3)).tolist()[0]
        for i in range(3):
            img[:,:,i] = color_mask[i]
        ax.imshow(np.dstack((img, m*0.35)))

_path = r'C:\Users\neun\Downloads\twitter_雨野しぐれ@単行本作業中低浮上(@ame_shlv)_20230406-141810_1643981426969444352_photo.jpg'
# _dir, _name = os.path.split(_path)
# os.chdir(os.path.dirname(_dir))
# image = cv2.imread(_name)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.imdecode(np.fromfile(_path,dtype=np.uint8),-1)


plt.figure(figsize=(20,20))
plt.imshow(image)
plt.axis('off')
plt.show()

import sys
sys.path.append("..")
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor

sam_checkpoint = r"./sam_vit_h_4b8939_fp16.pth"
model_type = "vit_h"

device = "cuda"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)

mask_generator = SamAutomaticMaskGenerator(sam)

masks = mask_generator.generate(image)

print(len(masks))
print(masks[0].keys())

plt.figure(figsize=(20,20))
plt.imshow(image)
show_anns(masks)
plt.axis('off')
plt.show()