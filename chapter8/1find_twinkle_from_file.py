find=open('poem.txt','r',encoding='utf-8')
f=find.read()
if 'twinkle' in f:
    print("present")
else:
    print("not present")
find.close()