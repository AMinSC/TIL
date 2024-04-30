import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
X = list(map(int, input().split()))

X.sort(reverse = True)
print(X[k-1])