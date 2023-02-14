num_list = list(map(int, input().split()))
n_max = max(num_list)
print(n_max, num_list.index(n_max) + 1)
'''
위의 코드도 예제가 잘 돌아가지만 baekjoon에서는 틀렸다고 나온다.
아마 input 방법 때문인것 같다.
정답은 아래 코드와 같다.
n_max = 0
num_list = []
for i in range(9):
	num_list.append(int(input()))
	if num_list[i] > n_max:
		n_max = num_list[i]
print(n_max, num_list.index(n_max) + 1)
'''
