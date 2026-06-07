import random

choice = input("Enter your choice rock : r , paper : p , scessor : s - ")
computer = random.choice(["r", "p", "s"])
print("computer choice : ",computer)
if(choice not in ['r','p','s']):
    print("invalid choice")
elif(choice == computer):
    print("Draw")

elif(choice == "r" and computer == "s") or \
     (choice == "p" and computer == "r") or \
     (choice == "s" and computer == "p"):
    print("user wins")

else:
    print("computer wins")
