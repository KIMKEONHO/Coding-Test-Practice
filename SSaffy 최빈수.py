T = int(input())

for i in range(T):
    case_number = int(input())
    n = list(map(int, input().split()))
    number = [0] * 101
    for j in n:
        number[j] += 1
    max_number = max(number)
    max_lst = [i for i in range(101) if number[i] == max_number]
    mode_score = max(max_lst)
    print(f"#{case_number} {mode_score}")
