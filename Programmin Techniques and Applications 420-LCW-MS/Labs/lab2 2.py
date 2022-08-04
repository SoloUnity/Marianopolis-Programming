def my_abs(x):
    return -x if x < 0 else x

def is_palindrome(x):
    return True if len(x) <= 1 else (x[0] == x[-1] and is_palindrome(x[1:-1]))

def power(x,y):
    result = [value ** y for value in x ]
    return result

def zeroes(m,n):
    row = [[0 for c in range(n)] for r in range(m)]
    return row

factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)

add_vectors = lambda x,y: [(a + b) for a,b in zip(x,y)]

all_even = lambda x: all([False if v % 2 != 0 else True for v in x ])

s = set()
for n in range(1, 10+1):
    result = 0
    for x in range(1, n+1):
        result += x
        s.add(result)

n = 10
r = []
for i in range(n):
    for j in range (i + 1, n):
        r.append((i,j))

p = 101 
q = 19 
r = 0
def simple_function(): 
    r=1
    r = (r + p) % q
    return r

def simple_function2(): 
    r = (r + p) % q
    return r
#Gets an error

def simple_function3(): 
    global r
    r = (r + p) % q
    return r
#Prints successfully

print(simple_function3())
print(p, q, r)

for _ in range(5):
    print(simple_function3())

#12
#18
#5
#11
#17

#2a)
#Number of calls: 4
#6
#Number of calls: 1
#7
#Number of calls: 4
#2
#Number of calls: 5
#15
#Number of calls: 5
#-1
#Number of calls: 5
#-1
#Number of calls: 6
#-1

#2c) Error
#2d) Calls not defined