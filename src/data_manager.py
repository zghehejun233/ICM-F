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


# 清洗数据
def global_equity_model_data_clean():
    pass

