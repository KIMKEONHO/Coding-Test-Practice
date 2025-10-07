def solution(cacheSize, cities):
    answer = 0

    if cacheSize == 0:
        return len(cities) * 5

    cache = [[" ", 0] for _ in range(cacheSize)]

    for city in cities:
        city = city.lower()
        hit = False

        for slot in cache:
            if slot[0] == city:
                answer += 1
                hit = True
                slot[1] = 0
            else:
                if slot[0] != " ":
                    slot[1] += 1

        if not hit:
            answer += 5
            empty = next((i for i, slot in enumerate(cache) if slot[0] == " "), None)
            if empty is not None:
                cache[empty] = [city, 0]
            else:
                oldest = max(range(cacheSize), key=lambda idx: cache[idx][1])
                cache[oldest] = [city, 0]

    return answer


cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
          "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))  # 50 나와야 함
