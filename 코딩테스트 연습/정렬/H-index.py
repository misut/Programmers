def solution(citations):
    answer = len( citations )
    citations.sort( reverse=True )
    n = 0
    while answer > n:
        if citations[n] >= answer:
            n += 1
        else:
            if n >= answer:
                break
            else:
                answer -= 1
                n = 0
    return answer
