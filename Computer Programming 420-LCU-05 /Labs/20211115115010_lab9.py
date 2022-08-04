def exercise1():
    #1
    colours = {'red':10, 'blue':20, 'green':30 }
    print(len(colours), colours)
    #3 {'red': 10, 'blue': 20, 'green': 30}
    #It is the same order

    #2
    colours['yellow'] = 40
    colours['orange'] = 50
    print(len(colours), colours)

    #3
    for x in colours:
        print(x)
    #It prints the full dictionary in order

    #4
    for x in colours:
        print(x, colours[x])

    for item in colours.items():
        print(item)

    for key, val in colours.items():
        print(key, val)

    #5
    print(max(colours.values()))
    print(max(colours))

    #6
    print(sum(colours.values()))

    #7
    for value in colours.values():
        value += 1

    #8
    for x in sorted(colours):
        print(x)

    #9
    for x in sorted(colours.items()):
        print(x)
    #it sorts them alphabetically through lexicographic measures

    #10
    def pink():
        '''Traceback (most recent call last):
          File "/Users/gordonng/Documents/Coding/Python/Cegep/Labs/lab9/main.py", line 49, in <module>
            print(colours['pink'])
        KeyError: 'pink'
        '''
        print(colours['pink'])

    #11
    print(colours.get('red'))
    print(colours.get('pink'))
    #10
    #None

    #12
    print(colours.get('red', 1099), colours.get('pink', 1099))
    #10 1099
    #Since it couldnt find pink, it returned 1099

    #13

    x = dict()
    y = x
    z = x.copy()
    print(x is y, x is z)
    print(x == y, x == z)
    z[2.0] = 'two'
    y[3.14159] = 'pi'
    y[2.71828] = 'e'
    print(x, z)
    y.clear()
    print(x, z)

    #x is copied to z, it is the same as y but is is not the same as z, despite containg the same information
    #x is also related to y, so when y is cleared, it is as well

    #14
    x = {'a': 10, 'c': 11, 'z': 12 }
    y = {'z': 12, 'a': 10, 'c': 11 }
    print(x == y)
    y['z'] -= 1
    print(x == y)
    #A True/False is printed. Other statements do not work. they also dont make sense as its a dictionary with randomly ordered keys

    #15
    from string import ascii_lowercase
    letters = dict.fromkeys(ascii_lowercase, 0)
    print(letters)
    colours = ('red', 'green', 'blue', 'black', 'magenta')
    cdict = dict.fromkeys(colours, 0.0)
    print(cdict)

    #16
    keys = [2001, 2006, 2011, 2016]
    values = [1039534, 1620693, 1649519, 1704694]
    pop = dict(zip(keys, values))
    print(pop)

    #17
    def slices():
        print(pop[0:2])
        #you cant as its unhashable? Also because they arent defined on a position like a list but based on their values/keys?

    #18
    print(sorted(pop))
    #yes you can as you can sort the entries on size

    #19
    print(2001 in pop, 2002 in pop)
    print(1649519 in pop)
    print(1649519 in pop.values())

    #20
    print(dict(zip(pop.values(),pop.keys())))

def exercise2():
    #1
    fp = open('/Users/gordonng/Downloads/lab9/alice.txt')
    entireText = fp.read()
    bankOfLetters = {}
    for letter in entireText.lower():
        if letter.isalpha():
            if letter in bankOfLetters:
                bankOfLetters[letter] += 1
            else:
                bankOfLetters[letter] = 1
    fp.close()
    for val,key in sorted(bankOfLetters.items()):
        print(val,key)

def exercise3():
    def clean(word):
        '''Strip away leading or trailing punctuation and convert to lower case.'''
        return word.strip('?!@#$%^&*();:.,\'\"-').lower()

    def get_second(x):
        '''Returns the second element of sequence 'x'.'''
        return x[1]

    fp = open('/Users/gordonng/Downloads/lab9/alice.txt')
    entireText = fp.read()
    bankOfWords = {}
    for word in entireText.lower().split():
        if "--" in word:
            word = clean(word).split("--")[0]
        if clean(word) in bankOfWords:
            bankOfWords[clean(word)] += 1
        else:
            bankOfWords[clean(word)] = 1
    fp.close()
    ascendingItems = sorted(bankOfWords.items(), key=get_second, reverse=True)
    for val,key in ascendingItems[:10]:
        print(val,key)
exercise3()