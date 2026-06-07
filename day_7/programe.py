#  write a program to print length of a string 
str={"hello", "welcome", "everyone ","here"}

def fun(list):
    print(len(list))

fun(str)


# write a program to prinnt factorial of a parameter in function
num=int(input("enter number"))
def fact(num): 
    a=1
    for i in range(1,num+1):
      a=a*i
      i=i+1
    print(a)

fact(num)


# WAF to convert USD into INR

num=int(input("enter the number of us dolour"))
def con(num):
    a=num*83
    print(num," us dolour in indian rupees are ",a)

con(num)


#write a program to print weather is given number is odd or even using function

num=int(input("enter the number"))
def even_odd(num):
    a=num%2
    if(a==0):
       print("number is even")
    else:
        print("number is odd")

even_odd(num)



#                                                                       recursion

# print numbers from 5 to 1
def num(n):
    if(n==0):
        return
    print(n)
    num(n-1)

num(5)