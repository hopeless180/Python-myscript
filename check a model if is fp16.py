import torch
import tensorflow as tf
import os

path = r"./sam_vit_h_4b8939_fp16.pth"
model = torch.load(path)
tensors = list(model.values()) # 获取字典中所有 Tensor 对象
is_fp16 = any(tensor.dtype == torch.float16 for tensor in tensors) # 判断是否是 fp16
print('Is model fp16: ', is_fp16)
if not is_fp16:
    for k, v in model.items():
        if 'bn' in k:
            model[k] = v.float()
    model = {k: v.half() for k, v in model.items()} # 将字典中的所有 Tensor 转换为 fp16 格式
    fp16 = os.path.splitext(path)
    torch.save(model, r'./sam_vit_h_4b8939_fp16.pth') # 保存转换后的模型