content= True
i=0
with open("log.txt") as f:
    while content:
        content = f.readline()
        

        if 'python' in content.lower():
            print(content)
            print("YES PYTHON IS PRESENT")
            print(i)
        i+=1