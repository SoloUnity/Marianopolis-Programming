# Example hash functions. These are all very simple, non-cryptographic
# hash functions. They make use of some Python operators that might not
# be familiar:
#
#     x >> y - right bit shift.
#        "Shifts" the binary pattern of x right by y bit positions.
#
#     x & y  - bitwise and
#        If a bit is "1" in both x and y, it will be "1" in the result.
#
#     x ^ y - bitwise exclusive or
#        If a bit is "1" in either x or y, but not in both, it will
#        be "1" in the result.
#
#     ~x    - unary bitwise not
#        The result will have the exact opposite bit pattern as x,
#        i.e. all 1's become 0's and all 0's become 1's.
#
import sys

# Create a bitmask to force numbers to remain in the appropriate
# word size. This is especially needed in Python because these
# calculations would normally use Python's unlimited integer size.
#
MASK64 = 2 ** 64 - 1
MASK32 = 2 ** 32 - 1

CRC32POLY = 0xedb88320
CRC32MASK = 0xffffffff          # same as 'MASK32' above.

def crc32(key):
    '''Old-fashioned CRC-32 algorithm from 1975, use to check
    integrity of Ethernet packets. Assumes 8-bit characters.
    This is an intentionally inefficient but simple implementation,
    efficient implementations make use of a 256-word lookup table
    of memoized values.'''
    y = CRC32MASK
    for c in key:
        y = (y ^ ord(c)) & CRC32MASK
        for k in range(8):      # for every bit
            if (y % 2) != 0:    # lowest bit set?
                y = y >> 1
                y = y ^ CRC32POLY
            else:
                y = y >> 1
            y &= CRC32MASK
    return (~y & CRC32MASK)
        
def djbx33a(key):
    '''Compute the hash function for a string 'key'.
    This is a version of the well-known DJBX33A algorithm
    "Daniel J. Bernstein, Times 33 with Addition".
    Note that the hash function makes use of two prime numbers.
    Using prime numbers reduces the probability of hash collisions.
    '''
    hash = 5381
    for c in key:
        hash = (hash * 33 + ord(c)) & MASK32
    return hash

FNV64prime = 0x00000100000001B3
FNV64basis = 0xCBF29CE484222325

def fnv(key):
    '''The 64-bit Fowler-Noll-Vo hash function, a version of which 
    used to be the standard Python hash function.'''
    x = FNV64basis
    for c in key:
        x = (FNV64prime * (x ^ ord(c))) & MASK64
    return x

def simple32(key):
    '''Simple 32-bit hash function, similar to original functions
    used in Java.'''
    x = 103
    for c in key:
        x = ((x * 31) + ord(c)) & MASK32
    return x

if __name__ == "__main__":
    print(djbx33a("Ez"), djbx33a("FY")) # hash collision
    print(djbx33a("apple"))
    print(djbx33a("banana"))
    
    def find_collisions(funcs, words):
        '''Function to find any words that have the same hash value for
        any of the given hash functions.'''
        dicts = [dict() for fun in funcs]
        for word in words:
            for dc, fn in zip(dicts, funcs):
                hval = fn(word)
                if hval not in dc:
                    dc[hval] = []
                    dc[hval].append(word)
            for dc, fn in zip(dicts, funcs):
                n_count = sum(len(dc[key]) > 1 for key in dc)
                print(fn.__name__, 'has', n_count, "collisions:")
                for key in dc:
                    if len(dc[key]) > 1:
                        print(' ', key, dc[key])

    from statistics import stdev
    def check_distribution(funcs, words, M):
        '''Checks the occupancy distribution of hash functions for a particular
        size M.'''
        lists = [[0 for i in range(M)] for fn in funcs]
        for word in words:
            for ls, fn in zip(lists, funcs):
                hval = fn(word) % M
                ls[hval] += 1
        print("Arranged", len(words), "words in", M, "bins.")
        for ls, fn in zip(lists, funcs):
            print(fn.__name__, min(ls), max(ls), stdev(ls))
        
    fp = open('dictionary-yawl.txt')
    words = [word.strip().lower() for word in fp]
    fp.close()

    find_collisions([simple32, crc32, djbx33a, fnv], words)
    check_distribution([simple32, crc32, djbx33a, fnv], words, 30001)
