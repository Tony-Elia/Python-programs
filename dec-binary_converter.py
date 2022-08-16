def bin_to_dec():
    bin = input("Enter the binary code\n")
    bin = bin[::-1]
    sum = 0
    i = 0
    for x in bin:
        sum += (2 ** (i)) * int(x)
        i += 1
    print(sum)

def dec_to_bin():
    dec = int(input("Enter the decimal number\n"))
    bin = ""
    breakLoop = False
    if dec == 0:
        print("0", end = "")
        breakLoop = True
    while breakLoop == False:
        if dec == 0:
            breakLoop = True
            break
        elif dec % 2 == 0:
            bin += "0"
        else:
            bin += "1"
        dec = int(dec / 2)
    bin = bin[::-1]
    print(bin)

def opening():
    ans = input("Enter 1 for Decimal to Binary\nEnter 2 for Binary to Decimal\n")
    if  ans == "1":
        dec_to_bin()
    elif ans == "2":
        bin_to_dec()
    else:
        print("Invalid input")
        opening()
opening()