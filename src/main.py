# coding=utf-8

"""

主类

"""

import logging
import global_equity_model

if __name__ == "__main__":
    logging.info('开始执行程序')
    global_equity_model.modify_model()
    logging.info('成功构建全球公平模型')