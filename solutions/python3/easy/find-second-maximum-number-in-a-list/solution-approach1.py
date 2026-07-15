# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# Problem     Find the Runner-Up Score!  
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-15, 11:37 a.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    high=float('-inf')
    second=float('-inf')
    for i in arr:
        if i>high:
            second=high
            high=i
        elif i>second and i<high:
            second=i 
    print(second)
