def solution(phone_number):
    number = phone_number[-4:]
    change_n = len(phone_number[:-4])
    return f"{'*' * change_n}{number}"