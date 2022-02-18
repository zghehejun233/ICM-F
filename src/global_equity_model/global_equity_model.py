# coding=utf-8
"""

本函数为全球公平模型的具体实现

"""

import logging
import src.data_manager as data_manager
import src.global_equity_model.global_equity_measure as global_equity_measure


def modify_model():
    logging.info('开始构建全球公平模型')
    data_manager.global_equity_model_init()
    logging.debug('载入初始数据')
    data_manager.global_equity_model_data_clean()
    logging.debug('进行数据清洗')
    global_equity_measure.measure_indexes()
    logging.debug('计算各个因子')
