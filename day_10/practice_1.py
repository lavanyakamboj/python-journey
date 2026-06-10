# without with --
# f=open("poem.txt")
# content = f.read()
# if("twinkle" in content):
#     print("yes")
# else:
#     print("no")
# f.close

# using with --

with open("poem.txt","r") as f:
    content = f.read()

    if "twinkle" in content:
        print("yes")
    else:
        print("no")