i = int(input("Enter Number: "))
sum = 0
a = i
while (a>0):
    digit = a%10
    sum += digit ** 3
    a //= 10
if(i==sum):
    print(i,"is Amstrong Number")
else:
    print(i,"is Not Amstrong Number")
