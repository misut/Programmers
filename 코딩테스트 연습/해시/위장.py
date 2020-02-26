def solution(clothes):
    answer = 1
    closet = {}
    for cloth, kind in clothes:
        closet[kind] = closet.get(kind, []) + [cloth]
    for kind, clothes in closet.items():
        answer *= len(clothes) + 1
    answer -= 1
    return answer
