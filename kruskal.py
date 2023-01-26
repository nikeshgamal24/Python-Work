#find function to determine head of the family to check whether the node connection does not form loop

def find(graph,node):
    if graph[node] < 0:
        return node #i.e. head of the group 
    else:
        # temp = find(graph,graph[node])
        # graph[node] = temp
        # return temp
        return find(graph,graph[node])

def union(graph,a,b,answer):
    ta = a
    tb = b
    a = find(graph, a) # node number
    b = find(graph, b) # node number
    if a == b:
        print(f"Can't join {ta} and {tb} as it forms cycle")
    else:
        answer.append([ta,tb])
        # node number ko value lai compare garnu parni xa to determine one node as head of the family
        print('-'*60)
        print(ta,a,graph[a])
        print(tb,b,graph[b])
        print('-'*60)
        if graph[a] == graph[b]:
            graph[a] = graph[a] + graph[b]
            graph[b] = a
        else: 
            #less negative means more node connection as a whole i.e. magnitude of node in that family is hight
            if graph[a] < graph[b]: 
                graph[a] = graph[a] + graph[b]
                graph[b] = a
            else:
                graph[b] = graph[b] + graph[a]
                graph[a] = b


#graph node in random order
#---------------------TEST CASE 1-------------------------------
n = 7
#pre-processing step that sorting the edges by weight--> O(E logE)
test_case1 = [[1,2,28],[2,3,16],[2,7,14],[3,4,12],[4,7,18],[4,5,22],[5,7,24],[5,6,25],[1,6,10]]
sorted_list = sorted(test_case1 , key =  lambda test_case1 : test_case1 [2]) 

#-------------------------TEST CASE 2------------------------------
# n = 9
# test_case2 = [[0,1,4],[0,7,8],[1,7,11],[1,2,8],[2,3,7],[2,8,2],[3,4,9],[3,5,14],[4,5,10],[5,2,4],[5,6,2],[6,8,6],[6,7,1]]

# sort the pair of vertices in ascending order
# sorted_list = sorted(test_case2 , key =  lambda test_case2 : test_case2 [2]) 


answer = []

graph = [-1]*(n+1)  #each node ma -1 halxa initially  to indicate initaillay each node is head of independent family
#make all singleton set

for u,v,d in sorted_list:
    union(graph,u,v,answer)

print("Final answer is:")
for item in answer:
    print(item)
