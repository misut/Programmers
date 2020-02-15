import itertools

def solution(baseball):
    answer = 0
    pool = [''.join( lst ) for lst in list( itertools.permutations( '123456789', 3 ) )]
    for guess in pool:
        for testcase in baseball:
            test, strike, ball = testcase
            test = str( test )
            g_strike, g_ball = 0,0
            if guess[0] == test[0]:
                g_strike += 1
            if guess[1] == test[1]:
                g_strike += 1
            if guess[2] == test[2]:
                g_strike += 1
            if guess[0] == test[1] or guess[0] == test[2]:
                g_ball += 1
            if guess[1] == test[0] or guess[1] == test[2]:
                g_ball += 1
            if guess[2] == test[1] or guess[2] == test[0]:
                g_ball += 1
            if g_strike != strike or g_ball != ball:
                break
        else:
            answer += 1
    return answer
