import itertools

primes = { 0: False, 1: False }
def is_prime( num ):
    if num not in primes:
        limit = int( num ** 0.5 )
        for div in range( 2, limit+1 ):
            if num%div == 0:
                primes[num] = False
                break
        else:
            primes[num] = True
    return primes[num]

def make_all( numbers ):
    length = len( numbers )
    number_pool = []
    for l in range( length ):
        number_pool = number_pool + list( itertools.permutations( numbers, l+1 ) )
    number_set = set()
    for number in number_pool:
        number_set.add( int( ''.join( number ) ) )
    return number_set

def solution(numbers):
    answer = 0
    number_set = make_all( numbers )
    for num in number_set:
        if is_prime( num ):
            answer += 1
    return answer
