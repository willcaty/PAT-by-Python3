# -*- coding=utf-8 -*


def check(input_str: str):
    if input_str.count("P") != 1 or input_str.count("T") != 1:
        return False
    elif input_str.index("T") < input_str.index("P"):
        return False
    elif input_str.count("A") < 1:
        return False
    for i in input_str:
        if i not in ["P", "A", "T"]:
            return False
    p_index = input_str.index('P')
    t_index = input_str.index('T')
    if input_str[p_index:t_index].count('A') > 0:
        left_a = input_str[0:p_index].count('A')
        middle_a = input_str[p_index:t_index].count('A')
        right_a = input_str[t_index:].count('A')
        if left_a * middle_a == right_a:
            return True
        else:
            return False
    else:
        return False


n = int(input())
for s in range(n):
    print("YES") if check(input()) else print('NO')
