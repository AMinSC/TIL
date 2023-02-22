s = list(map(str, input()))
asc_arr = []
for i in range(97, 123):
	asc_arr.append(i)
al_arr = asc_arr
for i, asc in enumerate(asc_arr):
	try:
		idx = s.index(chr(asc))
		al_arr[i] = idx
	except:
		al_arr[i] = -1
	print(al_arr[i])
#print(al_arr)
