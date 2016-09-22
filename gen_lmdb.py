import numpy as np
import lmdb
import sys
sys.path.append("/home/lancy/caffe/python")
from PIL import Image
import os
import caffe
from copy import deepcopy


HEIGHT = 500
WIDTH = 500

TRAIN_FILE_LIST = open("./VOC/ImageSets/Segmentation/train.txt", "r").read().strip().split("\n")[:-1]
TEST_FILE_LIST = open("./VOC/ImageSets/Segmentation/val.txt", "r").read().strip().split("\n")[:-1]

DIR = "./VOC"

def gen_input(lmdbname, file_list):
    X = np.zeros((len(file_list), 3, HEIGHT, WIDTH), dtype=np.float32)
    map_size = X.nbytes * 5

    env = lmdb.open(lmdbname, map_size=map_size)

    count = 0
    for i in file_list:
        print count
        with env.begin(write=True) as txn:
            filename = os.path.join(DIR, "JPEGImages", i + ".jpg")
            m = np.asarray(Image.open(filename)).transpose((2, 0, 1))
            datum = caffe.proto.caffe_pb2.Datum()
            datum.channels = m.shape[0]
            datum.height = m.shape[1]
            datum.width = m.shape[2]
            datum.data = m.tobytes()
            str_id = i
            txn.put(str_id.encode("ascii"), datum.SerializeToString())
            count += 1

def gen_output(lmdbname, file_list):
    X = np.zeros((len(file_list), 1, HEIGHT, WIDTH), dtype=np.uint8)
    map_size = X.nbytes * 3

    env = lmdb.open(lmdbname, map_size=map_size)
    
    count = 0
    for i in file_list:
        print count
        with env.begin(write=True) as txn:
            filename = os.path.join(DIR, "SegmentationClass", i + ".png")
            m = deepcopy(np.asarray(Image.open(filename)))
            for x in range(m.shape[0]):
                for y in range(m.shape[1]):
                    if m[x][y] == 255:
                        m[x][y] = 0
            datum = caffe.proto.caffe_pb2.Datum()
            datum.channels = 1
            datum.height = m.shape[0]
            datum.width = m.shape[1]
            datum.data = m.tobytes()
            str_id = i
            txn.put(str_id.encode("ascii"), datum.SerializeToString())
            count += 1

gen_input("train_input_lmdb", TRAIN_FILE_LIST)
gen_output("train_output_lmdb", TRAIN_FILE_LIST)

gen_input("test_input_lmdb", TEST_FILE_LIST)
gen_output("test_output_lmdb", TEST_FILE_LIST)
