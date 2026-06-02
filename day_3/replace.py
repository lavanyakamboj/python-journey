# write a programe to fill the name and date in given letter 
# replace doesnot change the string as the strings are immutable , replace , find method only create new string and print it doesnot change the previous

letter = '''dear <|Name|>,  
            you are selected!  
            <|date|> '''


print(letter.replace("<|Name|>","lavanya").replace("<|date|>","26 august 2026"))
# using replace twice is called chaining