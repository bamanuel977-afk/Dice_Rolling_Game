import random

print("===============================")
print("wellcome to our dice rolling game!")
print("====================================")
choice=input("you want to play (y/n)?")
while(choice=='yes'):
    num=random.randint(1,6)

    if num==1:
        print("-------------")
        print("             ")
        print("      0      ")
        print("             ")
        print("-------------")
    elif num==2:
        print("-------------")
        print("             ")
        print("    0  0     ")
        print("             ")
        print("-------------")
    elif num==3:
        print("-------------")
        print("     0       ")
        print("    0  0     ")
        print("             ")
        print("-------------")
    elif num==4:
        print("-------------")
        print("   0    0    ")
        print("             ")
        print("   0    0    ")
        print("-------------")
    elif num==5:
        print("-------------")
        print("      0      ")
        print("  0      0   ")
        print("  0      0   ")
        print("-------------")
    else:
        print("-------------")
        print("   0     0   ")
        print("   0     0   ")
        print("   0     0   ")
        print("-------------")

    choice = input("you want to play (y/n)?")
    if choice=='No':
        exit()
