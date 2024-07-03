def solution(numbers, hand):
    answer = ''
    left_hand = 10
    right_hand = 12
    
    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            left_hand = number
        elif number in [3, 6, 9]:
            answer += "R"
            right_hand = number
        else:
            left = sum(divmod(abs((number if number else 11) - left_hand), 3))
            right = sum(divmod(abs((number if number else 11) - right_hand), 3))
            
            number = number if number else 11
            if left < right:
                answer += "L"
                left_hand = number
            elif left > right:
                answer += "R"
                right_hand = number
            else:
                if hand == 'left':
                    answer += "L"
                    left_hand = number
                else:
                    answer += "R"
                    right_hand = number
            
    return answer