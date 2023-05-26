polynomial =  "1x"

def solution(polynomial):
    s = polynomial.split(' ')
    only_num = []
    poly_num = []
    for i in s:
        if 'x' in i:
            poly_num.append(i)
        elif i.isdigit():
            only_num.append(i)
    if only_num and not poly_num:
        if sum(map(int, only_num)) == 0:
            return ''
        return f'{sum(map(int, only_num))}'
    x = 0
    num = 0
    for i in poly_num:
        if i.isalpha():
            x += 1
        else:
            num += int(i[:len(i) - 1])
    if not only_num and poly_num:
        if x + num <= 1:
            return 'x'
        return f'{x + num}x'
    if int(sum(map(int, only_num))) == 0:
        if int(x + num) == 1:
            return 'x'
        return f'{x + num}x'
    if int(x + num) == 1:
        return f'x + {sum(map(int, only_num))}'
    return f'{x + num}x + {sum(map(int, only_num))}'


solution(polynomial)