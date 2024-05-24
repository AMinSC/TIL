def solution(park, routes):
    for i, y_li in enumerate(park):
        for j, x in enumerate(y_li):
            if x == 'S':
                s_y, s_x = i, j
    
    x_y_dict = {k: v for k, v in zip(['X', 'Y'], [s_x, s_y])}
    
    for route in routes:
        x = x_y_dict['X']
        y = x_y_dict['Y']
        op, n = route.split()
        n = int(n)

        if op == 'E' and n < len(park[y][x:]) and 'X' not in park[y][x + 1:x + n + 1]:
            print('E')
            x_y_dict['X'] += n
            
        if op == 'W' and n < len(park[y][:x]) + 1 and 'X' not in park[y][x - n:x]:
            x_y_dict['X'] -= n
            
        if op == 'S' and n < len(park[y:]):
            cnt = 0
            for check_y in park[y + 1:y + n + 1]:
                if check_y[x] == 'X':
                    break
                cnt += 1
            if cnt == n:
                x_y_dict['Y'] += n
                
        if op == 'N' and n <= len(park[y - n:y]):
            cnt = 0
            for check_y in park[y - n:y]:
                if check_y[x] == 'X':
                    break
                cnt += 1
            if cnt == n:
                x_y_dict['Y'] -= n
            
    return [x_y_dict['Y'], x_y_dict['X']]