prime = True
num = int(input("ENTER THE NUMBER"))
for i in range(2,10,2):
    if num%i==0:
        prime = False
        break
if prime:
    print("PRIME")
else:
    print(" NOT PRIME")        