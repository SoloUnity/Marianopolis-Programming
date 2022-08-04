listOfBids = input(str("Enter your bids seperated by spaces: "))
list1 = listOfBids.split(" ")
for index in range(len(list1)):
	list1[index] = float(list1[index])
list1.sort()
print(list1[-1], list1[-2])