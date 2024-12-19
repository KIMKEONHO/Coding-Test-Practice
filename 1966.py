from collections import deque
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    signi = list(map(int, sys.stdin.readline().split()))
    queue = deque([(value, idx) for idx, value in enumerate(signi)])
    count = 0

    while queue:
        # 현재 큐에서 가장 높은 중요도를 찾음
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            # 만약 현재 문서가 우리가 찾고자 하는 문서라면
            if queue[0][1] == M:
                print(count)
                break
            else:
                queue.popleft()  # 인쇄되었으므로 큐에서 제거
        else:
            queue.append(queue.popleft())  # 중요도가 낮다면 뒤로 보냄
