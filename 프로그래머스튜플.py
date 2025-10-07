def solution(s):
    answer = []

    s = s.lstrip('{').rstrip('}').split("},{")
    s = [list(map(int, x.split(','))) for x in s]

    tu = []
    for i in range(len(s)):
        for lst in s:
            if len(lst) == i + 1:
                for k in lst:
                    if k not in tu:
                        tu.append(k)
                        answer.append(k)

    print(answer)
    return answer