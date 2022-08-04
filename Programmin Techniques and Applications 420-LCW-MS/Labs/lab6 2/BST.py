# Template file for lab 6.
#
class BST(object):
    '''Class that represents a Binary Search Tree.'''
    class Node(object):
        '''A single node within a BST.'''
        def __init__(self, key, val = None):
            self.key = key
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        '''Construct an empty binary search tree.'''
        self.root = None

    def __len__(self):
        '''Compute the size (number of key/value pairs) of the BST.'''
        return BST._size(self.root)

    def __bool__(self):
        '''Convert a BST into a Boolean value. Like most Python collections,
        the logic here is that any non-empty BST evaluates as True.'''
        return self.root != None

    @staticmethod
    def _size(node):
        '''Compute the size of the tree below this node.'''
        if node == None:
            return 0
        else:
            return 1 + BST._size(node.left) + BST._size(node.right)

    def put(self, key, val = None):
        '''Insert the key-value pair into the BST.'''
        def _put(node, key, val):
            '''Helper function for the public put() method.'''
            if node == None:
                return BST.Node(key, val)
            elif key < node.key:
                node.left = _put(node.left, key, val)
            elif key > node.key:
                node.right = _put(node.right, key, val)
            else:
                node.val = val
            return node
        self.root = _put(self.root, key, val)

    @staticmethod
    def _get(node, key):
        '''Helper function for get() and contains(). This is not local
        so that it can be shared between the two public methods.

        Returns the node associated with the key, if present. Otherwise
        returns None.
        '''
        while True:
            if node == None:
                return None
            elif key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node

    def maxKey(self):
        node = self.root
        while True:
            if node.right == None:
                return node.key
            else:
                node = node.right

    def minKey(self):
        node = self.root
        while True:
            if node.left == None:
                return node.key
            else:
                node = node.left

    def traverse(self, node, func):
        if node == None:
            return
        self.traverse(node.left, func)
        func(node.key, node.val)
        self.traverse(node.right, func)

    def __repr__(self):
        tempList = []
        def appendToList(key, val):
            tempList.append((val, key))  
        self.traverse(self.root, appendToList)

        y = ""
        for item in tempList:
            if item != tempList[0]:
                y += ", "
            for x in item:
                if x == item[1]:
                    y += ":"
                if x == item[0]:
                    y = y + "'" + str(x) + "'"
                else:
                    y += str(x)
        return "{" + y + "}"



    def get(self, key):
        '''Get the value associated with the given 'key'.

        Raises KeyError() if the key is not present in the BST.
        '''
        x = BST._get(self.root, key)
        if x == None:
            raise KeyError(key)
        else:
            return x.val

    def __contains__(self, key):
        '''Implements the 'in' operator.'''
        return BST._get(self.root, key) != None

    def depth(self):
        '''Return the maximum depth of the tree.'''
        def _depth(node):
            '''Compute the depth of the tree below this node.'''
            if node == None:
                return 0
            else:
                return 1 + max(_depth(node.left), _depth(node.right))
        return _depth(self.root)

