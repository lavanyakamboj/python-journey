Marks = [12,34,54,24,54,56]

# append -- insert at the end 
Marks.append(4)
print(f'append : {Marks}')

# insert -- insert into list at a particular index
Marks.insert(3,10)    # here 3 is index and 10 is number
print(f'insert : {Marks}')

# sort
Marks.sort()
print(f'sort : {Marks}')

# reverse -- reverse the list 
Marks.reverse()
print(f'reverse : {Marks}')

# pop -- remove element 
value = Marks.pop(3)
print(f'pop : {value}')

# remove -- a particular value
Marks.remove(10)
print(f'remove : {Marks}')