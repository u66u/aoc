
with open('3.txt', 'r') as f:
    txt = f.read().strip().split('\n')
    txt = [line for line in txt if line]
    w1_in, w2_in = txt[0], txt[1]


def s1(w1: str, w2: str) -> int:
    seg = [[], []]
    ws = [w1.split(","), w2.split(",")]

    for idx in range(len(ws)):
        cx, cy = 0, 0
        wire_path = ws[idx]
        for move in wire_path:
            direction = move[0]
            amount = int(move[1:])

            start_pos = (cx, cy)
            if direction == "U": cy += amount
            elif direction == "D": cy -= amount
            elif direction == "R": cx += amount
            elif direction == "L": cx -= amount

            end_pos = (cx, cy)
            seg[idx].append((start_pos, end_pos))
            
    w1c, w2c = seg[0], seg[1]
    
    min_dist = float('inf')
    found = False

    for i in range(len(w1c)):
        x1_start, x1_end = w1c[i][0][0], w1c[i][1][0]
        y1_start, y1_end = w1c[i][0][1], w1c[i][1][1]
        
        w1_x_min, w1_x_max = sorted((x1_start, x1_end))
        w1_y_min, w1_y_max = sorted((y1_start, y1_end))
        
        w1_is_vert = x1_start == x1_end

        for j in range(len(w2c)):
            x2_start, x2_end = w2c[j][0][0], w2c[j][1][0]
            y2_start, y2_end = w2c[j][0][1], w2c[j][1][1]
            
            w2_x_min, w2_x_max = sorted((x2_start, x2_end))
            w2_y_min, w2_y_max = sorted((y2_start, y2_end))
            
            w2_is_vert = (x2_start == x2_end)

            cross_x, cross_y = 0, 0
            has_cross = False

            if w1_is_vert and not w2_is_vert:
                if (w2_x_min <= x1_start <= w2_x_max) and (w1_y_min <= y2_start <= w1_y_max):
                    cross_x = x1_start
                    cross_y = y2_start
                    has_cross = True
            elif not w1_is_vert and w2_is_vert:
                if (w1_x_min <= x2_start <= w1_x_max) and (w2_y_min <= y1_start <= w2_y_max):
                    cross_x = x2_start
                    cross_y = y1_start
                    has_cross = True

            if has_cross:
                if cross_x == 0 and cross_y == 0:
                    continue
                
                dist = abs(cross_x) + abs(cross_y)
                if dist < min_dist:
                    min_dist = dist
                    found = True
                    print(f"at ({cross_x}, {cross_y}), dist: {dist}")

    return min_dist if found else 0



res= s1(w1_in, w2_in)
print(res)

