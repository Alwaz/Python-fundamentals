
### this function will calculate the total ascii sum of string entered by user
def ascii_sum(s):
    total_ascii_sum = 0
    for i in range(len(s)):
        total_ascii_sum += ord(s[i])
    return total_ascii_sum



### this function will calculate the sum of odd ascii values.
def ascii_sum_odd(s):
    odd_ascii_sum = 0
    for i in range(len(s)):
        if ((i + 1) % 2 == 1):
            odd_ascii_sum += ord(s[i])
    return odd_ascii_sum

### this function will calculate the sum of even ascii values.
def ascii_sum_even(s):
    even_ascii_sum = 0
    for i in range(len(s)):
        if ((i + 1) % 2 == 0):
            even_ascii_sum += ord(s[i])
    return even_ascii_sum


text = input('Enter a String: ')
print('Sum of all ascii values: ', ascii_sum(text))
print('Sum of odd ascii values: ', ascii_sum_odd(text))
print('Sum of even ascii values: ', ascii_sum_even(text))


