# word = "python"
# data = True
# lineno=1
# with open("file.txt", "r") as f:
#    while data:
#       data=f.readline() 
#       if (word in data):
#           print("found")
#           print(lineno)
#           break
#       lineno+=1

with open("file.txt","r") as f:
    print(f.read())