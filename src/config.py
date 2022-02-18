# coding=utf-8
"""

这个文件用来定义全局变量和其他属性

"""

import numpy as np

# 定义每个国家对应的世界银行序号
china_index = 40
america_index = 251

# 定义八个指数数组

happiness_index = np.array([])
development_index = np.array([])
resource_index = np.array([])
labor_index = np.array([])
economic_index = np.array([])
education_index = np.array([])
technology_index = np.array([])
population = np.array([])

# 定义科技水平的两个子指标
patents_per_capitan = np.array([])
electricity_per_capitan = np.array([])


# 定义资源水平的三个子指标及其矩阵

population_density_per_city = np.array([])
water_per_capitan = np.array([])
forest_per_capitan = np.array([])


def get_resource_matrix():
    resource_matrix = np.vstack(
        (population_density_per_city, water_per_capitan, forest_per_capitan, energy_per_capitan))
    return resource_matrix


# 定义该国家的年份-指标矩阵
# 此处定义了一个函数，用来实现矩阵的刷新，保证矩阵由该文件自管理

def get_country_matrix():
    country_matrix = np.vstack((happiness_index, development_index, resource_index, labor_index, economic_index,
                                education_index, technology_index, population))
    return country_matrix
