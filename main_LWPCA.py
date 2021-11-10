# LWPCA
import numpy as np
from data_utils import *
from arguments import arg
import sys
import random
from algorithms.main import *
import os
from datetime import datetime


def load_missing(sub_link=None):
    if sub_link == None:
        link = arg.default_test_link
    else:
        link = sub_link
    matrix = []
    f = open(link, 'r')
    print(link)
    for line in f:
        elements = line[:-1].split(' ')
        matrix.append(list(map(int, elements)))
    f.close()

    matrix = np.array(matrix)  # list can not read by index while arr can be
    return matrix

def process_hub(data=None):
    result = []
    list_patch = arg.inner_testing
    dataInner = np.vstack(
        [np.copy(Tracking3D[list_patch[i][0]:list_patch[i][1]]) for i in range(len(list_patch))])
    print("data from testing sample : ", dataInner.shape)

    try:
        if not data:
            dataCollection = dataInner
    except Exception as e:
        dataCollection = np.vstack((data, dataInner))

    print("update reference:")
    print("collection shape : ", dataCollection.shape)
    test_folder = arg.test_link
    prefix = arg.save_dir
    order_fol = []
    print("missing in data collection: ")
    print(np.where(dataCollection == 0))
    frames = np.where(dataCollection == 0)[0]
    frames = np.unique(frames)
    dataCollection = np.delete(dataCollection, frames, 0)
    for test_name in os.listdir(test_folder):
        current_folder = test_folder + test_name
        if os.path.isdir(current_folder):
            order_fol.append(test_name)
            resCF = []
            test_reference = arg.missing_index
            number_test = 50
            print("******************************************************************************************")
            print("**************************************** STARTING ****************************************")
            print("******************************************************************************************")
            for sub_test in range(number_test):
                result_path = current_folder + '/' + str(sub_test) + ".txt"
                
                print(result_path)
                full_matrix = load_missing(result_path)
                A1 = np.copy(Tracking3D[test_reference[0]:test_reference[1]])
                # np.savetxt("original.txt", A1, fmt = "%.2f")
                missing_matrix = np.copy(full_matrix)
                A1zero = np.copy(A1)
                A1zero[np.where(missing_matrix == 0)] = 0
                # np.savetxt("missing_matrix.txt", A1zero, fmt = "%.2f")
                
                timecounter = datetime.now()
                A1_star8 = WPCA_local(np.copy(dataCollection), np.copy(A1zero))
                value = np.around(calculate_mae_matrix(
                    A1[np.where(A1zero == 0)] - A1_star8[np.where(A1zero == 0)]), decimals=17)
                print(str(datetime.now() - timecounter))
                # np.savetxt("interpolate.txt", A1_star8, fmt = "%.2f")

                resCF.append(value)
            print("**************************************** END ****************************************")
            result.append(np.asarray(resCF).mean())
            print(resCF)
            f.write(str([resCF]) + "\n")
    print(order_fol)
    return [result], order_fol


if __name__ == '__main__':
    f = open(arg.save_dir + 'result.txt', "w")
    print("reference data:")
    datas = arg.datas
    Tracking3D, _ = read_tracking_data3D(arg.data_link)
    Tracking3D = Tracking3D.astype(float)
    result, order_fol = process_hub()
    # result, order_fol = process_hub(data = datas)
    print(result)
    f.write(str(result) + "\n")
    f.write(str(order_fol) + "\n")
    f.write(str(datetime.now()))
    f.close()
