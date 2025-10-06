import sys

input = sys.stdin.readline


def date_to_days(date):
    yyyy, mm, dd = map(int, date.split("."))
    return yyyy * 12 * 28 + mm * 28 + dd


def solution(today, terms, privacies):
    today_days = date_to_days(today)
    term_dict = {t: int(m) for t, m in terms.items()}

    answer = []
    for i, (date, tp) in enumerate(privacies, start=1):
        start_days = date_to_days(date)
        expire_days = start_days + term_dict[tp] * 28
        if expire_days <= today_days:
            answer.append(i)
    return answer


YYYY, MM, DD = input().strip().split(".")
today = ".".join([YYYY, MM, DD])

n = int(input().strip())
terms = {}
for _ in range(n):
    t, m = input().split()
    terms[t] = m

p = int(input().strip())
privacies = []
for _ in range(p):
    date, t = input().split()
    privacies.append((date, t))

print(solution(today, terms, privacies))
