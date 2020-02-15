def solution(answers):
    answer = []
    ans_cnt = [0, 0, 0]
    ans_lst = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    for idx, ans in enumerate( answers ):
        for spj in range( 3 ):
            length = len( ans_lst[spj] )
            if ans == ans_lst[spj][idx%length]:
                ans_cnt[spj] += 1
    highscore = max( ans_cnt )
    for spj in range( 3 ):
        if ans_cnt[spj] == highscore:
            answer.append( spj+1 )
    return answer
