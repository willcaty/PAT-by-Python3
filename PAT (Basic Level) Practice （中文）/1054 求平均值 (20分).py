# -*- coding=utf-8 -*-
input()
total, count = 0, 0
for i in input().split():
    try:
        n = float(i)
        if -1000 <= n <= 1000:
            if len(str(n).split('.')[1]) > 2:
                raise Exception
        else:
            raise Exception
        total += n
        count += 1
    except Exception:
        print('ERROR: {} is not a legal number'.format(i))

if count == 0:
    print('The average of 0 numbers is Undefined')
elif count == 1:
    print(f'The average of 1 number is {total:.2f}')
else:
    print(f'The average of {count} numbers is {total / count:.2f}')
