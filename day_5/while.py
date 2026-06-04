# while loop

i=10
while(i>0):
    print(i)
    i=i-1


#print numbers from 1 to 100
i=1
while i<= 100:
    print(i)
    i+=1

#primt multiplication tableof a number
num=int(input("enter the number you want"))
count=1
while count<=10 :
    print( num," * ",count,"=", num*count)
    count+=1

#print the elements(1,4,9,16,25,36,64,81,100)
a=1
while a<=10:
    print(a*a)
    a+=1

#search for element x in(1,4,9,16,25,36,64,81,100)
num=int(input("enter the number you want to search"))
b=1
while (b<=10):
    c=b*b
    print(c)
    b+=1
    if(num==c):
       print("yes number exist at", b-1 ,"index")  