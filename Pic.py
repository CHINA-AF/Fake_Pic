#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 作者：龙.吟
from PIL import Image
import numpy as np
import time


def main(pic1, pic2, result_name):
    pic1 = Image.open(pic1).convert("L")
    pic2 = Image.open(pic2).convert("L")
    arr1 = np.array(pic1)
    arr2 = np.array(pic2)
    height = min(arr1.shape[0], arr2.shape[0])
    width = min(arr1.shape[1], arr2.shape[1])
    result = np.zeros((height, width, 4), np.uint8)
    # result = []
    # for h in range(0, height):
    #     row = []
    #     for w in range(0, width):
    #         a = arr1[h, w] / 255  # A=α·X+(1-α)·白色背景
    #         b = arr2[h, w] / 255 # B=α·X+(1-α)·黑色背景
    #         alpha = 1 - (a - b)
    #         g = int((b / alpha)*255)
    #         if alpha > 1:
    #             alpha = 1
    #         point = [g, g, g, alpha * 255]
    #         row.append(point)
    #     result.append(row)
    # result = np.array(result)
    result_pic = Image.fromarray(np.uint8(result))
    result_pic.save(result_name)
    result_pic.show()


if __name__ == '__main__':
    path1 = input('白色背景图片：')
    path2 = input('黑色背景图片：')
    path3 = input('输出文件名：')
    # t1 = time.time()
    # main('pic1.jpg','pic2.jpg','t.png')
    # t2 = time.time()
    # print(t2-t1)
    # 8.406963586807251
