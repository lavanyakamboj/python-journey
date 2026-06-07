#calculate sum using recursion

def sum(num):
    if(num==0):
        return 0
    return sum(num-1)+num

c=sum(5)
print(c)
