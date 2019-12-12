file = open("input.txt","r")
class node():
    def __init__(self, data):
        self.branches = []
        self.data = data
    def addBranch(self, x):
        self.branches.append(x)
lines = file.readlines()
nodes = {}
for i in lines:
    B = i.split(")")[1][:-1]
    A = i.split(")")[0]
    if(A not in nodes):
        nodes[A] = node(A)
    if(B not in nodes):
        nodes[B] = node(B)
    nodes[A].addBranch(nodes[B])
def traverse(n, length):
    if(len(n.branches)==0):
        return length
    return length + sum([traverse(i, length+1) for i in n.branches])

x = []
n = nodes["COM"]
length  = 0
visited = ["COM"]
file.close()
    
with open('input.txt', 'r') as f:
    parents = dict( reversed(orbit.split(')')) for orbit in f.read().splitlines() )            
ancestors = lambda n: ancestors(parents[n]).union([parents[n]]) if n in parents else set()
print(len(ancestors('YOU') ^ ancestors('SAN')))
        
    
        
        
    
