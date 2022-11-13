# 19/20
# -1: your analysis of Manhattan vs. Hamming is somewhat reversed. A key
#  difference is that Hamming distance has a very limited range (from zero to
# the total number of tiles) and so many boards with very "distances" from the
# goal share the same Hamming distance. The Manhattan distance has a much wider
# range and captures more information about the relative positions of the
# tiles.
"""
Gordon Ng , 2031408 
Wednesday , April 6
R. Vincent , instructor 
Assignment 2
"""
# Main program for assignment 2. Your job here is to finish the
# Solver class's __init__ method to solve the puzzle as described
# in the handout.
#
from MinPQ import MinPQ
from Board import Board

import functools
@functools.total_ordering
class Node(object):
    def __init__(self, bd, moves, node):
        '''Construct a new node object. A node contains four attributes:
        1. The board associated with this node (Board).
        2. The number of moves to reach this node (int).
        3. The cost or distance metric for this node (int).
        4. The previous node (Node).
        '''
        self.board = bd         # save the board
        self.moves = moves      # number of moves to reach this board.
        self.cost = bd.distance() # save the distance metric.
        self.previous = node      # save the previous node.
    def __gt__(self, other):
        '''A node is 'greater' than another if the cost plus the
        number of moves is larger. Note that this code will fail
        if 'other' is None.'''
        return (self.cost + self.moves) > (other.cost + other.moves)
    def __eq__(self, other):
        '''Two nodes are equal if the sum of the cost and moves are
        the same. The board itself is ignored.'''
        if self is other:       # comparing to itself?
            return True
        if other is None:       # comparing to None
            return False
        return (self.cost + self.moves) == (other.cost + other.moves)
  
class Solver(object):
    def __init__(self, initial):
        '''Initialize the object by finding the solution for the
        puzzle.'''
        self.__solvable = False
        self.__trace = []       # List of Board objects.
        # This is where your code to solve the puzzle will go!

        queue = MinPQ()
        queue.insert(Node(initial, 0, None))
        
        while not queue.isEmpty():  
            node = queue.delete()   #Picks the minimum node by distance

            for neighbor in node.board.neighbors(): #Finds and appends every board variation of move 1
                if node.previous == None or neighbor != node.previous.board:
                    queue.insert(Node(neighbor, node.moves + 1, node))

            if node.board.solved(): #Runs if the board is solved
                while node != None: #Traces back the solve solution and appends to a list
                    self.__trace.append(node)  
                    node = node.previous
                self.__solvable = True
                break

    def solvable(self):
        '''Returns True if this puzzle can be solved.'''
        return self.__solvable;
  
    def moves(self):
        '''Returns the number of moves in the solution, or -1 if
        not solvable.'''
        return len(self.__trace) - 1 if self.__solvable else -1
  
    def solution(self):
        '''Returns a list of Board objects beginning with the initial Board
        and ending with the solved Board.'''
        return self.__trace.copy()

# Add your main program here. It should prompt for a file name, read
# the file, and create and run the Solver class to find the solution
# for the puzzle. Then it should print the result (see the example output
# file for details).

file = input("What file would you like to open: ")
fp = open(file)
puzzle = ""
for line in fp:     # Adds lines into a string to pass into board class instance
    puzzle += line
board = Board(puzzle)
solver = Solver(board)


print("Minimum moves =" , solver.solution()[0].moves) 
counter = 0
for trace in solver.solution()[::-1]: #Prints out the formatted reverse of the trace list from the Solver class 
    print("Move #" + str(counter))
    counter += 1
    print(trace.board)

