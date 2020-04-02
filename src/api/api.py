import imageio
import numpy as np
# from scipy.misc import imread
from skimage.measure import compare_ssim
import urllib.parse
from flask import request, jsonify
import json
from src.util import ssim_consin
from src.util.newCompare import CompareImage
from src.util import phash
import importlib
import sys
from PIL import Image
import os
importlib.reload(sys)


def pictureMatch_ssim():
    try:
        reqdata = json.loads(request.data)
        firstPicture = reqdata['nativeImg']
        secondPicture = reqdata['matchImg']
        # print(firstPicture, secondPicture)
        # print(request)
    except:
        return jsonify({'state': 'error'})

    ssim_consin.urllib_download(firstPicture, './image/img1.png')
    ssim_consin.urllib_download(secondPicture, './image/img2.png')

    img1 = imageio.imread('./image/img1.png')
    img2 = imageio.imread('./image/img2.png')

    img2 = np.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))

    print(img2.shape)
    print(img1.shape)
    ssim = compare_ssim(img1, img2, multichannel=True)

    print(ssim)

    # os.remove('./image/img1.png')
    # os.remove('./image/img2.png')
    # return jsonify(cosin)
    return jsonify(ssim)


def pictureMatch_cosin():
    try:
        reqdata = json.loads(request.data)
        firstPicture = reqdata['nativeImg']
        secondPicture = reqdata['matchImg']
        # print(firstPicture, secondPicture)
        # print(request)
    except:
        return jsonify({'state': 'error'})

    ssim_consin.urllib_download(firstPicture, './image/img1.png')
    ssim_consin.urllib_download(secondPicture, './image/img2.png')

    image1 = Image.open('./image/img1.png')
    image2 = Image.open('./image/img2.png')
    cosin = ssim_consin.image_similarity_vectors_via_numpy(image1, image2)

    print(cosin)

    # os.remove('./image/img1.png')
    # os.remove('./image/img2.png')
    return jsonify(cosin)


def normalCompare():
    try:
        reqdata = json.loads(request.data)
        firstPicture = reqdata['nativeImg']
        secondPicture = reqdata['matchImg']
        # print(firstPicture, secondPicture)
        # print(request)
    except:
        return jsonify({'state': 'error'})

    ssim_consin.urllib_download(firstPicture, './image/img1.png')
    ssim_consin.urllib_download(secondPicture, './image/img2.png')

    compare_image = CompareImage()
    result = compare_image.compare_image(
        "./image/img1.png", "./image/img2.png")

    # os.remove('./image/img1.png')
    # os.remove('./image/img2.png')
    return jsonify(result)


def hashCompare():
    try:
        reqdata = json.loads(request.data)
        firstPicture = reqdata['nativeImg']
        secondPicture = reqdata['matchImg']
        # print(firstPicture, secondPicture)
        # print(request)
    except:
        return jsonify({'state': 'error'})

    im = phash.get_image(firstPicture)
    # im = phash.get_image('./image/img1.png')
    h = phash.avhash(im)

    _im = phash.get_image(secondPicture)
    # _im = phash.get_image('./image/img2.png')
    _h = phash.avhash(_im)
    result = phash.haming_distance_list(h, _h)

    return jsonify(result)
