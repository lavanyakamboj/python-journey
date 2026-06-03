numbers = {1, 2, 3, 4, 5}
print(numbers)


# emtey set
h = set()   # dont use h={} b/c it creates empty dictonary
print(h)
print(type(h))

# 1. add values =====   set_name.add(value)
h = set()
h.add(1)
h.add(4)
h.add((6,2,34,56))
h.add("collage")
print(h)

# 2. remove values =====   set_name.remove(value)
a = {1,1,2,1,5,79}
a .remove(1)
print(a)


# 3. to emptey the set  ==== set_name.clear()
b = {1,2,5,79}
b.clear()
print(b)
print(len(b))

# 4. to pop elements in random order any value could be printed ==== set-name.pop()
b = {1,1,2,1,5,79}
print(b.pop())

# 5. to combine two sets ==== set1.union(set2)
b = {1,2,5,79}
k={4,9,7,76,4,0}
e=b.union(k)
print(e)      
#  or
print(b.union(k)) 

# 6. to return commo value if the two sets ==== set1.intersection(set2)
b = {1,2,5,79}
k={4,9,7,76,4,0,1}
e=b.intersection(k)
print(e) 
