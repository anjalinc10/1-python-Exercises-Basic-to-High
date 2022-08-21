mytuple =(23,4,5,6)
# mytuple[0]=45
# print(mytuple)
# TypeError: 'tuple' object does not support item assignment
mylist=list(mytuple) #convert into list to perform action
mylist[0]=45
print(mylist)