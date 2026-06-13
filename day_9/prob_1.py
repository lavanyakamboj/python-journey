#  from a file containing the numbers serpeated by comma ,prin the count of even numbers

count=0
with open("practice.txt","r") as f:
   data=f.read()
   print(data)
   num=data.split(",")
   for i in num:
      if(int(i)%2==0):
         count+=1
         print(i,"\n")
print("total number divisible by 2 are =",count)