def solution(numbers):
    answer = []
    stack = []
    # 뒷 큰수를 구하기 위해 리스트를 반전시킴
    for number in reversed(numbers):
        
        # 스택에 요소값이 있을 경우, 현재 숫자와 스택의 맨 위의 값을 비교
        while len(stack) > 0:
            # 스택의 맨 위의 값이 크다면 답변 리스트에 값을 추가하고 스택에 추가
            if stack[-1] > number:
                answer.append(stack[-1])
                stack.append(number)
                break
            # 그렇지 않다면 스택의 값을 제거
            else:
                stack.pop()
                
        # 스택에 값이 없다면 현재 숫자를 스택에 넣어두고, 답변 리시트에 -1 추가
        # 예를 들어 스택의 값이 현재의 값보다 모두 적을 경우, 
        # 위의 while 문을 통해 모든 값이 제거된 후 기능을 수행
        if len(stack) == 0:
            stack.append(number)
            answer.append(-1)
    
    return answer[::-1]