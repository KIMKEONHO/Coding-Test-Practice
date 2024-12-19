T = int(input())

for i in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.reverse()

    max_price = 0
    total_profit = 0
    for j in lst:
        if j > max_price:
            max_price = j
        else:
            total_profit += max_price - j

    print(f"#{i + 1} {total_profit}")
