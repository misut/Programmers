def solution(brown, red):
    answer = [3, 3]
    while True:
        while answer[0]*answer[1] != brown+red or (answer[0]-2)*(answer[1]-2) != red:
            answer[0] += 1
            if answer[0]*answer[1] > brown+red or (answer[0]-2)*(answer[1]-2) > red:
                break
        else:
            break
        answer[1] += 1
        answer[0] = answer[1]
    return answer
