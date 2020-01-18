def search_path( left, used=[], start='ICN' ):
    left = [ticket for ticket in left]
    if not left:
        return [start]
    for ticket in left:
        if ticket[0] == start:
            left.remove( ticket )
            path = search_path( left, used+[ticket], ticket[1] )
            left.append( ticket )
            left.sort()
            if path:
                return [start] + path

def solution( tickets ):
    answer = []
    tickets.sort()
    answer = search_path( tickets )
    return answer
