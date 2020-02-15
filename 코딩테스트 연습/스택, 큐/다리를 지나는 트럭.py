import collections

def solution(bridge_length, weight, truck_weights):
    n_trucks = len( truck_weights )
    truck_weights.reverse()
    answer = 1
    current = truck_weights.pop()
    passed = []
    passing = collections.deque( [(1, current)] )
    while len( passed ) < n_trucks:
        answer += 1
        if answer-passing[0][0] == bridge_length:
            passed.append( passing.popleft()[1] )
            current -= passed[-1]
        if truck_weights and current+truck_weights[-1] <= weight:
            truck = truck_weights.pop()
            passing.append( (answer, truck) )
            current += truck
    return answer
