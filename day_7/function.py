'''# functions
# its syntax is ===    def fun_name(parameter 1,parameter 2):

# example = 1
    def sum(a,b): #parameters a and b
        return a+b
        
    c=sum(3,6) #functon call # 3,6 are arguments
    print(c)

# example = 2
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

# default arguments 
# here if we want to give default value to the parameters we could do so 
# we give default value to any one of the parameter and give another paraeter value further but note when we gave value to any one parameter we have to gae value to second parameter,



#1.  simple example
    def sum(a=1,b=5):
    return a+b

    c=sum()
    print(c)




#2. giving default value to any one of parameter
    def sum(a,b=5):
    return a+b

    c=sum(6)
    print(c)



'''




