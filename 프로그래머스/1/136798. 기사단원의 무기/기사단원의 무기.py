def solution(number, limit, power):
    answer = 0
    number_list = []
    for num in range(1, number + 1):
        num_list = []
        new_num = int(num ** 0.5) + 1
        for i in range(1, new_num):
            if num % i == 0:
                num_list.append(i)
                if i ** 2 != num:
                    num_list.append(num // i)
                # cnt += 1
            # if cnt > limit:
            #     break
        if len(num_list) > limit:
            number_list.append(power)
        else:
            number_list.append(len(num_list))
    
    return sum(number_list)