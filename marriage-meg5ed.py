# Mary Graham (meg5ed)
# Collaborators: Scott Miller(Fsm5yd) Alexus Ferguson (Alw3fk)
# CS4102 Algorithms - S'18 -- Nate Brunelle
# Due Wednesday May 9, 2018 at 11P via Collab
# Sources: https://medium.com/basecs/finding-the-shortest-path-with-a-little-help-from-dijkstra-613149fbdc8e
# Sources: https://gist.github.com/econchick/4666413
# Sources: https://www.python.org/doc/essays/graphs/

from itertools import product
import queue


def getProduct(nodes):
        goodList = []       #verified positions
        for i in range(0,len(nodes)):
                for j in range(0,len(nodes)):
                        if (i != j) and (i not in nodes[j]):
                                goodList.append([i,j])
        graph = {}
        for i in range(0,len(nodes)):
                for j in range(0,len(nodes)):
                        if [i,j] in goodList:
                                tmp = []
                                for z in list(product(nodes[i],nodes[j])):
                                        if list(z) in goodList:
                                                tmp.append(z)
                                graph[(i,j)] = tmp
        ret = {}
        
        for x in graph: #removing positions that are not reached
                if len(graph[x]) != 1:
                        ret[x] = graph[x]
        return ret

def createNodes(adjls):
        nodes = {}
        for i in range(0,len(adjls)):
                nodes[i] = adjls[i] + [i]
        return nodes

def get_Path(graph, start, end):         
        visited = {tuple(start): 0}
        path = {}
        nodes = set(graph)
        while nodes:
                min_node = None
                for n in nodes:
                        if n in visited:
                                if min_node is None:
                                        min_node = n
                if min_node is None:
                        break
                nodes.remove(min_node)
                cur = visited[min_node]

                for edge in graph[min_node]:
                        weight = cur + 1
                        if edge not in visited:
                                visited[edge] = weight
                                path[edge] = weight
        return visited, path

def findPaths(adjls, strt1, end1, strt2, end2):
        nodes = createNodes(adjls) #better representation of nodes
        graph = getProduct(nodes) #defines all possible positions
        nodeList = []
        for i in graph:
                nodeList.append(list(i))
        print(list(get_Path(graph, [strt1,strt2], [end1, end2])))

        return (str(strt1)+" ... "+str(end1), str(strt2)+" ... "+str(end2))

           

def find_Shortest_Path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

#def properOutput(Verticies):

	#print 


#example code to read the input file. Use it or don't. You're an adult, make your own decisions.
f = open('chapel.txt', 'r')
cNodes = int(f.readline()) #number of nodes
tpLuke = f.readline().split()
strtLuke = int(tpLuke[0]) #Luke's start node
endLuke = int(tpLuke[1]) #Luke's end node
tpLor = f.readline().split()
strtLor = int(tpLor[0]) #Lorelai's start node
endLor = int(tpLor[1]) #Lorelai's end node
adjlsChapel = [] #adjacency list
for node in range(cNodes):
	adjlsChapel.append(list(map(lambda rm: int(rm), f.readline().split())))
pthLuke, pthLor = findPaths(adjlsChapel, strtLuke, endLuke, strtLor, endLor)
print(pthLuke)
print(pthLor)
