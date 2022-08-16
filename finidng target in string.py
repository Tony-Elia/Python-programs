def check() :
    s2 = input("Write the string\n")
    s1 = input("write the target\n")
    all_found = False

    for x in s1:
        for y in s2:
            if x == y:
                all_found = True
                break
            else: 
                all_found = False
        if all_found == False:
            break
    
    print(all_found)

def checkStr():
    y = input("Write the string\n")
    x = input("Write the target\n")
    x = list(x)
    found = False
    for i in x:
        if i in y:
            found = True
        else:
            found = False
        if found == False:
            break
    print(found)

def starter():
    v = input("Version 1 or Version 2 (1/2)")
    v = str(v)
    if v == "1":
        check()
    elif v == "2":
        checkStr()
    else:
        print("Please, Write 1 or 2 only")
        starter()
starter()
