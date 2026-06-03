# take the fruits names from user and add it to the list 

fruits=[]
a=int(input("how many names u want to enter : "))

for i in range (0,a):
    f1=input("enter fruite : ")
    fruits.append(f1)

print("you entered : \n ")
print(fruits)
