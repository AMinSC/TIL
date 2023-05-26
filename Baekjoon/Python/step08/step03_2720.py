T = int(input())
# 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)
change = {'q': 25, 'd': 10, 'n': 5, 'p': 1}
for _ in range(T):
    c = float(input())
    c_list = []
    for i in change:
        share, remainder = divmod(c, change[i])
        c_list.append(int(share))
        c = remainder
    print(*c_list, sep=' ')
