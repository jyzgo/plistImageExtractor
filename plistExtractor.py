#! /usr/lical/bin/python
import os
import sys
from PIL import Image
from xml.etree import ElementTree
import json
import plistlib


def tree_to_dict(tree):
    d = {}
    for index, item in enumerate(tree):
        if item.tag == 'key':
            if tree[index + 1].tag == 'string':
                d[item.text] = tree[index + 1].text
            elif tree[index + 1].tag == 'true':
                d[item.text] = True
            elif tree[index + 1].tag == 'false':
                d[item.text] = False
            elif tree[index + 1].tag == 'dict':
                d[item.text] = tree_to_dict(tree[index + 1])
    return d


def frames_from_data(filename):
    img_filename = filename + '.png'
    data_filename = filename + '.plist'
    root = ElementTree.fromstring(open(data_filename, 'r').read())
    plist_dict = tree_to_dict(root[0])

    def to_list(x): return x.replace('{', '').replace('}', '').split(',')
    frames = list(plist_dict['frames'].items())
    dirname = os.path.dirname(os.path.realpath(filename)) + '/' + filename

    if not os.path.isdir(dirname):
        os.makedirs(dirname)

    for k, v in frames:
        outfile = str(k)
        print("outfile " + outfile)
        outfile = dirname + '/' + outfile
        frame = v
        isRotate = bool(frame['textureRotated'])
        spriteSize = to_list(frame['spriteSize'])
        width = int(spriteSize[1] if isRotate else spriteSize[0])
        height = int(spriteSize[0] if isRotate else spriteSize[1])
        rectlist = to_list(frame['textureRect'])

        spriteSourceSize = to_list(frame['spriteSourceSize'])
        realWidth = int(spriteSourceSize[0])
        realHeight = int(spriteSourceSize[1])
        realSizeList = [realWidth, realHeight]
        img = Image.open(img_filename)
        box = (
            int(rectlist[0]),
            int(rectlist[1]),
            int(rectlist[0]) + width,  # height,
            int(rectlist[1]) + height  # width
        )

        img = img.crop(box)

        if(isRotate):
            img = img.transpose(Image.ROTATE_90)
        offsetList = to_list(frame['spriteOffset'])
        offset_x = int(offsetList[1] if isRotate else offsetList[0])
        offset_y = int(offsetList[0] if isRotate else offsetList[1])
        offset_x = int(offsetList[0])
        offset_y = int(offsetList[1])
        result_box = (
            int((
                (realSizeList[1] if isRotate else realSizeList[0])-width)/2 + offset_x),
            int((
                (realSizeList[0] if isRotate else realSizeList[1])-height)/2 + offset_y),

        )

        outImg = Image.new('RGBA', (realWidth, realHeight), (0, 0, 0, 0))
        outImg.paste(img, result_box, mask=0)
        outImg.save(outfile)


if __name__ == '__main__':
    outfile = "outtest.png"
    filename = sys.argv[1]
    frames_from_data(filename)
