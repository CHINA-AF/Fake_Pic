#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 作者：龙.吟
from PIL import Image
import numpy as np
import time


def main(pic1, pic2, result_name):
    pic1 = Image.open(pic1).convert("L")
    pic2 = Image.open(pic2).convert("L")
    # np.set_printoptions(precision=0)
    arr1 = np.array(pic1)
    arr2 = np.array(pic2)
    height = min(arr1.shape[0], arr2.shape[0])
    width = min(arr1.shape[1], arr2.shape[1])
    a = arr1[:height, :width]/255
    b = arr2[:height, :width]/255
    alpha = (1 - (a - b)).clip(0, 1)
    g = (b / alpha) * 255
    alpha = np.expand_dims(alpha*255, axis=2)  # 将二维矩阵转为一层的三维矩阵
    g = np.expand_dims(g, axis=2)
    result = np.concatenate((g, alpha), axis=2)  # 将两个三维矩阵按照第三轴叠加
    result_pic = Image.fromarray(np.uint8(result))
    result_pic.save(result_name)
    result_pic.show()


if __name__ == '__main__':
    path1 = input('白色背景图片：')
    path2 = input('黑色背景图片：')
    path3 = input('输出文件名：')
    if '.png' not in path3:
        path3 += '.png'
    t1 = time.time()
    main(path1,path2,path3)
    # main('pic1.jpg', 'pic2.jpg', 't.png')
    t2 = time.time()
    print('\n输出完成！耗时 {:.2f} 秒'.format(t2-t1))
    # 8.604106903076172s
