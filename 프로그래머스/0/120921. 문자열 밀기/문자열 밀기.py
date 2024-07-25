def solution(A, B):
    # if A == B:
    #     return 0
    # first = A[0]
    # i = B.index(first)
    # new_b = B[i:] + B[:i]
    # if new_b == A:
    #     return i
    # return -1
    
    return (B * 2).index(A) if A in (B * 2)  else -1
