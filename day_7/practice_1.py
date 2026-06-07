# write a program to print element of a string in a single line

#  one method
str=["hello", "welcome", "everyone ","here"]

for i in str:
    print(i, end=" ")

# second mathod toprint all elements of the list in one line 
str=["hello", "welcome", "everyone ","here"]
def name(list):
    for i in list:
        print(i,end=" ")
   
name(str)