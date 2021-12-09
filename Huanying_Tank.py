#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 作者：龙.吟
from PIL import Image
import numpy as np
import time


def process_bar(percent, total_length=15):
    """
    进度条
    :param percent: 当前进度
    :param total_length: 进度条长度
    :return:
    """
    bar = '正在加载：'+ '■' * int(percent * total_length) + '□' * (total_length - int(percent * total_length))
    print('\r%s %d%%' % (bar, percent * 100), end='')



def main(pic1, pic2, result_name):
    pic1 = Image.open(pic1).convert("L")
    pic2 = Image.open(pic2).convert("L")
    arr1 = np.array(pic1)
    arr2 = np.array(pic2)
    height = min(arr1.shape[0], arr2.shape[0])
    width = min(arr1.shape[1], arr2.shape[1])
    result = np.zeros((height, width, 2), np.uint8)
    for h in range(0, height):
        process_bar(h / (height - 1), total_length=20)
        for w in range(0, width):
            a = arr1[h, w] / 255  # A=α·X+(1-α)·白色背景
            b = arr2[h, w] / 255  # B=α·X+(1-α)·黑色背景
            alpha = 1 - (a - b)
            g = int((b / alpha) * 255)
            if alpha > 1:
                alpha = 1
            point = [g,  alpha * 255]
            result[h, w] = point
    result = np.array(result)
    result_pic = Image.fromarray(np.uint8(result))
    result_pic.save(result_name)
    result_pic.show()


if __name__ == '__main__':
    # path1 = input('白色背景图片：')
    # path2 = input('黑色背景图片：')
    # path3 = input('输出文件名：')
    # main(path1,path2,path3)
    t1 = time.time()
    main('pic1.jpg', 'pic2.jpg', 't.png')
    t2 = time.time()
    print('\n输出完成！耗时：'+str(t2 - t1))
    # 8.604106903076172s
