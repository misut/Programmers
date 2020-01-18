def solution( numbers, target, idx=0, result=0 ):
    answer = 0
    if idx == len( numbers ):
        if result == target:
            return 1
        else:
            return 0
    answer += solution( numbers, target, idx+1, result+numbers[idx] )
    answer += solution( numbers, target, idx+1, result-numbers[idx] )
    return answer
