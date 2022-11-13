"""
Gordon Ng , 2031408 
Wednesday , May 5
R. Vincent , instructor 
Assignment 3
"""

# 19/20
# -1 need to use normalization with kNN

from extra_trees import extra_trees # suggestion!
from classifier import data_item, normalize_dataset
from random import shuffle
from knnclassifier import knnclassifier

fp = open('spambase.data')
dataset = []
for line in fp:
    fields = line.split(',')
    data = [float(x) for x in fields[:-1]]
    label = int(fields[-1])
    dataset.append(data_item(label, data))

print("Read {} items.".format(len(dataset)))
print("{} features per item.".format(len(dataset[0].data)))

# Add your code here...
length = len(dataset)
fourFifths = round((length/5)*4)
TN1, FN1, FP1, TP1 = 0, 0, 0, 0
TN2, FN2, FP2, TP2 = 0, 0, 0, 0
settings = [[15, 10, 2, 1], [15, 10, 4, 2], [20, 10 ,2, 3], [15, 13, 2, 4], [15 ,10 , 4, 5]]
iteration = 1
for setting in settings:
    for fold in range(5):
        shuffle(dataset)
        trainingSet = dataset[:fourFifths]
        testSet = dataset[fourFifths:]
        extraTrees = extra_trees(M = setting[0], K = setting[1], Nmin = setting[2])
        extraTrees.train(trainingSet)
        knn = knnclassifier(K = setting[3])
        knn.train(trainingSet) 

        for item in testSet:
            prediction = extraTrees.predict(item.data)
            if prediction == 0 and item.label == 0:
                TN1 += 1
            elif prediction == 0 and item.label == 1:
                FN1 += 1
            elif prediction == 1 and item.label == 0:
                FP1 += 1
            elif prediction == 1 and item.label == 1:
                TP1 += 1

        for item in testSet:
            prediction = knn.predict(item.data)
            if prediction == 0 and item.label == 0:
                TN2 += 1
            elif prediction == 0 and item.label == 1:
                FN2 += 1
            elif prediction == 1 and item.label == 0:
                FP2 += 1
            elif prediction == 1 and item.label == 1:
                TP2 += 1

    print("{}) {:11s} | TPR: {:5f} | FPR: {:5f} | M: {} | K: {} | Nmin: {}".format(iteration, "extraTrees", TP1/(TP1 + FN1), FP1/(FP1 + TN1), setting[0], setting[1], setting[2]))
    print("{}) {:11s} | TPR: {:5f} | FPR: {:5f} | K: {}".format(iteration, "knn", TP2/(TP2 + FN2), FP2/(FP2 + TN2), setting[3]))
    iteration += 1

#extraTrees Classifier
#Changing the values of M, K and Nmin may have a slight impact, however, even if it does, it is negligible and within margin of error. They all have roughly the same TPR and FPR.

#knn Classifier
#There is a strong correlation between higher TPR and a lower K, while the FPR is virtually identical no matter the K.
        







    
