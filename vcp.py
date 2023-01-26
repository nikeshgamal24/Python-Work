def is_safe(v, color_initial, c, graph):
    for i in range(len(graph)):
        if graph[v][i] == 1 and c[i] == color_initial:
            return False
    return True

def graph_colouring(graph, color_initials, c, v):
    if v == len(graph):
        return True

    for color_initial in color_initials:
        if is_safe(v, color_initial, c, graph):
            c[v] = color_initial
            if graph_colouring(graph, color_initials, c, v+1) == True:
                return True
            c[v] = 'X'
    return False

def vertex_coloring(graph, color_initials):
    v = len(graph)
    c = ['X'] * v
    if graph_colouring(graph, color_initials, c, 0) == False:
        return False
    return c

if __name__ == "__main__":
    graph = [[0,1,1,0,1,1], [1,0,1,0,0,0], [1,1,0,1,0,0], [0,0,1,0,1,0],[1,0,0,1,0,1],[1,0,0,0,1,0]]
    color_initials = ['R', 'G', 'B']
    result = vertex_coloring(graph, color_initials)
    if result == False:
        print("No solution exists")
    else:
        print("Colors assigned to the vertices: ",result)