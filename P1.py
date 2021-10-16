Mnum = 8
num = 1
for i in range(6) :
    Tnum = int(input("Enter Your Guess : "))
    if Tnum == Mnum :
        print("Congratulations You Won!!!")
        num = 0
    elif Tnum != Mnum :
        print("You were wrong try again :(")
        num = 0
    if Tnum < Mnum :
        print("Guess a number higer than",Tnum)
        num = 0
    if Tnum > Mnum :
        print("Guess a number lower than",Tnum)
        num = 0



