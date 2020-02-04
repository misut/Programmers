def solution(arrangement):
    answer = 0
    iron = 0
    pre = ')'
    for cur in arrangement:
        # 쇠막대기 시작
        if cur is '(':
            iron += 1
        else:
            iron -= 1
            # 레이저
            if pre is '(':
                answer += iron
            # 쇠막대기 끝
            else:
                answer += 1
        pre = cur
    return answer
