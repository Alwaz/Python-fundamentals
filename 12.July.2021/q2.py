
# Attendance checker

# if attendance is less then 75 then student is not eligible to attend classes

total_classes = int(input('Enter Total Number of Classes held: '))

classes_attended = int(input('Enter Number of classes attended: '))

# Calculating percentage
attendance = int((classes_attended/total_classes)*100)

print(str(attendance) + '%')

if attendance < 75:
    print('You are not allowed sit in exam')
else:
    print('You are allowed to sit in exam')



