def rev_ltoi (A:list):
    a = []
    for i in A:
        a.append(i)
    a.reverse()
    f_n = int(a[0]) * 100
    s_n = int(a[1]) * 10
    t_n = int(a[2])
    return f_n + s_n + t_n

A, B = input().split()
A = rev_ltoi(A)
B = rev_ltoi(B)
if A > B:
    print(A)
else:
    print(B)