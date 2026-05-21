#!/usr/bin/env python3
# Author: Abdul Mostofa
# Author ID: amostofa
# Date Created: 2026/05/20

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')
