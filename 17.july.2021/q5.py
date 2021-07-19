
### function to perform XOR on boolean inputs.
def calc_XOR(bool1, bool2):
    if bool1=='False' and bool2=='False':
        return False
    elif  bool1 == 'False' and bool2 == 'True':
        return True
    elif bool1 == 'True' and bool2 =='False':
        return True
    else:
        return False


### asks the user for two Boolean inputs.
user_bool1=input("Enter 'True or 'False: ")
user_bool2 = input("Enter 'True or 'False: ")

print('XOR result: ',calc_XOR(user_bool1, user_bool2))