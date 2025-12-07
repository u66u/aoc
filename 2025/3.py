from os import getenv
from aocd import get_data

session = getenv("AOC_SESSION")
d = get_data(session, 3, 2025)
inp = d.split("\n")


def p1(inp: list) -> int:
    res = 0
    for s in inp:
        m, idx = 0, 0
        n = len(s)
        for i in range(n - 1):
            x = int(s[i])
            if x > m:
                m = x
                idx = i
        num = m * 10
        m = 0
        for j in range(idx + 1, n):
            x = int(s[j])
            if x > m:
                m = x
        num += m
        res += num
    return res


def p2(inp: list) -> int:
    res = 0
    for s in inp:
        n = len(s)
        num, idx = 0, -1
        for i in range(11, -1, -1):
            m, m_idx = 0, idx + 1
            for j in range(idx + 1, n - i):
                x = int(s[j])
                if x > m:
                    m = x
                    m_idx = j
            idx = m_idx
            num += m * (10**i)
        res += num
    return res


print(p2(inp))
