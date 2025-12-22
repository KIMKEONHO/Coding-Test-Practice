def solution(s):

    answer = 0

    for _ in range(len(s)):
        # 문자열 회전을 위해 deque 사용
        from collections import deque

        s = deque(s)

        stack = []

        status = True

        # 입력 받은 문자열을 스택으로 관리
        # 1. 반복문을 돌며 나온 문자가 [, (, { 라면 append
        # 2. ], ), } 라면 pop을 함. (예외. pop 했을 시 문자가 비어있으면 바로 False)
        # 2-1. 이때 pop을 통해 나온 문자가 매칭되는 괄호가 아니면 False
        # 2-2. 매칭된 괄호라면 남은 for문을 마저 실행
        # 3. 이 전체 과정을 문자열 길이만큼 반복
        for char in s:

            if char in ('[', '(', '{'):
                stack.append(char)
            elif char == ']':
                if stack:
                    top = stack.pop()
                    if top == '[':
                        continue
                    else:
                        status = False
                        break
                else:
                    status = False
                    break
            elif char == '}':
                if stack:
                    top = stack.pop()
                    if top == '{':
                        continue
                    else:
                        status = False
                        break
                else:
                    status = False
                    break
            elif char == ')':
                if stack:
                    top = stack.pop()
                    if top == '(':
                        continue
                    else:
                        status = False
                        break
                else:
                    status = False
                    break


        if status:
            answer += 1

        s.rotate(-1)

    return answer


def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        stack = []
        for j in range(n):
            c = s[(i + j) % n]
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if not stack:
                    break

                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    break

    else:
        if not stack:
            answer += 1


    return answer


