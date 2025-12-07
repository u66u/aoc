from pathlib import Path
def solve(path: Path) -> int:
    res = 0
    with open(path, "r") as f:
        l = f.readlines()
        for i in l:
            x = int(i.strip())
            while x > 0:
                x = x // 3 - 2
                if x > 0:
                    res+=x 
    return res

print(solve("1.txt"))
