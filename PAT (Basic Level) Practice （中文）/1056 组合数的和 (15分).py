# -*- coding=utf-8 -*-

import sys

a = sys.stdin.readline().split()
print((int(a[0]) - 1) * 11 * sum(map(int, a[1:])))
