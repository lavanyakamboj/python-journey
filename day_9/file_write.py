# if in write or apend mode we open any file which doesnot exist then it will created.
# if we open file in write mode then its previous content get deleated i.e. data will get 
# over write so we use appned mode to write new things and also to make exist the previous content.

st = "this is example of the write mode "

f = open("file.txt","w")
f.write(st)
f.close()