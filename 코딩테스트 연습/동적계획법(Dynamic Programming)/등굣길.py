import collections

def solution(m, n, puddles):
    board = [[-1 if [x+1, y+1] in puddles else 0 for y in range( n )] for x in range( m )]
    board[0][0] = 1
    q = collections.deque( [[0, 0]] )
    while q:
        x, y = q.popleft()
        if x+1 < m and board[x+1][y] >= 0:
            board[x+1][y] += board[x][y]
            if [x+1, y] not in q:
                q.append( [x+1, y] )
        if y+1 < n and board[x][y+1] >= 0:
            board[x][y+1] += board[x][y]
            if [x, y+1] not in q:
                q.append( [x, y+1] )
    answer = board[m-1][n-1] % 1000000007
    return answer
