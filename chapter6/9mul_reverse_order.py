num = int(input("ENTER NUMBER"))
for j in range(0,10):
    for i in range(10-j,11-j):
        print(f'{num}X{i}={num*i}')