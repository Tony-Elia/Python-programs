import random
target = int(random.randint(0, 20))
c = 0; b = 0

while b == 0: 
    print("Enter a number between 0 to 20")
    x  = int(input('Enter your guess: '))
    if x < target:
        print("Too low")
        c += 1
    elif x > target:
        print("Too high")
        c += 1
    else:
        c += 1
        if c == 1:
            print("Awesome you got it from the first time!")
        else:
            print('Congratulations you got it with ' + str(c) + ' tries')
        b = 1
        


