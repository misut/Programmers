import itertools


def solution(N, number):
    answer = 0
    memo = {cnt: set() for cnt in range( 1, 9 )}
    n = 0
    for cnt in range( 1, 9 ):
        n += N
        memo[cnt].add( n )
        n *= 10
    for A in range( 1, 9 ):
        if number in memo[A]:
            answer = A
            break
        for B in range( 1, A+1 ):
            if A+B > 8:
                break
            for n1, n2 in itertools.product( memo[A], memo[B] ):
                if n1+n2 in range( 1, 32001 ):
                    memo[A+B].add( n1+n2 )
                if n1-n2 in range( 1, 32001 ):
                    memo[A+B].add( n1-n2 )
                if n2-n1 in range( 1, 32001 ):
                    memo[A+B].add( n2-n1 )
                if n1*n2 in range( 1, 32001 ):
                    memo[A+B].add( n1*n2 )
                if n1//n2 in range( 1, 32001 ):
                    memo[A+B].add( n1//n2 )
                if n2//n1 in range( 1, 32001 ):
                    memo[A+B].add( n2//n1 )
    else:
        answer = -1
    for cnt in range( 1, 9 ):
        print( sorted( memo[cnt] ) )
    return answer
