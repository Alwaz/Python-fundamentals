# this method will check the conjuctor
def colletz_conjuctor(n):
    chain = []
    while (n != 1):
        chain.append(n)
        print(n, end='-')
        if (n % 2 != 0):
            n = 3 * n + 1
        else:
            n = n // 2
    print(n)
    return len(chain) + 1


num = int(input('Please enter a number: '))
print('The length of collatz chain is: ', colletz_conjuctor(num))