def solution(n, arr1, arr2):
    answer = []
    result = [[0 for _ in range(n)] for _ in range(n)]

    aw1 = []
    aw2 = []

    for i in arr1:
        lst = toBinary(i, n)
        aw1.append(lst)

    for i in arr2:
        lst = toBinary(i, n)
        aw2.append(lst)

    for i in range(n):
        for j in range(n):
            if aw1[i][j] == 1 or aw2[i][j] == 1:
                result[i][j] = '#'
            else:
                result[i][j] = ' '

    for row in result:
        answer.append("".join(row))

    return answer

def toBinary(value, n):
    result = []
    while value > 0:
        result.append(value % 2)
        value //= 2
    result.reverse()
    while len(result) < n:
        result.insert(0, 0)
    return result


n = int(input().strip())

arr1 = list(map(int, input().strip().split()))

arr2 = list(map(int, input().strip().split()))

solution(n, arr1, arr2)