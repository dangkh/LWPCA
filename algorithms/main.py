import numpy as np
from algorithms.utils import *
from algorithms.WPCA_locally import *
from algorithms.LWPCA_wholeFrame import *


def WPCA_local(source_data, test_data):
    interpolation = interpolation_WPCA_local(source_data, test_data)
    result = interpolation.result
    return result

def LWPCA_wholeFrame(source_data, test_data):
    interpolation = interpolation_MaskWPCA_wholeFrame(source_data, test_data)
    result = interpolation.result
    return result


if __name__ == '__main__':
    print("main")
