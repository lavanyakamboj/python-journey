# for loop 

# it is used to itrate over a sequece such as list, tuple,string etc
# used of loop in which we know how many times we want to execute the loop 
# first example --> for i
name="hello everyone present here" 
for i in name:
    print(i) 

# second example --> for range() 
for i in range(8):
    print(i) 

# example 
color=("red","blue","green")
for a in color:
   print(a)
   for i in a:
       print(i)
#print the elements(1,4,9,16,25,36,64,81,100)       
a=1
for i in range(10):
    print(a*a)
    a+=1 
          
#    or 
for a in range(1,10):
    print(a*a)
    a+=1
    
# increment

for a in range(1,10,2):  # here the third value increment the value by that specific number
    print(a*a)
    a+=1