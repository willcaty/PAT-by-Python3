# -*- coding=utf-8 -*-

n = [input() for i in range(4)]

day = {'A': 'MON', 'B': 'TUE', 'C': 'WED', 'D': 'THU', 'E': 'FRI', 'F': 'SAT', 'G': 'SUN'}
hour = {'0': '00', '1': '01', '2': '02', '3': '03', '4': '04',
        '5': '05', '6': '06', '7': '07', '8': '08', '9': '09',
        'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14',
        'F': '15', 'G': '16', 'H': '17', 'I': '18', 'J': '19',
        'K': '20', 'L': '21', 'M': '22', 'N': '23'}
n0, n1, n2, n3 = n[0], n[1], n[2], n[3]

repeat = []
for i in range(min(len(n0), len(n1))):
    if n0[i] == n1[i] and n0[i].isupper() and 'A' <= n0[i] <= 'G':
        repeat.append(day.get(n0[i]))
        break
for j in range(i + 1, min(len(n0), len(n1))):
    if n0[j] == n1[j] and 'A' <= n1[j] <= 'N':
        repeat.append(hour.get(n0[j]))
        break
    elif n0[j] == n1[j] and n0[j].isdigit():
        repeat.append(hour.get(n0[j]))
        break
for i in range(min(len(n2), len(n3))):
    if n2[i].isalpha() and n2[i] == n3[i]:
        if i < 10:
            repeat.append('0' + str(i))
        else:
            repeat.append(str(i))
        break

print(f'{repeat[0]} {repeat[1]}:{repeat[2]}')
