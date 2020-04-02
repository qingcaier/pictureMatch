# coding=utf-8
from PIL import Image
from numpy import average, linalg, dot
import os
import importlib
import sys
import urllib

importlib.reload(sys)
os.makedirs('./image/', exist_ok=True)
# IMAGE_URL = "http://cdn.cdlshow.xyz/GZ_01_0003_华南土特产展览交流大会旧址手工业馆/crop-建筑整体透视或立面2.jpg"
# IMAGE_URL = "http://www.open-open.com/bbs/uploadImg/20160107/20160107133856_341.jpg"
# IMAGE_URLTemp = urllib.parse.quote(IMAGE_URL, safe='/:?=')
# newPath = unicode(IMAGE_URL, 'utf8')


# 将网络url图片下载到本地
def urllib_download(IMAGE_URL, urlName):
    from urllib.request import urlretrieve
    # import urllib.parse
    # newIMAGE_URL = urllib.parse.unquote(IMAGE_URL)
    newIMAGE_URL = urllib.parse.quote(IMAGE_URL, safe='/:?=')
    urlretrieve(newIMAGE_URL, urlName)


# def get_thumbnail(image, size=(1200, 750), greyscale=False):
def get_thumbnail(image, size=(400, 250), greyscale=False):
    image = image.resize(size, Image.ANTIALIAS)
    if greyscale:
        image = image.convert('L')
    return image


def image_similarity_vectors_via_numpy(image1, image2):

    image1 = get_thumbnail(image1)
    image2 = get_thumbnail(image2)
    images = [image1, image2]
    vectors = []
    norms = []
    for image in images:
        vector = []
        for pixel_tuple in image.getdata():
            vector.append(average(pixel_tuple))
        vectors.append(vector)
        norms.append(linalg.norm(vector, 2))
    a, b = vectors
    a_norm, b_norm = norms
    res = dot(a / a_norm, b / b_norm)
    return res
