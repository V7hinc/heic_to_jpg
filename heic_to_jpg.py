#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
    @Author:V7hinc
    @Datetime:2020/12/13 2:17 下午
    @Software:PyCharm
    @Filename:heic_to_jpg.py
"""

# 正式代码
import whatimage
import pyheif
import traceback
from PIL import Image


def heic_to_jpg(file_path):
    # read_image_file_rb
    with open(file_path, 'rb') as f:
        bytesIo = f.read()
        try:

            fmt = whatimage.identify_image(bytesIo)
            print('fmt = ', fmt)
            if fmt in ['heic']:
                i = pyheif.read_heif(bytesIo)
                # print('i = ', i)
                # print('i.metadata = ', i.metadata)
                pi = Image.frombytes(mode=i.mode, size=i.size, data=i.data)
                # print('pi = ', pi)
                pi.save('heeh.jpg', format="jpeg")
        except:
            traceback.print_exc()


if __name__ == "__main__":
    file_path = 'heic/IMG_0008.HEIC'
    print('file_path = ', file_path)
    heic_to_jpg(file_path)

