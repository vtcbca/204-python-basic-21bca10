i = int(input("Enter any Number: "))
sum = 0
a = i
while (i != 0):
    sum = sum+(i%10)
    i = i//10
print(a,"Sum is ",sum)
