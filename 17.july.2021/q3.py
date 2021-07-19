from random import randint


def lucky_seven_ludo(dice_roll_count):
    count = sum_num = 0
    for i in range(1, dice_roll_count + 1):

        first_random_num = randint(i, 6)
        second_random_num = randint(i, 6)

        print('(', first_random_num, second_random_num, ')')

        sum_num = first_random_num + second_random_num

        print('Dice rolled', i, 'sum: ', sum_num)
        if (sum_num == 7):
            count += 1
    return print('lucky 7 got',count,'time(s)')

times = int(input('Enter number of times dice should be rolled. '))
lucky_seven_ludo(times)


