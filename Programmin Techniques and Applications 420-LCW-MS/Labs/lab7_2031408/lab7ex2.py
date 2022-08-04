from graph import digraph
from bfs import bfs, pathTo

#Exercise 1
fp = input()
pageNum = int(fp.readline().strip())
digraph = digraph(pageNum)  
endingPagePath = []         
reachable = []
shortestPageLength = []


for i in range(pageNum):
    v = [int(x) for x in fp.readline().split()]
    for item in v:
        if item != 0 and item != v[0]:
            digraph.addEdge(i, item - 1)
        if item == 0:
            endingPagePath.append(i)

bfs1, bfs2 = bfs(digraph, 0)

for i in range(1,pageNum):    
    reachable.append(pathTo(bfs2, 0, i))
if None in reachable:
    print("N")
else:
    print("Y")
for item in endingPagePath:
    shortestPageLength.append(reachable[item - 1])
print(len(min(shortestPageLength)))

#Exercise 2
graph = str(digraph).split("\n")
graph.pop(0)
graphList = []
for x in graph:
    temp = []
    for y in x.split(":"):
        for z in y.split():
            temp.append(z)
    if len(temp) != 0:
        graphList.append(temp)

print(int(max(graphList)[0]) - 1, len(max(graphList)))






