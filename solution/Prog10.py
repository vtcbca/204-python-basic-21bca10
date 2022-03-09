i = int(input("Enter Number : "))
a = i
sum = 0
while (i>0):
    digit = i%10
    sum =sum*10+digit
    i = i//10
if (a==sum):
    print(a,"Number is Palindrom")
else:
    print(a,"Number is Not Palindrom")
