import datetime

class User:    
    def __init__(self, no, date, rank):
        year, month, day = map(int, date.split("."))
        self.year = year
        self.month = month
        self.day = day
        self.rank = rank
        self.date = date
        self.no = no
    
    def max_term(self, month):
        days = self.day + (int(month) * 28)
        months, days = divmod(days, 28)
        if not days:
            days = 28
            months -= 1
        self.day = days
        
        months += self.month
        years, months = divmod(months, 12)
        if not months:
            months = 12
            years -= 1
        self.month = months

        self.year += years
        self.date = f"{self.year}.{self.month}.{self.day}"
        
    def get_date(self):
        self.date = f"{self.year}.{self.month}.{self.day}"
    
    def check_date(self, today):
        today = datetime.datetime.strptime(today, '%Y.%m.%d')
        max_date = datetime.datetime.strptime(self.date, '%Y.%m.%d')
        
        if max_date <= today:
            return True

    def __str__(self):
        return f"rank: {self.rank}, date: {self.date}, no: {self.no}"
        

def solution(today, terms, privacies):
    answer = []
    # 모든 달은 28일
    terms_dict = {}
    for term in terms:
        rank, month = term.split()
        terms_dict[rank] = month
    privacies_list = []
    
    for privacie in privacies:
        date, rank = privacie.split()
        privacies_list.append([date, rank])
    
    for i, privacie in enumerate(privacies_list, 1):
        
        user = User(i, privacie[0], privacie[1])
        user.max_term(terms_dict[user.rank])
        user.get_date()
        
        if user.check_date(today):
            answer.append(user.no)
    
    return answer