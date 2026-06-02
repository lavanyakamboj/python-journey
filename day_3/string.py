# string 

# length of string = len(string)
'''
    a="hello everyone present here"
    print("lenth of a ", len(a),"")
    print("\n")
    print(a[0:5])
    print(a[0:len(a)-13])
'''
# multi line strings in - ''' ......'''


# string mathods 
 
# 1.srip()
'''
    a="                        hello everyone present here                "
    a="                        hello everyone present here                "
    print(a)
    print(a.strip())
'''

# 2.rstrip
'''
    a="//////hello everyone present here//////"
    print(a.rstrip("/"))
'''

# 3.find()
'''
    a="hello everyone present here"
    print(a.find("pr"))
'''

# 4. slice()
'''
    name = "lavanya"
    name_slice = name[0:3] # this includes the characters from the index 0 to 2 not 3
    print(name_slice)
'''

# print after space in slicing 
name = "lavanya"
name_slice = name[2:7:2] # this includes the characters from the index 0 to 2 not 3
print(name_slice)


# 5. length of string -- len()
print (len(name))

# 6. endswith() -- tells weather the string ends with some given characters or not - gave true or false
# similar there is starts with;
#both these functions are acse senstive

print (name.endswith("rry"))
print (name.endswith("ya"))
