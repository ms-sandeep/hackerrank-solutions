# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
# Problem     Time Conversion
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-18, 12:34 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hours=s[:2]
    am_pm=s[-2:]
    min_sec=s[2:-2]
    if int(hours)<12 and am_pm=='PM':
        new=int(hours)+12
        res=str(new)+ min_sec
    elif int(hours)==12 and am_pm=='AM':
        new='00'
        res=new+min_sec
    else:
        res=hours+min_sec
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
