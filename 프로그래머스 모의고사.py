from collections import deque

per1Pattern = deque([1,2,3,4,5])
per2Pattern = deque([2,1,2,3,2,4,2,5])
per3Pattern = deque([3,3,1,1,2,2,4,4,5,5])

def solution(answers):

    scores = [0, 0, 0]

    for i in answers:

        pA = per1Pattern.popleft()
        pB = per2Pattern.popleft()
        pC = per3Pattern.popleft()

        if i == pA:
            scores[0] += 1
            print(per1Pattern)
        if i == pB:
            scores[1] += 1
            per2Pattern.append(pB)
            print(per2Pattern)
        if i == pC:
            scores[2] += 1
            per3Pattern.append(pC)
            print(per3Pattern)

    max_score = 0

    if scores:
        max_score = max(scores)

    answer = []

    for i, score in enumerate(scores):
        if score == max_score:
            answer.append(i + 1)

    return answer


