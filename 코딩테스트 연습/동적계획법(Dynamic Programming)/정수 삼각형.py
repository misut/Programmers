def solution(triangle):
    n_levels = len( triangle )
    for lev in range( n_levels-2, -1, -1 ):
        for cur in range( lev+1 ):
            if triangle[lev+1][cur] > triangle[lev+1][cur+1]:
                triangle[lev][cur] += triangle[lev+1][cur]
            else:
                triangle[lev][cur] += triangle[lev+1][cur+1]
    answer = triangle[0][0]
    return answer
