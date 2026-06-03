# ask number from user b/w 0-9 and write its english 

numbers = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten"
}

num=int(input("enter number : "))
print(numbers.get(num))