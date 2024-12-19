def find_movie_title(n):
    count = 0
    number = 666

    while True:
        if '666' in str(number):
            count += 1
            if count == n:
                return number
        number += 1


# 입력 받기
n = int(input().strip())
print(find_movie_title(n))