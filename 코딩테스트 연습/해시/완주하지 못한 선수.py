def solution(participant, completion):
    names = {}
    for name in participant:
        names[name] = names.get(name, 0) + 1
    for name in completion:
        names[name] -= 1
        if names[name] is 0:
            del names[name]
    answer = list(names.keys())[0]
    return answer
