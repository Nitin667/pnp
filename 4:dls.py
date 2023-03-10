from collections import defaultdict

path = []
class Graph:
	def __init__(self,vertices):
		self.V = vertices
		self.graph = defaultdict(list)
	
	def addEdge(self,u,v):
		self.graph[u].append(v)
		
	def DLS(self,source,target,maxDepth):
		path.append(source)
		if source == target: 
			#path.append(source)
			return True
		
		if maxDepth <= 0 : return False
		
		for i in self.graph[source]:
			#path.append(source)
			#path.append(i)
			if(self.DLS(i, target, maxDepth-1)):
				return True
		return False
		
g = Graph(9)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,5)
g.addEdge(2,6)
g.addEdge(3,7)
g.addEdge(3,8)

target = 2
maxDepth = 3
source = 0

if g.DLS(source, target, maxDepth) == True:
	print(f"Target {target} is reacheable from source {source} within max depth {maxDepth}")
	print(f"traversing path is:")
	print(path)
else:
	print(f"Target {target} is NOT reachable from source {source} within max depth {maxDepth}")
	
