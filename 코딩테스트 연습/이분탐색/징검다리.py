def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append( distance )
    stt, end = 1, distance
    while stt+1 < end:
        mid = (stt+end) // 2
        pre, m = 0, 0
        for rock in rocks:
            if rock - pre < mid:
                m += 1
                if m > n:
                    break
            else:
                pre = rock
        if m <= n:
            stt = mid
        else:
            end = mid
    return stt
