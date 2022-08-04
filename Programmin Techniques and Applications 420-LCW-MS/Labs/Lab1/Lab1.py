#Question 1.1
def nDigits(x):
    if x < 10:
        return 1
    return 1 + nDigits(x/10)

#Question 1.2
def subsets(ls):
    for i in range(2**(len(ls))):
        newSubset = []
        k = 0
        j = i
        while j != 0:
            if j % 2 == 1:
                newSubset.append(ls[k])
            j //= 2
            k += 1
        print(newSubset)
    

#Question 1.3
def flatten(x):
    if len(x) == 0:
        return[]
    elif type(x[0]) == list:
        return flatten(x[0]) + flatten(x[1:])
    else:
        return [x[0]] + flatten(x[1:])




    
        
