#calculate factorial

num=int(input('Enter number whos factorial needs to be known: '))

fact=1

if num==0 or num==1:
    print(1)
elif num<0:
    print('Factorial doesnt exist')
else:
    for i in range(1,num+1):
        fact=fact*i
    print('factorial of ',num,'is', fact)