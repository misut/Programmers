def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    while progresses:
        for idx, speed in enumerate( speeds ):
            if progresses[idx] < 100:
                progresses[idx] += speed
        release = 0
        while progresses and progresses[-1] >= 100:
            progresses.pop()
            speeds.pop()
            release += 1
        if release > 0:
            answer.append( release )
    return answer
