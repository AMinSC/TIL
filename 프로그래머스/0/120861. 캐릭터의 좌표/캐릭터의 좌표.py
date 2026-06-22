def solution(keyinput, board):

    max_x = board[0] // 2
    max_y = board[1] // 2
    x = 0
    y = 0
    
    for key in keyinput:
        if key == "left":
            if x == max_x * -1: pass
            else: x -= 1
        elif key == "right":
            if x == max_x: pass
            else: x += 1
        elif key == "up":
            if y == max_y: pass
            else: y += 1
        elif key == "down":
            if y == max_y * -1: pass
            else: y -= 1
            
    return x, y