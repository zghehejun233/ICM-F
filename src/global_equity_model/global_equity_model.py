# coding=utf-8
"""

本函数为全球公平模型的具体实现

"""

import logging
import numpy as np
import pandas as pd
from scipy import optimize

np.seterr(divide='ignore', invalid='ignore')


def maximum_normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range


def topsis(data, list_max, list_min):
    max_list = []
    min_list = []
    answer_list = []
    for i in range(data.shape[0]):
        max_sum = 0
        min_sum = 0
        print(data.shape)
        for k in range(data.shape[1]):
            max_sum += np.power(data[i, k] - list_max[k], 2)
            min_sum += np.power(data[i, k] - list_min[k], 2)
        max_list.append(pow(max_sum, 0.5))
        min_list.append(pow(min_sum, 0.5))
        answer_list.append(min_list[i] / (min_list[i] + max_list[i]))
        max_sum, min_sum = 0, 0
    answer = np.array(answer_list)
    print(answer)


def technology_modify_function(data):
    list_max = np.vstack((np.max(data[:, 0]), np.max(data[:, 1])))
    list_min = np.vstack((np.min(data[:, 0]), np.min(data[:, 1])))
    return topsis(data, list_max, list_min)


def resource_modify_function(data):
    list_max = np.vstack((np.max(data[:, 0]), np.max(data[:, 1]), np.max(data[:, 2])))
    list_min = np.vstack((np.min(data[:, 0]), np.min(data[:, 1]), np.min(data[:, 2])))
    return topsis(data, list_max, list_min)


def start():
    human_development_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/人类发展指数.csv")
    development_index = human_development_file.values

    labor_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/劳动力.csv")
    labor_index = labor_file.values

    gdp_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/GDP_world_bank.csv")
    economic_index = gdp_file.values

    high_education_file = pd.read_csv('/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model'
                                      '/高等教育入学率.csv')
    temp = high_education_file.values
    education_index = temp[:, 3:].astype(np.float64)

    non_resident_patent = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/非居民专利数.csv")
    temp = non_resident_patent.values
    patents_per_capitan = temp[:, 3:].astype(np.float64)

    power_used = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/耗电量.csv")
    temp = power_used.values
    electricity_per_capitan = temp[:, 3:].astype(np.float64)

    population_file = pd.read_csv('/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/人口.csv')
    population = population_file.values

    population_per_city_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model"
                                           "/城市人口比例.csv")
    temp = population_per_city_file.values
    population_density_per_city = temp[:, 3:].astype(np.float64)

    # 数据拟合不好，先不看
    water_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/人均可再生内陆水资源.csv")
    temp = water_file.values
    water_per_capitan = temp[:, 6:].astype(np.float64)

    forest_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/森林面积.csv")
    temp = forest_file.values
    forest_per_capitan = temp[:, 3:].astype(np.float64)

    print('导入数据结束')

    # 清洗数据

    development_index = np.nan_to_num(development_index, nan=0)
    labor_index = np.nan_to_num(labor_index, nan=0)
    economic_index = np.nan_to_num(economic_index, nan=0)
    education_index = np.nan_to_num(education_index, nan=0)
    population = np.nan_to_num(population, nan=0)

    patents_per_capitan = np.nan_to_num(patents_per_capitan, nan=0.0)
    electricity_per_capitan = np.nan_to_num(electricity_per_capitan, nan=0)

    population_density_per_city = np.nan_to_num(population_density_per_city, nan=0)
    water_per_capitan = np.nan_to_num(water_per_capitan, nan=0)
    forest_per_capitan = np.nan_to_num(forest_per_capitan, nan=0)
    print(population_density_per_city)
    print(water_per_capitan)
    print(forest_per_capitan)
    print('清理nan数据结束')

    # 定义幸福度指数计算
    # 定义发展指数计算
    # 定义资源水平指数计算
    # 城市人口比例逐行归一化
    for i in range(population_density_per_city.shape[1]):
        population_density_per_city[:, i] = maximum_normalization(population_density_per_city[:, i])
    # 人均可再生水逐行归一化
    for i in range(water_per_capitan.shape[1]):
        water_per_capitan[:, i] = maximum_normalization(water_per_capitan[:, i])
    # 人均森林面积逐行归一化
    for i in range(forest_per_capitan.shape[1]):
        forest_per_capitan[:, i] = maximum_normalization(forest_per_capitan[:, i])
    temp_matrix = np.vstack((population_density_per_city[:124, 0], water_per_capitan[:124, 0]))
    resource_matrix = temp_matrix.transpose()
    for i in range(1, 30):
        temp_matrix = np.vstack(
            (population_density_per_city[:124, i], water_per_capitan[:124, i], forest_per_capitan[:124, i]))
        temp_matrix = temp_matrix.transpose()
        resource_matrix = np.column_stack((resource_matrix, temp_matrix))
    resource_matrix = resource_matrix.reshape((29, 124, 3))

    # 定义劳动力水平指数计算
    # 定义经济水平指数计算
    # 定义教育水平指数计算
    # 科技发展水平指数计算
    # 非居民专利数逐行归一化数据
    for i in range(patents_per_capitan.shape[1]):
        patents_per_capitan[:, i] = maximum_normalization(patents_per_capitan[:, i])
    # 取对数
    for i in range(patents_per_capitan.shape[0]):
        for j in range(patents_per_capitan.shape[1]):
            if patents_per_capitan[i, j] != 0:
                patents_per_capitan[i, j] = np.log(patents_per_capitan[i, j])
    # 人均耗电量逐行归一化数据
    for i in range(electricity_per_capitan.shape[1]):
        electricity_per_capitan[:, i] = maximum_normalization(electricity_per_capitan[:, i])
    # 构建并转置矩阵
    temp_matrix = np.vstack((electricity_per_capitan[:124, 0], patents_per_capitan[:124, 0]))
    technology_matrix = temp_matrix.transpose()
    # 构建高维矩阵
    for i in range(1, 40):
        temp_matrix = np.vstack((electricity_per_capitan[:124, i], patents_per_capitan[:124, i]))
        temp_matrix = temp_matrix.transpose()
        technology_matrix = np.column_stack((technology_matrix, temp_matrix))
    technology_matrix = technology_matrix.reshape((40, 124, 2))

    # topsis分析测试
    test_data = maximum_normalization(np.random.randn(20)).reshape(10, 2)
    print(test_data)
    technology_modify_function(test_data)

    # 定义人口水平指数计算
    #
