# Use Python's built-in secure hashing module.
import hashlib

fp = open('dictionary-yawl.txt')
words = {word.strip().lower() for word in fp}
fp.close()

# Create the "rainbow table", which is just a dictionary that maps
# the hex digest to a word.

rt = {}
for word in words:
    hash = hashlib.sha256()    # Create a new sha256() hash object.
    # string must be 'encoded' as a byte string before passing it to
    # the update() method.
    hash.update(str.encode(word))
    key = hash.hexdigest()
    assert key not in rt        # Crash if there are duplicates.
    rt[key] = word              # Add an entry to the rainbow table.
# open external file
fp = open('passwords.txt')

# TODO: Use the "rainbow table" to decrypt the passwords.
decrypted = dict()
for line in fp:
    line = line.strip().split()
    decrypted[line[0]] = rt.get(line[0])

print("Decrypting 'unsalted' passwords:")

# TODO: Now decrypt the salted passwords.
# To pass the salt value from the file to the hash function, you need
# to convert the Python integer to a value with two bytes. You can do this
# by using the "to_bytes()" method of the int() type. For this example,
# x.to_bytes(2, 'little') will convert the integer x into a 2-byte,
# little-endian representation. You will need to pass this value to the
# hash function's update method after you pass the encoded string value.
# 

for line in fp:
    line = line.strip().split()
    if len(line) == 2:
        salt = line[1]
        for i in words:
            hash = hashlib.sha256()
            hash.update(salt.to_bytes(2, i))
            if hash.hexdigest() == line[0]:
                decrypted[line[0]] = i
                break
print("Decrypt:")    

#2
class Rectangle(object):
    def __init__(self, topy,leftx,bottomy, rightx):
        self.top = int(topy)
        self.left = int(leftx)
        self.bottom = int(bottomy)
        self.right = int(rightx)

    def __hash__(self):
        y = (self.bottom ^ self.top) 
        for _ in range(8):     
            if (y % 2) != 0:   
                y = y >> 1
                y =self.left * y ^ self.right 
            else:
                y = y >> 1
    
        return self.top*self.bottom + self.right*self.left

    def __eq__(self,other):
        return hash(self) == hash(other)