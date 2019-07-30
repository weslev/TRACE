startList = []
listPlus2R = []
listPlus2 = []
listDiv3 = []
listEvOd = []

# Creates and prints a list from 1 to 10
startList = [x for x in range(1, 11)]
print(startList)

# Creates and prints a list from 1 to 10 with 2 added to all numbers (regular way)
for x in range(1,11):
    listPlus2R.append(x)
print(listPlus2R)
    

# Creates and prints a list from 1 to 10 with 2 added to all numbers
listPlus2 = [x + 2 for x in startList]
print(listPlus2)

# Creates and prints a list from 1 to 10 with all numbers cubed
listCubed = [x**3 for x in startList]
print(listCubed)

# Creates and prints a list from only numbers divisible by three from a range of 1 to 10 and adds 3 to all numbers in the list
listDiv3 = [x + 3 for x in startList if not(x % 3)]
print(listDiv3)

# Creates a list from 1 to 10 and then prints which numbers are even and which are odd
listEvOd = ["Even" if not(x % 2) else "Odd" for x in startList]
print(listEvOd)
