s = input("Enter the string: ")
c = input("Enter the target: ")
found = False 
index = 1
for i in s:
    if i in c and found == False:
        print("found at index " + str(index), end="")
        found = True
    elif i in c and found == True:
        print(" and at index " + str(index), end="")
    index += 1
if found == False:
    print("Not found")