with open("sample1.txt") as f:
    content = f.read()
words= ["monkey","faltu",'shembdi']
for word in words:
    content = content.replace(word,"s%^@$^")

    with open("sample1.txt","w") as f:
        f.write(content)
