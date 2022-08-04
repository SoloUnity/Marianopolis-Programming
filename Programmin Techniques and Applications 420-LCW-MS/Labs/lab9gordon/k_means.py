''' One of the most common unsupervised learning paradigms is {\em
clustering}. These algorithms automatically assign
each data item in a dataset to a cluster, or class. Generally it is up
to the person using the algorithm to choose the number of clusters.

The simplest approach to clustering is the k-means clustering algorithm
(This 'k' isn't the same 'k' as in 'k'-nearest neighbor). The algorithm 
consists of three essential steps:

  1. Initialize - define $k$ initial mean values for your
    dataset. These can be chosen just by picking $k$ elements of your
    dataset and using their feature vectors as the initial means.
  2. Assignment step - choose the mean value closest in distance to
    the feature vector of an item, and assign that item to that cluster.
  3. Update step - given the new assignment, recompute the means for
    the members.

The assignment step and update step are performed repeatedly, until the
assignment step _converges_, meaning that the none of the items is
assigned to a different class in the assignment.

k-means clustering is an example of an _expectation maximization_ algorithm.
EM algorithms are common in unsupervised learning. To put it as simply as
possible, these algorithms attempt to find the "most likely" choice for some
parameters of a model - in this case, the assignment to clusters or classes.

This is a very simple implementation of k-means clustering. It
closely follows the description above.
'''
from classifier import argmin, distance, normalize_dataset
from random import sample

def k_means(dataset, k):
    '''Automatically assign each item in the dataset to one of 'k' classes.
    
    Initializes by selecting k elements from the dataset randomly.

    Returns 3-tuple containing the number of iterations performed, the 
    dissimilarity, and a list of classification labels. The
    dissimilarity is the total squared distance from each item to its
    class mean (centroid).
    '''
    n_items = len(dataset)            # number of examples.
    n_features = len(dataset[0].data) # features per example.
    #
    # Select the initial 'k' centroids from the actual data.
    #
    centres = sample([item.data for item in dataset], k)
    assignments = [0] * n_items # will hold the class assignments.
    iterations = 0              # counts the total number of iterations.
    while True:
        dissimilarity = 0       # total distance for this iteration.

        ####################################
        # Assignment step - assign each item to the nearest class.
        #
        changes = 0
        for j in range(n_items):
            # COMPUTE ASSIGNMENTS HERE
            # Find assignments[j] such that
            #    distance(dataset[j].data, centres[assignments[j]])
            # is minimized.
            # If any assignment is altered you need to increment 'changes',
            # so that the next iteration will run.
            # Don't forget to compute the dissimilarity!!

            minimumCentre = assignments[j] #0 if untouched
            minimumDistance = distance(dataset[j].data, centres[0]) #Sets a random distance as the minimum distance

            for x in range(len(centres)):
                if distance(dataset[j].data, centres[x]) < minimumDistance:
                    minimumDistance = distance(dataset[j].data, centres[x])
                    minimumCentre = x
            
            if assignments[j] != minimumCentre:
                changes += 1

            assignments[j] = minimumCentre
            dissimilarity += minimumDistance

        if changes == 0:
            break               # algorithm is finished.

        ####################################
        # Update step - recompute the centres.
        #
        # 1. Count the number of items assigned to each class.
        counts = [0] * k
        for c in assignments:
            counts[c] += 1
        #
        # 2. If a class is empty, we are in trouble. This rarely happens,
        # so I have not added code to handle this correctly.
        #
        if not all(counts):
            raise ValueError("Class was empty!")

        # 3. Compute the total vectors for each class and item.
        totals = [list([0] * n_features) for i in range(k)]
        for j in range(n_features):
            for c, item in zip(assignments, dataset):
                totals[c][j] += item.data[j]

        # 4. Divide the total vector by the counts to get the actual
        # mean vector, which is the new centre.
        for i in range(k):
            for j in range(n_features):
                centres[i][j] = totals[i][j] / counts[i]

        iterations += 1

    # Return the number of iterations, the final dissimilarity, and the
    # final assignments.
    return (iterations, dissimilarity, assignments)

def purity(dataset, classes, k):
    '''
    Compute a purity score to evaluate the quality of a clustering.

    The 'dataset' is an existing set of labeled items. The 'classes'
    is a list of integers giving the integer index of the cluster assigned
    to each item. 'k' is the number of clusters.
    
    Technically this is kind of cheating - we are using the labels
    from the original dataset, which we might not have in a "true"
    unsupervised learning situation.

    This is used to compute a 'purity' score for the clustering. A 
    perfect clustering should give a purity of 1, 

    You are not responsible for knowing the algorithm to compute the
    score, but if you are curious there is a good explanation here:
    
    https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-clustering-1.html
    '''
    n = len(dataset)
    m = 0
    for i in range(k):          # iterate over cluster indices.
        counts = {}
        for cls, item in zip(classes, dataset):
            if cls == i:
                label = item.label
                counts[label] = counts.get(label, 0) + 1
        m += max(counts.values()) # count number of items in majority.
    return m / n

