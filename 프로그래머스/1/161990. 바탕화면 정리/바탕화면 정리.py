def solution(wallpaper):
    lux = len(wallpaper)
    luy = len(wallpaper[0])
    rdx = 0
    rdy = 0
    for r, c in enumerate(wallpaper):
        if "#" in c:
            if rdx < r + 1:
                rdx = r + 1
            if lux > r:
                lux = r
            n_luy = c.find("#")
            n_rdy = c.rfind("#") + 1
            if luy > n_luy:
                luy = n_luy
            if rdy < n_rdy:
                rdy = n_rdy
            
    return [lux, luy, rdx, rdy]