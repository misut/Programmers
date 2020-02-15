def solution(heights):
    answer = []
    stack = []
    for idx, height in enumerate( heights ):
        while stack:
            if stack[-1][1] > height:
                answer.append( stack[-1][0] )
                break
            stack.pop()
        else:
            answer.append( 0 )
        stack.append( (idx+1, height) )
    return answer
