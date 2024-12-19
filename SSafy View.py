for test_case in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))

    view_count = 0

    for i in range(2, N - 2):
        left_max = max(heights[i - 2], heights[i - 1])
        right_max = max(heights[i + 1], heights[i + 2])
        surrounding_max = max(left_max, right_max)

        if heights[i] > surrounding_max:
            view_count += heights[i] - surrounding_max

    print(f"#{test_case} {view_count}")
