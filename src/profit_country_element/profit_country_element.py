# coding=utf-8
import random

import numpy as np
import matplotlib.pyplot as plt

# 国家实力
typical_country_ability_vector = np.array([0.2, 0.5, 0.81])
# 人力成本 与国家成本关系通过increase_labor_vector函数拟合
labor_cost_vector = np.array([0.1, 0.35, 0.55])
# 物质开采难度
typical_element_difficulty_vector = np.array([0.1, 0.15, 0.4, 0.7])
# 物质开采收益
typical_element_income_vector = np.array([0.2, 0.3, 0.6, 1.0])
# 初始利润矩阵，方便后面全局引用
profit_matrix = np.array([[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]])

# 增长因子计算函数控制因子
p = 0.1
# 加权增长因子计算函数控制因子
a, b, c, d = 0.1, 0.1, 0.5, 1.1


# 归一化函数
def maximum_normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range


# 将每次得到的实力因子归一化方便目测比较
country_ability_index_matrix = maximum_normalization(typical_country_ability_vector)
country_ability_absolute_index_matrix = typical_country_ability_vector


# 增长因子计算函数
def increase_function(data, punish):
    global p
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            data[i, j] = data[i, j] * punish[i, j]
    return data


# 加权增长因子计算函数
def increase_vector_function(data):
    global a, b, c, d
    vector = []
    for i in range(data.shape[0]):
        vector.append(a * data[i, 0] + b * data[i, 1] + c * data[i, 2] + d * data[i, 3] + random.uniform(0.9, 1.15))
    return vector


# 劳动力成本计算函数
def increase_labor_vector(data, ability):
    for i in range(data.shape[0]):
        data[i] = np.power(ability[i], 3)
    return data


# 增长循环函数
def increase(times):
    global typical_country_ability_vector, typical_element_income_vector, typical_element_difficulty_vector, \
        labor_cost_vector, profit_matrix, country_ability_index_matrix, country_ability_absolute_index_matrix
    for i in range(times):
        print('第{}次演算'.format(i + 2))
        ability_matrix = np.array(
            [typical_country_ability_vector, typical_country_ability_vector, typical_country_ability_vector,
             typical_country_ability_vector]).transpose()
        print('每个国家的能力为：')
        print(ability_matrix)
        difficulty_matrix = np.array(
            [typical_element_difficulty_vector, typical_element_difficulty_vector, typical_element_difficulty_vector])
        print('每个元素的开采难度为：')
        print(difficulty_matrix)
        punish_matrix = ability_matrix - difficulty_matrix
        min_value = float(punish_matrix[0, 0])
        for j in range(punish_matrix.shape[0]):
            _min = float(np.min(punish_matrix[j]))
            if float(_min < min_value):
                min_value = _min
        punish_matrix = punish_matrix - min_value
        print('惩罚矩阵的初始值为：')
        print(punish_matrix)
        increase_matrix = increase_function(profit_matrix, punish_matrix)
        print('增长矩阵为：')
        print(increase_matrix)
        increase_vector = increase_vector_function(increase_matrix)
        print('增长向量为：')
        print(increase_vector)
        typical_country_ability_vector = np.multiply(typical_country_ability_vector, increase_vector)
        country_ability_absolute_index_matrix = np.vstack(
            (country_ability_absolute_index_matrix, typical_country_ability_vector))
        _temp = maximum_normalization(typical_country_ability_vector)
        country_ability_index_matrix = np.vstack((country_ability_index_matrix, _temp))
        print('增长后的国家能力为：')
        print(typical_country_ability_vector)


# 初始化
def init():
    global typical_country_ability_vector, typical_element_income_vector, typical_element_difficulty_vector, \
        labor_cost_vector, profit_matrix, country_ability_index_matrix, country_ability_absolute_index_matrix
    print('第一次初始化')

    labor_cost_matrix = np.array([labor_cost_vector, labor_cost_vector, labor_cost_vector, labor_cost_vector])
    labor_cost_matrix = labor_cost_matrix.transpose()
    print('人力成本为：')
    print(labor_cost_matrix)
    income_matrix = np.array(
        [typical_element_income_vector, typical_element_income_vector, typical_element_income_vector])
    print('每种元素的收益为：')
    print(income_matrix)
    profit_matrix = income_matrix - labor_cost_matrix
    print('计算得到初始状态的净利润分别为')
    print(profit_matrix)
    ability_matrix = np.array(
        [typical_country_ability_vector, typical_country_ability_vector, typical_country_ability_vector,
         typical_country_ability_vector]).transpose()
    print('每个国家的能力为：')
    print(ability_matrix)
    difficulty_matrix = np.array(
        [typical_element_difficulty_vector, typical_element_difficulty_vector, typical_element_difficulty_vector])
    print('每个元素的开采难度为：')
    print(difficulty_matrix)
    punish_matrix = ability_matrix - difficulty_matrix
    min_val = float(punish_matrix[0, 0])
    for i in range(punish_matrix.shape[0]):
        _min = float(np.min(punish_matrix[i]))
        if float(_min < min_val):
            min_val = _min
    punish_matrix = punish_matrix - min_val
    print('惩罚矩阵的初始值为：')
    print(punish_matrix)
    increase_matrix = increase_function(profit_matrix, punish_matrix)
    print('增长矩阵为：')
    print(increase_matrix)
    increase_vector = increase_vector_function(increase_matrix)
    print('增长向量为：')
    print(increase_vector)
    typical_country_ability_vector = np.multiply(typical_country_ability_vector, increase_vector)
    country_ability_absolute_index_matrix = np.vstack(
        (country_ability_absolute_index_matrix, typical_country_ability_vector))
    _temp = maximum_normalization(typical_country_ability_vector)
    country_ability_index_matrix = np.vstack((country_ability_index_matrix, _temp))
    print('增长后的国家能力为：')
    print(typical_country_ability_vector)


def draw_increase():
    global country_ability_index_matrix, country_ability_absolute_index_matrix
    plt.figure(1, figsize=(19, 11))
    plt.plot(country_ability_index_matrix)
    plt.title('relative')
    plt.figure(2, figsize=(19, 11))
    plt.plot(country_ability_absolute_index_matrix)
    plt.title('absolute')
    plt.show()


if __name__ == '__main__':
    time = 50
    print('********')
    print('开始演算')
    init()
    increase(time)
    print('各国能力经过{}次演算后，变化如下所示'.format(time + 1))
    print(country_ability_index_matrix)
    draw_increase()
    print('结束')
    print('********')
