def my_len(x):
    length = 0
    for item in x:
        length += 1
    return length
assert my_len([]) == 0
assert my_len("Marianopolis") == 12
assert my_len((1, 5, 9, 2)) == 4

def my_count(my_list, value):
    amount = 0
    for item in my_list:
        if item == value:
            amount += 1
    return amount
x = [1, 2, 3, 3]
assert my_count(x, 1) == 1
assert my_count(x, 3) == 2
assert my_count(tuple(x), 4) == 0

def my_find(my_list, value):
    position = 0
    for item in my_list:
        if value not in my_list:
            return -1
        elif item != value:
            position += 1
        elif item == value:
            return position

x = ["orange", "red", "yellow", "green"]
assert my_find(x, "blue") == -1
assert my_find(x, "green") == 3
assert my_find(tuple(x), "orange") == 0

def product(my_list):
    final = 1
    if len(my_list) == 0:
        return 1
    else:
        for item in my_list:
            final = final * item
        return final
assert product([]) == 1
assert product([3]) == 3
assert product([3, 7, 5]) == 105
assert product([2, -5, 7, 3, 19]) == -3990

def is_cdn_postal_code(st):
    if st[0] == "Z" or len(st) != 7:
        return False
    elif st[0].isalpha() and st[1].isdigit() and st[2].isalpha() and st[3] == " " and st[4].isdigit() and st[5].isalpha() and st[6].isdigit():
        return True
    else:
        return False
assert is_cdn_postal_code("H2Y 1B5")
assert is_cdn_postal_code("S7K 1L9")
assert is_cdn_postal_code("X1A 1E5")
assert is_cdn_postal_code("Y1A 1A4")
assert not is_cdn_postal_code("H4T 16Z")
assert not is_cdn_postal_code("Y1A1A5")
assert not is_cdn_postal_code("Z4A 2N5")

def is_sorted(x):
    errorCheck = 0
    for value in range(1,len(x)):
        if x[value-1] <= x[value]:
            errorCheck = 1
        else:
            errorCheck = 0
    if errorCheck == 1 or len(x) == 0 or len(x) == 1:
        return True
    else:
        return False

assert is_sorted([])
assert is_sorted([2])
assert is_sorted([1, 2])
assert not is_sorted([2, 1])
assert is_sorted([1, 100, 110, 2000, 2000, 123456, 10**10, 10**19])
assert not is_sorted([1, 2, 3, 4, 4, 4, 6, 5])

def my_split(a_str):
    tempList = []
    newStart = 0
    for value in range(len(a_str)):
        if a_str[value] == ' ':
            if len(a_str[newStart:value]) > 0:
                tempList.append(a_str[newStart:value])
                newStart = value + 1
            else:
                newStart = value + 1
        elif value == (len(a_str)-1):
            tempList.append(a_str[newStart:value+1])
    print(tempList)
    return tempList
assert my_split("") == []
assert my_split(" ") == []
assert my_split("To be or not to be") == ['To', 'be', 'or', 'not', 'to', 'be']
assert my_split(" aardvark  marmoset   zebra ") == ['aardvark', 'marmoset', 'zebra']
assert my_split("    10 201 -12  109") == ['10', '201', '-12', '109']
