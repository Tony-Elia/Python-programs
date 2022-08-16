###############################
#مسااااااااااااااااااااااااء
#العسسللللللللللللللللللللللل
#This file is copyrighted to Youssef and Tony ©
###############################
print("#" * 20)
print("--", "Youssef", "&", "Tony", "--")
print("#" * 20)

print()
print("For 1st [v] Press => 0 & For 2nd [v] => 1")
version = input()

def coutMe1() :
    fill = input("Fill")
    lf = len(fill)
    width = int(input("Width"))
    height = int(input("Height"))
    print(fill * (width + 2))
    for i in range(0, height) :
        print(fill, " " * (width - (lf * 2)), fill)
    print(fill * (width + 2))


def coutMe() :
    fill = input("Fill")
    fl = len(fill)
    width = int(input("Width"))
    height = int(input("Height"))
    abas = fl
    abasL = width + fl - abas

    print(fill * (width + 2))
    for i in range(0, height) :
        print(fill, end="")
        
        for a in range(fl, width + fl):

            if abas == abasL and abas == a:
                print("x", end="")
            elif abas == a :
                print("\\", end="")
            elif abasL == a:
                print("/", end="")  
            else :
                print(" ", end="")      
        abas +=1
        abasL -=1
        print(fill, end="\n")
        # print("", end="\n")
    print(fill * (width + 2))

if version == "0" :
    coutMe1()
else :
    coutMe()
