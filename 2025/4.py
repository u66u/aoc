from os import getenv
from pathlib import Path

from aocd import get_data

session = getenv("AOC_SESSION")
file_path = Path(__file__)
day = int(file_path.stem)
year = int(file_path.parent.name)

d = get_data(session, day, year)
inp = [line for line in d.split("\n")]


def p1(inp: list) -> int:
    dirs = [
        (0, 1),
        (1, 0),
        (-1, 1),
        (1, -1),
        (1, 1),
        (0, -1),
        (-1, 0),
        (-1, -1)
    ]
    res = 0
    for row in range(len(inp)):
        for col in range(len(inp[0])):
            if inp[row][col] != "@": continue
            cnt = 0
            for d in dirs:
                r, c = row+d[0], col+d[1]
                if -1 < r < len(inp):
                    if -1 < c < len(inp[0]):
                        if inp[r][c] == "@": cnt+=1
                if cnt > 3: break
            if cnt < 4: res +=1
    return res



print(p1(inp))
