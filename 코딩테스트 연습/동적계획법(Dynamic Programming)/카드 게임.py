import sys

sys.setrecursionlimit( 100000 )
visited = [[-1 for row in range( 2001 )] for col in range( 2001 )]
def solution(left, right):
    answer = 0
    col, row = len( left ), len( right )
    if visited[col][row] >= 0:
        answer = visited[col][row]
    else:
        if left and right:
            if left[0] > right[0]:
                answer = right[0] + solution( left, right[1:])
            else:
                answer = max( solution( left[1:], right ), solution( left[1:], right[1:] ) )
        visited[col][row] = answer
    return answer
