from heapq import *

def prism(grpah , start, parent , distance , visited):
    print('--'*45)
    print("Inside function prism")
    print('-'*60)
    print(f'graph {graph}')
    print(f'parent {parent}')
    print(f'visited {visited}')
    print(f'distance {distance}')
    print()

    bag = []
    heappush(bag,[0,start])
    parent[start] = -1
    distance[start] = 0

    while bag:
        print('---------------------------BAG comten------------------------')
        print(bag)
        print('-'*60)
        print('-'*100)
        print('------------------OUTER LOOP---------------------')
        node_distance, node = heappop(bag)
        print(f"POPED --> distance: {node_distance} and node: {node} \n\n")

        if not visited[node]:
            visited[node] = 1
            print(f'visited: {visited}')

            #looking for the child node of the current node
            for child_distance , child_node in graph[node]:
                print('------------------INNER LOOP---------------------')
                
                print(f'Child_node: {child_node} and child_distance: {child_distance}')

                if distance[child_node] > child_distance and not visited[child_node]:
                    print()
                    print(f'Child_node: {child_node} and child_distance: {child_distance}')
                    print()
                    print(f' child node distance to node {distance[child_node]} \n')
                    parent[child_node] = node
                    print(f'updated parent {parent} \n')
                    distance[child_node] = child_distance
                    print(f'updated distance {distance} \n')
                    heappush(bag,[child_distance,child_node])
                    print(f'updated bag {bag}')

            print('------------------NEXT ITERATION--------------------\n')
            print(f'graph {graph}')
            print(f'parent {parent}')
            print(f'visited {visited}')
            print(f'distance {distance}')
            print()
        else:
            print('This node is already visited')

    print('-'*100)
    print('----------------------FINAL OUTPUT-------------------------------')
    print(parent)
    print(distance)

# input = [[1,2,1],[2,5,2],[1,5,3],[2,3,4],[3,4,1],[4,5,2],[2,4,1]]
# n=5
n = 7
#pre-processing step that sorting the edges by weight--> O(E logE)
input= [[1,2,28],[2,3,16],[2,7,14],[3,4,12],[4,7,18],[4,5,22],[5,7,24],[5,6,25],[1,6,10]]

graph = {}
parent = {}
visited = {}
distance = {}

for i in range(1,n+1):
    graph[i] = []

    parent[i] = None
    visited[i] = 0
    distance[i] = 10**8+1

print('-'*60)
print(graph)
print(parent)
print(visited)
print(distance)
print()

ind =0
for u,v,d in input:
   # to have record the node can be reached from which node with what distance 
    graph[u].append([d,v])
    graph[v].append([d,u])
    print(f'{ind+1} loop run')
    ind +=1
    print(graph)

#at this stage we have  record of graph in which we have record i.e. that particular node is accesssed by which other node and by what distance


start = 1
prism(graph , start, parent , distance , visited)
