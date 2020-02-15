def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        subarray = array[i-1:j]
        subarray.sort()
        answer.append( subarray[k-1] )
    return answer
