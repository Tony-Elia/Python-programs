while True:
    start = int(input("Write the start value \n"))
    end  = int(input("Write the end value \n"))
    if start >= end :
        print("Start value should be less than the end value")
    else :
        break
print("Do you want to search for even orr odd values?")
searchKey = int(input("1: Even / 2: Odd \n write 1 or 2 \n"))
result = []
for i in range(start, end + 1):
    if searchKey == 1:
        if i % 2 == 0:
            result.append(i)
    elif searchKey == 2:
        if i % 2 != 0:
            result.append(i)
    else:
        result = ["Invalid Input"]
print(result)