import numpy as np
from sklearn.cluster import KMeans


def kmeans(k):
    num_clusters = k
    km_cluster = KMeans(n_clusters=num_clusters, max_iter=300)

    ll = []
    f = open('./output/animal.txt', 'r')
    for ff in f:
        line = ff.split(',')
        temp = [float(l) for l in line]
        ll.append(temp)

    X = np.array(ll)
    # print(X.shape) (30, 2048)
    km_cluster.fit(X)
    return list(km_cluster.labels_)
