def solution(arr1, arr2):

    # 각 행렬의 행과 열의 길이
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])

    answer = [[0] * c2 for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for l in range(c1):
                answer[i][j] += arr1[i][l] * arr2[l][j]

    return answer
