student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA"
}
print(student) # or 
print(student.items())
print(type(student))

#  Accessing Values
print(student["name"])  # or 
print(student.get("name")) # it doesnot exist get gave none and above line gave error

# Adding a New Item
student["city"]="delhi"
print(student) 

# Updating a Value
student["name"]="ram"
student.update({"city":"chd"}) # if the element doesnot extsts it create new
print(student)


# Removing an Item
student.pop("name")
print(student)

# keys--  All keys
print(student.keys())
    # to get all keys  ==  dict_name.keys()    keys come in the form of dict keys to convert ot into the list we use tpecasting
print(list(student.keys()))  # type casting in list
print(tuple(student.keys()))  # type casting in tuple

# valuse--  All values
print(student.values())

# null dictonary
null={}
print(null)

#   nested dictonary  == in this we xould creat new dictonary in the value of the specific key 
info={
    "name":"ram",
    "subjects":{    # dictonary in dictonary
        "physics": 98,
        "maths":69,
        "chem":87,
     },
} 

print(info)
print(info["name"])
print(info["subjects"]["chem"])