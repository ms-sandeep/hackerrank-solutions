# ──────────────────────────────────────────────────
# Problem     Diagonal Difference
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-23, 10:53 a.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    val1=0
    val2=0
    for i in range(len(arr)):
        val1+=arr[i][i]
    m=len(arr)-1
    for j in range(len(arr)):
        val2+=arr[j][m]
        m-=1
    ans=val2-val1
    return abs(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
