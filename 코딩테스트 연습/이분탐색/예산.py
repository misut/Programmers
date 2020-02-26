def solution( budgets, M ):
    answer = 0
    csum = 0
    budget_cnt = [0 for _ in range( 100001 )]
    for budget in budgets:
        budget_cnt[budget] += 1
        answer = max( answer, budget )
        csum += budget
    for limit in range( answer, 0, -1 ):
        if csum < M:
            answer = limit
            break
        csum -= budget_cnt[limit]
        budget_cnt[limit-1] += budget_cnt[limit]
        budget_cnt[limit] = 0
    return answer
