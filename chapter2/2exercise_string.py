letter = '''        Dear <NAME>
        you are selected
        <DATE>'''
name = input("enter name")
date = input("enter date")

print(letter.replace("<NAME>",name).replace("<DATE>",date))





