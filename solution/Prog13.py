i = 5
for a in range(i):
    for b in range(i+1):
        print('',end='')
    for b in range(a,i):
        print('*',end='')
    print()
