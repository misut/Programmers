import collections

def solution(priorities, location):
    answer = 0
    priorities = collections.deque( [(i, p) for i, p in enumerate( priorities )] )
    while priorities:
        current = priorities.popleft()
        if priorities and current[1] < max( priorities, key=lambda x : x[1] )[1]:
            priorities.append( current )
            continue
        answer += 1
        if current[0] == location:
            break
    return answer
