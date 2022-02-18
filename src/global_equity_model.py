# coding=utf-8
"""

本函数为全球公平模型的具体实现

"""

import logging
import numpy as np
import data_manager


def modify_model():
    logging.info('开始构建全球公平模型')
    data_manager.global_equity_model_init()
    logging.debug('载入初始数据')
