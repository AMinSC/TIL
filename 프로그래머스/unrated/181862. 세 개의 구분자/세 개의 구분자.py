def solution(myStr):
    answer = myStr.replace("a", " ").replace("b", " ").replace("c", " ").split()
    return answer if answer else ["EMPTY"]