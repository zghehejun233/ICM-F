# coding=utf-8
"""

本函数为全球公平模型的具体实现

"""

import numpy as np
import pandas as pd

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
        for k in range(data.shape[1]):
            max_sum += np.power(data[i, k] - list_max[k], 2)
            min_sum += np.power(data[i, k] - list_min[k], 2)
        max_list.append(pow(max_sum, 0.5))
        min_list.append(pow(min_sum, 0.5))
        answer_list.append(min_list[i] / (min_list[i] + max_list[i]))
        max_sum, min_sum = 0, 0
    answer = np.array(answer_list)
    return answer


def technology_modify_function(data):
    list_max = np.vstack((np.max(data[:, 0]), np.max(data[:, 1])))
    list_min = np.vstack((np.min(data[:, 0]), np.min(data[:, 1])))
    return topsis(data, list_max, list_min)


def resource_modify_function(data):
    list_max = np.vstack((np.max(data[:, 0]), np.max(data[:, 1])))
    list_min = np.vstack((np.min(data[:, 0]), np.min(data[:, 1])))
    return topsis(data, list_max, list_min)


def get_final_index(inc, res, lab, eco, edu, tech, pop):
    a = 0.30
    b = 0.28
    c = 0.22
    d = 0.45
    e = 0.34
    f = 0.28
    g = 0.33
    final_index = np.array(a * inc + b * res + c * lab + d * eco + e * edu + f * tech + g * pop)
    final_index_except_america = final_index[:-1, :]
    for i in range(final_index.shape[1]):
        final_index[:, i] = maximum_normalization(final_index[:, i])
    for i in range(final_index_except_america.shape[1]):
        final_index_except_america[:, i] = maximum_normalization(final_index_except_america[:, i])
    np.savetxt("../data/global_equity_model/final_index.csv", final_index, delimiter=",")
    return final_index


def start():
    income_file = pd.read_csv('/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/人均国民净收入额筛选数据.csv')
    temp = income_file.values
    income_index = temp[:, 27:].astype(np.float64)

    labor_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/劳动力筛选数据.csv",
                             encoding='utf-8')
    temp = labor_file.values
    labor_index = temp[:, 7:].astype(np.float64)

    gdp_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/GDP数据筛选数据.csv")
    temp = gdp_file.values
    economic_index = temp[:, 37:].astype(np.float64)

    high_education_file = pd.read_csv('/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model'
                                      '/高等教育入学率筛选数据.csv')
    temp = high_education_file.values
    education_index = temp[:, 27:].astype(np.float64)

    non_resident_patent = pd.read_csv(
        "/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/非居民专利数筛选数据.csv")
    temp = non_resident_patent.values
    patents_per_capitan = temp[:, 12:].astype(np.float64)

    power_used = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/耗电量筛选数据.csv")
    temp = power_used.values
    electricity_per_capitan = temp[:, 21:].astype(np.float64)

    high_technology_income_file = pd.read_csv(
        "/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/高科技出口（美元）筛选数据.csv")
    temp = high_technology_income_file.values
    high_technology_income = temp[:, 3:].astype(np.float64)

    population_file = pd.read_csv('/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/人口筛选数据.csv')
    temp = population_file.values
    population_index = temp[:, 37:].astype(np.float64)

    population_per_city_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model"
                                           "/城镇人口比例筛选数据.csv")
    temp = population_per_city_file.values
    population_density_per_city = temp[:, 32:].astype(np.float64)

    forest_file = pd.read_csv("/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_model/森林面积筛选数据.csv")
    temp = forest_file.values
    forest_per_capitan = temp[:, 8:].astype(np.float64)

    print('导入数据结束')

    # 清洗数据

    income_index = np.nan_to_num(income_index, nan=0)
    labor_index = np.nan_to_num(labor_index, nan=0)
    economic_index = np.nan_to_num(economic_index, nan=0)
    education_index = np.nan_to_num(education_index, nan=0)
    population_index = np.nan_to_num(population_index, nan=0)

    patents_per_capitan = np.nan_to_num(patents_per_capitan, nan=0.0)
    electricity_per_capitan = np.nan_to_num(electricity_per_capitan, nan=0)

    population_density_per_city = np.nan_to_num(population_density_per_city, nan=0)
    forest_per_capitan = np.nan_to_num(forest_per_capitan, nan=0)
    print('清理nan数据结束')

    # 定义幸福度指数计算
    for i in range(income_index.shape[1]):
        income_index[:, i] = maximum_normalization(income_index[:, i])

    # 资源水平计算 城市人口比例逐行归一化
    for i in range(population_density_per_city.shape[1]):
        population_density_per_city[:, i] = maximum_normalization(population_density_per_city[:, i])
    # 人均森林面积逐行归一化
    for i in range(forest_per_capitan.shape[1]):
        forest_per_capitan[:, i] = maximum_normalization(forest_per_capitan[:, i])
    # 构建资源矩阵
    temp_matrix = np.vstack((population_density_per_city[:, 0], forest_per_capitan[:, 0]))
    resource_matrix = temp_matrix.transpose()
    for i in range(1, 25):
        temp_matrix = np.vstack(
            (population_density_per_city[:, i], forest_per_capitan[:, i]))
        resource_matrix = np.hstack((resource_matrix, temp_matrix.transpose()))
    # 计算指数
    temp_data = resource_matrix[:, :2]
    answer = resource_modify_function(temp_data)
    resource_index = np.array(answer)
    for i in range(25):
        temp_data = resource_matrix[:, 2 * i:2 * (i + 1)]
        answer = resource_modify_function(temp_data)
        resource_index = np.hstack((resource_index, answer))

    # 定义劳动力水平指数计算
    for i in range(labor_index.shape[1]):
        labor_index[:, i] = maximum_normalization(labor_index[:, i])
    # 定义经济水平指数计算
    for i in range(economic_index.shape[1]):
        economic_index[:, i] = maximum_normalization(economic_index[:, i])

    # 定义教育水平指数计算
    for i in range(education_index.shape[1]):
        education_index[:, i] = maximum_normalization(education_index[:, i])

    # 科技水平 非居民专利数逐行归一化数据
    for i in range(patents_per_capitan.shape[1]):
        patents_per_capitan[:, i] = maximum_normalization(patents_per_capitan[:, i])
    # 取对数
    for i in range(electricity_per_capitan.shape[0]):
        for j in range(electricity_per_capitan.shape[1]):
            if electricity_per_capitan[i, j] != 0:
                electricity_per_capitan[i, j] = np.log(electricity_per_capitan[i, j])
    # 人均耗电量逐行归一化数据
    for i in range(electricity_per_capitan.shape[1]):
        electricity_per_capitan[:, i] = maximum_normalization(electricity_per_capitan[:, i])
    # 构建资源矩阵
    temp_matrix = np.vstack((patents_per_capitan[:, 0], electricity_per_capitan[:, 0]))
    technology_matrix = temp_matrix.transpose()
    for i in range(1, 25):
        temp_matrix = np.vstack(
            (patents_per_capitan[:, i], electricity_per_capitan[:, i]))
        technology_matrix = np.hstack((resource_matrix, temp_matrix.transpose()))
    # 计算指数
    temp_data = technology_matrix[:, :2]
    answer = technology_modify_function(temp_data)
    technology_index = np.array(answer)
    for i in range(25):
        temp_data = technology_matrix[:, 2 * i:2 * (i + 1)]
        answer = technology_modify_function(temp_data)
        technology_index = np.hstack((technology_index, answer))

    # 定义人口水平指数计算
    for i in range(population_index.shape[1]):
        population_index[:, i] = maximum_normalization(population_index[:, i])

    print('因子计算结束')
    get_final_index(income_index, resource_index, labor_index, economic_index, education_index, technology_index,
                    population_index)
    print('全球公平指数生成')
