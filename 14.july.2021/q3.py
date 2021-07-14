#Calculate avg
user_quit= " "
user_list=[]
sum=0
product=1

print('Enter numbers to calculate product and avg, press q to exit')

# While loop will terminate on pressing q
while user_quit!='q':
    num=int(input())
    user_list.append(num)
    user_quit=input('wanna exit?')

# loop to calculate avg and product
for i in range(0,len(user_list)):
    sum+=user_list[i]
    product*=user_list[i]
print('Avg of user input number is: ', sum/len(user_list))
print('Product of Number is: ', product)








