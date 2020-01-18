class vertex:
    def __init__( self, value ):
        self.value = value
        self.color = 'White'
        self.d = 0
        self.f = 0
        self.adj = []
        
    def adjacents( self ):
        return self.adj
    
    def get_color( self ):
        return self.color
    
    def discover( self, time ):
        self.color = 'Gray'
        self.d = time
    
    def finish( self, time ):
        self.color = 'Black'
        self.f = time
    
    def connect_to( self, other ):
        self.adj.append( other )
    
    def connect_with( self, other ):
        self.connect_to( other )
        other.connect_to( self )
        
def DFS( V ):
    cuts = []
    time = 0
    for u in V:
        if u.get_color() is 'White':
            time, cut = DFS_VISIT( u, time )
            cuts.append( cut )
    return cuts

def DFS_VISIT( u, time ):
    time += 1
    u.discover( time )
    cuts = [u]
    for v in u.adjacents():
        if v.get_color() is 'White':
            time, cut = DFS_VISIT( v, time )
            cuts.append( cut )
    time += 1
    u.finish( time )
    return time, cuts

def solution( n, computers ):
    V = [vertex( v ) for v in range( n )]
    for u in range( n ):
        for v in range( u, n ):
            if computers[u][v] == 1:
                V[u].connect_with(V[v])
    cuts = DFS( V )
    answer = len( cuts )
    return answer
