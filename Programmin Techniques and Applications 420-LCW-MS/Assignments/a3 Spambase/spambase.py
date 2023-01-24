from extra_trees import extra_trees # suggestion!
from classifier import data_item, normalize_dataset
from random import shuffle

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
