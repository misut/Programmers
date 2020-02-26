class node:
    def __init__(self):
        self.numbers = []
        self.childs = [None for _ in range(10)]
    
    def insert(self, number):
        cur = self
        for n in number:
            if cur.numbers:
                return False
            idx = int( n )
            if not cur.childs[idx]:
                cur.childs[idx] = node()
            cur = cur.childs[idx]
        else:
            cur.numbers.append( number )
        return True

def solution(phone_book):
    answer = True
    root = node()
    phone_book.sort(key=lambda x : len(x))
    for number in phone_book:
        answer = root.insert( number )
        if not answer:
            break
    return answer
