# Starting point for Lab 9.
#
from datasets import *
from classifier import normalize_dataset
from k_means import *

# Read and cluster the three datasets. All three chosen datasets
# are known to have three classes.
#
datasets = {
    'iris': read_iris_dataset(),
    'seeds': read_seeds_dataset(),
    'wine': read_wine_dataset()
}

N_CLASSES = 3

# Exercise 2
for name, dset in datasets.items():
    dset = normalize_dataset(dset)

    results = []
    for _ in range(10):
        iter, dis, cls = k_means(dset, N_CLASSES)
        results.append((iter, dis, cls))

    top = min(results, key = lambda x: x[1])

    iter, dis, cls = top
    p = purity(dset, cls, N_CLASSES)
    print(f"{name}: iterations {iter:d}, dissimilarity {dis:.2f}, purity {p:.2f}")

