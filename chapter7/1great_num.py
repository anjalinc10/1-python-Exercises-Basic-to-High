def great(num):
    return max(num)

num1 = int(input("ENTER FIRST NUMBER  "))
num2 = int(input("ENTER SECOND NUMBER  "))
num3 = int(input("ENTER TTHIRD NUMBER  "))

a = [num1,num2,num3]
print(great(a))

#method_2
def maximum(nums):
    temp=0
    for n in nums:
        if n>temp:
            temp=n
    return temp

nums=[23,34,55]
print(maximum(nums))