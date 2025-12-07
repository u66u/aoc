from pathlib import Path


def inp(path: Path) -> list[list[str]]:
    res = []
    with open(path, "r") as f:
        l = f.readlines()
        for i in l:
            res.append([c for c in i if c != "\n"])
    return res


def solve(inp: list[list[str]]) -> int:
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    grid = [list(row) for row in inp]
    seen = set()
    
    seen.add(tuple("".join(row) for row in grid))

    while True:
        new_state = [['.' for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                cell = grid[i][j]
                bugs = 0
                for d in dirs:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < 5 and 0 <= y < 5:
                        if grid[x][y] == "#": 
                            bugs += 1
                
                if cell == "#":
                    if bugs == 1:
                        new_state[i][j] = "#"
                    else:
                        new_state[i][j] = "."
                else: 
                    if bugs == 1 or bugs == 2:
                        new_state[i][j] = "#"
                    else:
                        new_state[i][j] = "."
                        
        grid = new_state
        
        t = tuple("".join(row) for row in grid)
        
        if t in seen: 
            rating = 0
            count = 0
            for r in range(5):
                for c in range(5):
                    if grid[r][c] == "#":
                        rating += 2**count
                    count += 1
            return rating
            
        seen.add(t)

x = inp("24.txt")
print(solve(x))


