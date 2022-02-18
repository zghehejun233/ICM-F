# coding=utf-8

"""

这个文件用来数据的获取、存储，文件的读取

"""

import logging
import pandas as pd
import numpy as np
import config


def global_equity_model_init():
    # config.happiness_index

    human_development_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/人类发展指数.csv")
    config.development_index = human_development_file.values
    logging.debug(config.development_index)

    labor_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/劳动力.csv")
    config.labor_index = labor_file.values
    logging.debug(config.labor_index)

    gdp_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/GDP_world_bank.csv")
    config.economic_index = gdp_file.values
    logging.debug(config.economic_index)

    high_education_file = pd.read_csv('/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model'
                                      '/高等教育入学率.csv')
    config.education_index = high_education_file.values
    logging.debug(config.education_index)

    non_resident_patent = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/非居民专利数.csv")
    config.patents_per_capitan = non_resident_patent.values
    logging.debug(config.patents_per_capitan)

    power_used = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/耗电量.csv")
    config.electricity_per_capitan = power_used.values
    logging.debug(config.electricity_per_capitan)

    population_file = pd.read_csv('/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/人口.csv')
    config.population = population_file.values
    logging.debug(config.population)

    population_per_city_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model"
                                           "/城市人口比例.csv")
    config.population_density_per_city = population_per_city_file.values
    logging.debug(config.population_density_per_city)

    water_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/人均可再生内陆水资源.csv")
    config.water_per_capitan = water_file.values
    logging.debug(config.water_per_capitan)

    forest_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/森林面积.csv")
    config.forest_per_capitan = forest_file.values
    logging.debug(config.forest_per_capitan)


'''
# 数据清洗
def global_equity_model_data_clean():
    # 定义反复使用的remove_list
    remove_list = []

    # 处理发展指数
    for i in range(3, 26, 2):
        remove_list.append(i)
    for j in range(27, 35):
        remove_list.append(j)
    config.development_index = np.delete(config.development_index, remove_list, axis=1)
    remove_list = []

    # 处理劳动力指数
    for i in range(4, 34):
        remove_list.append(i)
    config.labor_index = np.delete(config.labor_index, remove_list, axis=1)
    remove_list = []

    # 处理GDP指数

    # 处理高等教育水平指数
    for i in range(4, 14):
        remove_list.append(i)
    config.education_index = np.delete(config.education_index, remove_list, axis=1)
    remove_list = []

    # 处理非居民专利指数
    for i in range(4, 15):
        remove_list.append(1990+i)
    config.patents_per_capitan = np.nan_to_num(config.patents_per_capitan, nan=0)
    # config.patents_per_capitan = np.delete(config.patents_per_capitan, remove_list, axis=1)


    remove_list = []

    # 处理人均耗电指数

    # 处理人口指数
    # 处理单位人口指数
    # 处理人均水资源指数
    # 处理人均森林面积指数
'''
