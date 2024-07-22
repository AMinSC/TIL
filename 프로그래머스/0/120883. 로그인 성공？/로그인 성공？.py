def solution(id_pw, db):
    answer = 'fail'
    for user in db:
        if id_pw[0] == user[0]:
            if id_pw[1] == user[1]:
                return "login"
            return "wrong pw"
    return answer