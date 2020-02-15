#`bfn` means "big fucking number"
class bfn( str ):
    def __lt__( self, other ):
        return self+other < other+self

def solution(numbers):
    answer = ''
    snums = sorted( [bfn( number ) for number in numbers], reverse=True )
    answer = answer.join( snums )
    if answer[0] == '0':
        return '0'
    return answer
