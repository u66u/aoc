import math
from pathlib import Path


def inp(path: Path) -> list[list[str]]:
    res = []
    with open(path, "r") as f:
        l = f.readlines()
        for i in l:
            res.append([c for c in i if c != "\n"])
    return res


def solve(inp_grid):
    aster = []
    rows = len(inp_grid)
    cols = len(inp_grid[0])

    for r in range(rows):
        for c in range(cols):
            if inp_grid[r][c] == "#":
                aster.append((r, c))

    best = 0
    for station in aster:
        r_s, c_s = station
        seen_angles = set()

        for target in aster:
            if station == target:
                continue

            r_t, c_t = target
            dy = r_t - r_s
            dx = c_t - c_s

            angle = math.atan2(dy, dx)
            seen_angles.add(angle)
        best = max(best_count, len(seen_angles))

    return best


print(solve(inp("1.txt")))


# x, y = 10, 2
# g = gcd(x,y)
# i = 5
# print(g)
# while i:
#     print (x, y)
#     x = x // g
#     y = y // g
#     i-=1
#
