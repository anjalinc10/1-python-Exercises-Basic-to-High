# method_1
list1=["sachin","soham","tejas","mohan"]
for i in list1:
    if i[0]=='s':
        print("HELLO",i)
# method_2
for i in list1:
    if i.startswith("s"):
        print("HELLO",i)