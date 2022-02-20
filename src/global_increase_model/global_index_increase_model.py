# coding=utf-8

import numpy as np

typical_country_labor_vector = np.array([0.1, 0.2, 0.8])
typical_country_tech_vector = np.array([0.3, 0.5, 0.6])
labor_cost_vector = np.array([0.1, 0.35, 0.55])
typical_element_difficulty_vector = np.array([0.1, 0.15, 0.4, 0.7])
typical_element_income_vector = np.array([0.2, 0.3, 0.6, 1.0])
profit_matrix = np.array([[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]])
country_ability_index_matrix = typical_country_ability_vector

p = 0.1
a, b, c, d = 0.1, 0.1, 0.5, 1.1


def increase_function(data, punish):
    global p
    data = data
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            data[i, j] = data[i, j] * punish[i, j]
    return data


def increase_vector_function(data):
    global a, b, c, d
    vector = []
    for i in range(data.shape[0]):
        vector.append(a * data[i, 0] + b * data[i, 1] + c * data[i, 2] + d * data[i, 3] + 1)
    print(vector)
    return vector


def incrase_labor_vector(data, ability):
    for i in range(data.shape[0]):
        data[i] = np.power(ability[i], 3)
    return data


def increase(times):
    global typical_country_ability_vector, typical_element_income_vector, typical_element_difficulty_vector, \
        labor_cost_vector, profit_matrix, country_ability_index_matrix
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
        min = float(punish_matrix[0, 0])
        for i in range(punish_matrix.shape[0]):
            _min = float(np.min(punish_matrix[i]))
            if float(_min < min):
                min = _min
        punish_matrix = punish_matrix - min
        print('惩罚矩阵的初始值为：')
        print(punish_matrix)
        increase_matrix = increase_function(profit_matrix, punish_matrix)
        print('增长矩阵为：')
        print(increase_matrix)
        increase_vector = increase_vector_function(increase_matrix)
        print('增长向量为：')
        print(increase_vector)
        typical_country_ability_vector = np.multiply(typical_country_ability_vector, increase_vector)
        country_ability_index_matrix = np.vstack((country_ability_index_matrix, typical_country_ability_vector))
        print('增长后的国家能力为：')
        print(typical_country_ability_vector)


def init():
    global typical_country_ability_vector, typical_element_income_vector, typical_element_difficulty_vector, \
        labor_cost_vector, profit_matrix, country_ability_index_matrix
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
    min = float(punish_matrix[0, 0])
    for i in range(punish_matrix.shape[0]):
        _min = float(np.min(punish_matrix[i]))
        if float(_min < min):
            min = _min
    punish_matrix = punish_matrix - min
    print('惩罚矩阵的初始值为：')
    print(punish_matrix)
    increase_matrix = increase_function(profit_matrix, punish_matrix)
    print('增长矩阵为：')
    print(increase_matrix)
    increase_vector = increase_vector_function(increase_matrix)
    print('增长向量为：')
    print(increase_vector)
    typical_country_ability_vector = np.multiply(typical_country_ability_vector, increase_vector)
    country_ability_index_matrix = np.vstack((country_ability_index_matrix, typical_country_ability_vector))
    print('增长后的国家能力为：')
    print(typical_country_ability_vector)


if __name__ == '__main__':
    time = int(input('输入演算的次数'))
    print('********')
    print('开始演算')
    init()
    increase(time)
    print('各国能力经过{}次演算后，变化如下所示'.format(time + 1))
    print(country_ability_index_matrix)
    print('结束')
    print('********')
