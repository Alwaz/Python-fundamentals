length=int(input('how long is your flag? '))
width=int(input('how wide is your flag? '))

length_2=int(input('how long ? '))
width_2=int(input('how wide ? '))



for l in range(length):
    for w in range(width):
        print('*', end=' ')
    print()    

for l2 in range(length_2):
    for w2 in range(width_2):
        print('*', end=' ')
    print()   
