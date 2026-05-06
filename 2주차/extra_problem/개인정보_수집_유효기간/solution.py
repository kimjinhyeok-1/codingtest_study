def solution(today, terms, privacies):
    answer = []
    
    term_dict = {}
    for t in terms:
        kind, months = t.split()
        term_dict[kind] = int(months)
    
    def to_days(date):
        y, m, d = map(int, date.split("."))
        return y * 12 * 28 + m * 28 + d
    
    today_days = to_days(today)
    
    for i, privacy in enumerate(privacies):
        date, kind = privacy.split()
        expire = to_days(date) + term_dict[kind] * 28
        if expire <= today_days:
            answer.append(i + 1)
    
    return answer