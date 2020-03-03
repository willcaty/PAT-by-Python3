# -*- coding: utf-8 -*-

pin = {0: 'ling', 1: 'yi', 2: 'er', 3: 'san',
       4: 'si', 5: 'wu', 6: 'liu', 7: 'qi',
       8: 'ba', 9: 'jiu'}

output = [pin.get(int(i)) for i in str(sum(list(map(int, input()))))]
print(' '.join(output))

"""
将接收到的参数转换成List[int]类型
将list求和，在获取对应的拼音输出
"""

