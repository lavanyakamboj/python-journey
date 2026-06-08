f = open("file.txt","r")
data = f.read()
print(data)
f.close()

# - 1. opening file -- done by f = open('file name','r')
'''
    f=open('for_file_io.txt','r')
    text=f.read()  #for read the file . it is the deault mode if no mode is given. here 'text' be string in which all data of the file is returned.
    print(text)
    print(type(text))
    f.close 
'''

# in read mode we can specify the number of letters we want to read br --f.read(any number)
'''
    f=open('for_file_io.txt','r')
    text=f.read(6)  
    print(text)
    f.close 
'''

# to read one line 
'''
f=open('for_file_io.txt','r')
text=f.readline()  # read first line
text2=f.readline()  # read second line
print(text2)
print(text)
f.close 
'''

# note -- if we have already printed all data and the use read line then the empty line is printed as all data is already read.
'''
    f=open('for_file_io.txt','r')
    text=f.read()  
    print(text)
    text1=f.readline()  # read first line
    text2=f.readline()  # read second line
    print(text1)
    print(text2)
    f.close 
'''
