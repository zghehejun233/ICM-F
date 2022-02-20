# coding=utf-8
"""

本函数用来在分析时展示数据

"""

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import seaborn

# Importing the dataset
dataset = pd.read_csv('/Users/guosurui/Documents/git_code/ICM-F/data/global_equity_data/逐年各个指标2013.csv')
X = dataset.iloc[:, :].values

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, max_iter=300, n_init=10, init='k-means++', random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Applying the k-means to the mall dataset
kmeans = KMeans(n_clusters=3, max_iter=300, n_init=10, init='k-means++', random_state=0)
y_kmeans = kmeans.fit_predict(X)

# Visualizing the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='类型I')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='类型II')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='类型III')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='重心')
plt.title('国家类型聚类')
plt.legend()
plt.show()
print(' ')