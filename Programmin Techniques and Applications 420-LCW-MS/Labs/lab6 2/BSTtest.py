# Basic BST testing code. Any assertion error indicates a problem.
#
from BST import BST
a = BST()
assert not a and len(a) == 0
try:
    y = a.get('x')
except KeyError as e:
    assert str(e) == "'x'"
else:
    raise Exception("KeyError not generated!")
s = 'cadbe'
for i, c in enumerate(s):
    a.put(c, i * 100)
assert a.depth() == 3
assert a and len(a) == len(s)
for i, c in enumerate(s):
    assert c in a and a.get(c) == i * 100
a.put('k', 0)
assert 'k' in a and a.get('k') == 0
assert len(a) == len(s) + 1
try:
    y = a.get('z')
except KeyError as e:
    assert str(e) == "'z'"
else:
    raise Exception("KeyError not generated!")


# ADD TESTS FOR YOUR NEW FUNCTIONALITY AFTER THIS LINE.

bst = BST()
bst.put(0, "a")
bst.put(1, "b")
bst.put(2, "c")
bst.put(3, "d")
bst.put(4, "e")

print(bst.maxKey(), bst.minKey())
print("All tests passed.")

print(bst)

# This code implements the performance testing you should comment on.
# For each value of n, it creates M different trees by randomizing the order
# of the integers from 0..n-2, then it computes the minimum, maximum, and mean
# depth of the M different trees.
#
from random import shuffle
M = 100 # number of trees to create per value of N
n = 16  # starting number of nodes
print("N   MIN MAX  MEAN")
while n < 512:
    stats = []
    data = list(range(n-1)) # generate a list of N-1 ints from 0 to N-2.
    for i in range(M):      # create M different trees
        bst = BST()             # create empty BST
        shuffle(data)           # randomize the data
        for x in data:          # build the tree
            bst.put(x)
        stats.append(bst.depth())
    print('{:3d} {:3d} {:3d} {:5.2f}'.format(n-1, min(stats), max(stats), sum(stats)/M))
    n *= 2

