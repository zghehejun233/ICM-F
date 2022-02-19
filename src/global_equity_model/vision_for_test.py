# coding=utf-8
"""

本函数用来在分析时展示数据

"""

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import seaborn

X = pd.read_csv("/data/global_equity_data/全球均衡模型最终得分.csv")
# Using the elbow method to find the optimal number of clusters
dots_information = X.values
dots_information_ = np.delete(dots_information, [1, 2, 3, 4, 5, 7, 9, 10, 11, 12, 13, 15, 18, 19, 20, 22, 23, 24],
                              0).transpose()
figure = plt.figure(1, figsize=(19, 11))
plt.plot(dots_information_)
plt.show()
