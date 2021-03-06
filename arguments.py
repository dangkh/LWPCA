import sys
import argparse
sys.path.append("/Users/kieudang/Desktop/weightPCA/")
from data_utils import *

class arguments(argparse.Namespace):

    length3D = 400
    

    # """ CMU config """
    missing_index = [50, 450]
    # current result
    inner_testing = [[250, 650], [450, 850], [1050, 1450], [1450, 1850]]
    data_link = "./data3D/135_02.txt"
    
    collection_link = ["./data3D/135_01.txt", "./data3D/135_03.txt"]
    outter_testing = [[1450, 1850], [1450, 1850]]
    # single case
    # weightScale = 2000
    # MMweight = 0.001

    # mul case
    # weightScale = 2000
    # MMweight = 0.02
    # others = 0.001
    

    
    """ HDM config """
    # missing_index = [150, 550]
    
    # inner_testing = [[350, 750], [550, 950], [1050, 1450], [1450, 1850]]
    # data_link = "./data3D/HDM3.txt"
    # collection_link = ["./data3D/135_01.txt", "./data3D/135_03.txt"]
    # outter_testing = [[1450, 1850], [1450, 1850]]
    # # single case
    # # weightScale = 500
    # # MMweight = 0.001

    # # mul case
    # # weightScale = 500
    # # MMweight = 0.02
    # # others = 0.001


    tmp = []
    counter = 0
    for x in collection_link:
        print("reading source: ", x)
        source, _ = read_tracking_data3D(x)
        source = source.astype(float)
        source = source[outter_testing[counter][0]:outter_testing[counter][1]]
        counter += 1
        K = source.shape[0] // length3D
        list_patch = [[x * 400, (x + 1) * 400] for x in range(K)]
        tmp.append(np.copy(source[list_patch[0][0]: list_patch[-1][1]]))
    datas = np.vstack(tmp)

    
    test_link = "./test/"
    save_dir = "./result/"
    default_test_link = "./test/fullFrame/2.txt"


arg = arguments
