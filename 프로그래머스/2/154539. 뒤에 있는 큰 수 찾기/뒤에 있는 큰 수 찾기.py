def solution(numbers):
    num_len = len(numbers)
    # 답변 리스트를 인자값의 길이만큼 -1로 초기화
    answer = [-1] * num_len
    stack = []
    for i in range(num_len):
        # stack에 top의 위치한 numbers배열의 숫자와 현재 숫자를 비교하여, 
        # 현재 숫자가 클 경우 stack에서 pop한 인덱스 요소의 답변 리스트값을 현재 값으로 대입
        # 즉, 현재 숫자보다 작은 앞의 값들을 현재 값으로 대입
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        
        stack.append(i)
    return answer