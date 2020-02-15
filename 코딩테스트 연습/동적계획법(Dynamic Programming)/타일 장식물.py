memo = [0 for _ in range( 81 )]
memo[0], memo[1], memo[2] = 2, 4, 6

def solution( N ):
    if memo[N]:
        answer = memo[N]
    else:
        answer = solution( N-1 )+solution( N-2 )
        memo[N] = answer
    return answer
