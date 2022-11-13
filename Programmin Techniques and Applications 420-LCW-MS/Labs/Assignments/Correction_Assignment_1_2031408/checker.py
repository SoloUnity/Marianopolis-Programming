# Gordon Ng, 2031408
# R. Vincent , instructor
# Advanced Programming , section 1 
# Assignment 1, Exercise 2

class stack(list):
    '''A very simple stack class derived from a Python list.'''
    def isEmpty(self):
        '''return True if the stack is empty.'''
        return self == []

    def push(self, value):
        '''Add a value to the stack.'''
        self.append(value)

    def top(self):
        '''Check the top of the stack, without changing the stack.'''
        if self.isEmpty():
            raise ValueError("Stack underflow")
        return self[-1]

    def pop(self):
        '''Remove the top of the stack, returing the value found there.'''
        if self.isEmpty():
            raise ValueError("Stack underflow")
        return super().pop()


       
inputFile = str(input("File name: "))
file = open(inputFile)
stack = stack()
brackets = [["(", "[", "{"],[")", "]", "}"]]    # List of brackest to check
missingList = []
left = brackets[0]
right = brackets[1]
error = 0                                       # Counts the number of errors 
count = 0                                       # Counts the number of tools
for line in file:
    count += 1
    tempData = list(line)                       # Splits each line into individual characters
    for character in tempData:
        try:
            if character in left:
                missingList.append(count)       # Appends potential missing bracket line count
                stack.push(character)
            elif character in right: 
                if (character == ")" and stack.top() == "(") or (character == "}" and stack.top() == "{") or (character == "]" and stack.top() == "["):
                    missingList.pop()           # Removes potential missing bracket line count
                    stack.pop()
                else:
                    missingList.pop()
                    print("Mismatched bracket at line", count , ".")
                    error += 1                  # Adds error count
        except:
            print("Extra bracket at line", count , ".")
            error += 1                          # Adds error count

if len(missingList) != 0:                       # Prints all line counts of missing brackets
    for item in missingList:
        print("Missing bracket at", item)
elif error == 0:
    print("All tests passed")

















    

