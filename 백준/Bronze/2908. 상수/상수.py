def rev (A:list):
    a = []
    for i in A:
        a.append(i)
    a.reverse()
    return (a)

def ltoi (A:list):
    f_n = int(A[0]) * 100
    s_n = int(A[1]) * 10
    t_n = int(A[2])
    return f_n + s_n + t_n

A, B = input().split()
A = rev(A)
B = rev(B)
A = ltoi(A)
B = ltoi(B)
if A > B:
    print(A)
else:
    print(B)