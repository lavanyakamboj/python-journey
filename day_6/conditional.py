# if , else , elif - is used for the conditional statements 

# write programe to enter age from user - less then zero - print invalid , less then 18 - cant vode , 18> - can vote 

a= int(input("enter age of the student : "))

if(a<=0):
    print("invalid age ")
elif(a>0 and a<18):
    print("cant vote")
else:
    print("can vote")
