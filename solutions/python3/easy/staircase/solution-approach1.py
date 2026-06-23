# ──────────────────────────────────────────────────
# Problem     Staircase
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-23, 11:17 a.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(" ",end="")
        for k in range(i):
            print("#",end='')
        print()
            

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
