def solution( money ):
    money_A, money_B = money[:-1], money[:]
    length_A, length_B = len( money_A ), len( money_B )
    visited_A = [0 for _ in range( length_A )]
    visited_B = [0 for _ in range( length_B )]
    
    visited_A[0], visited_A[1] = money[0], money[0]
    visited_B[0], visited_B[1] = 0, money[1]
    for idx in range( 2, length_A ):
        visited_A[idx] = max( visited_A[idx-2]+money[idx], visited_A[idx-1] )
    for idx in range( 2, length_B ):
        visited_B[idx] = max( visited_B[idx-2]+money[idx], visited_B[idx-1] )
    return max( visited_A[-1], visited_B[-1] )
