# -*- coding: utf-8 -*-

n = input().split()
m = input().split()
offset = int(n[0]) - int(n[1])
print(' '.join(m[offset:] + m[:offset]))
