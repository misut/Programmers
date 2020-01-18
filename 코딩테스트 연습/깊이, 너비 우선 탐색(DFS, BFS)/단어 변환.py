from collections import deque

def just_one_different( word1, word2 ):
    diff = 0
    for c1, c2 in zip( word1, word2 ):
        if c1 is not c2:
            diff += 1
    if diff == 1:
        return True
    return False
    
def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append( (begin, 0) )
    while queue:
        cursor, level = queue.popleft()
        if cursor is target:
            answer = level
            break
        nextwords = []
        for word in words:
            if just_one_different( cursor, word ):
                nextwords.append( word )
        for word in nextwords:
            words.remove( word )
            queue.append( (word, level+1) )
    return answer
