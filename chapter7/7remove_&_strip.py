def remove(string,word):
    newstr= string.replace(word,"")
    return newstr.strip()

this = "     i am doing my python exercise which is very interesting"
n = remove(this,"very")
print(n)