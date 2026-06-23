# ──────────────────────────────────────────────────
# Problem     Mini-Max Sum
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-23, 11:50 a.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min_val=float('inf')
    max_val=float('-inf')
    for i in range(len(arr)):
        sum_val=0
        for j in range(len(arr)):
            if i==j:
                continue
            else:
                sum_val+=arr[j]
        min_val=min(min_val,sum_val)
        max_val=max(max_val,sum_val) 
    print(min_val, max_val)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
