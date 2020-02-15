def solution( K, travel ):
    answer=0
    visited=[[0 for _ in range( 1000000 )]for _ in range( 101 )]
    visited[0][travel[0][0]] = travel[0][1]
    visited[0][travel[0][2]] = travel[0][3]
    for i in range( 1, len( travel ) ):
        walk_t, walk_c, bike_t, bike_c = travel[i]
        for j in range( K ):
            if visited[i-1][j] == 0:
                continue
            if j + walk_t <= K:
                visited[i][j+walk_t] = max( visited[i][j+walk_t], visited[i-1][j]+walk_c )
                answer= max( answer,visited[i][j+walk_t] )
            if j + bike_t <= K:
                visited[i][j+bike_t] = max( visited[i][j+bike_t], visited[i-1][j]+bike_c )
                answer= max( answer,visited[i][j+bike_t] )
    return answer
