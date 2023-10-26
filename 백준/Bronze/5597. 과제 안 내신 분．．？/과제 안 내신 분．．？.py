student_list = []
while 1:
    try:
        a = int(input())
        student_list.append(a)
    except:
        break
total_list = [i for i in range(1, 31)]
answer_list = []
for i in total_list:
    if i not in student_list:
        answer_list.append(i)
print(f"{min(answer_list)}\n{max(answer_list)}")