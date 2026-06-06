'''#                                                            functions
#    its syntax is ===    def fun_name(parameter 1,parameter 2):
#                                                                       example = 1
def sum(a,b): #parameters a and b
    return a+b
    
c=sum(3,6) #functon call # 3,6 are arguments
print(c)

#                                                                       example = 2
def p():
    print("hello")


p()#unction call in second example
p()
p()



#  if a function returns no value then it results none in optput example in same above example 
def p():
    print("hello")

z=p()
print(z)

#                                                                    default arguments 
# here if we want to give default value to the parameters we could dp so 
  #we give default value to any one of the parameter and give another paraeter value further but note when we gave value to any one parameter we have to gae value to second parameter,



#1.                                                       simple example
def sum(a=1,b=5):
   return a+b

c=sum()
print(c)




#2.                                                giving default value to any one of parameter
def sum(a,b=5):
   return a+b

c=sum(6)
print(c)



#                                           write a program to print length of a string 
str={"hello", "welcome", "everyone ","here"}

def fun(list):
    print(len(list))

fun(str)



#write a program to print element of a string in a single line

#                                                                      one method
str=["hello", "welcome", "everyone ","here"]

for i in str:
    print(i, end=" ")

#                                               second mathod toprint all elements of the list in one line 
str=["hello", "welcome", "everyone ","here"]
def name(list):
    for i in list:
        print(i,end=" ")
   
name(str)





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

num(5)'''

#calculate sum using recursion

def sum(num):
    if(num==0):
        return 0
    return sum(num-1)+num

c=sum(5)
print(c)



