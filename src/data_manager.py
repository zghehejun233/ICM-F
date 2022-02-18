# coding=utf-8

"""

这个文件用来数据的获取、存储，文件的读取

"""

import numpy as np
import pandas as pd


def global_equity_model_init():
    gdp_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/GDP_world_bank.csv")
    print(gdp_file.to_string())
    print('cao')
