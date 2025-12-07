from aocd import get_data
from os import getenv

session = getenv("AOC_SESSION")
d = get_data(session, 3, 2025)
inp = d.split("\n")

def p1(inp: list) -> int:
    res = 0
    for s in inp:
        m, idx = 0, 0
        n = len(s)
        for i in range(n-1):
            x = int(s[i])
            if x > m: 
                m = x
                idx = i
        num = m * 10
        m = 0
        for j in range(idx+1, n):
            x = int(s[j])
            if x > m: 
                m = x
        num += m
        res += num
    return res

print(p1(inp))
