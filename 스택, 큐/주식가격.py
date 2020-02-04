def solution(prices):
    answer = [0 for price in prices]
    stack, targets = [], []
    for sec, price in enumerate( prices ):
        targets.clear()
        for idx, time in enumerate( stack ):
            if prices[time] > price:
                answer[time] = sec-time
                targets.append( idx )
        for target in reversed( targets ):
            del stack[target]
        stack.append( sec )
    else:
        for time in stack:
            answer[time] = sec-time
    return answer
