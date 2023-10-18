visited = []
heights = []
reachable_heights = []
bridges = 0
g = [] #Adjacency matrix

# Definition of bridge: A bridge is an edge that increases the number of connected components when deleteted. 
# Finds number of bridges in undirected graph. Can be modified to find articulation vertices.
def dfs(u, e):
    global bridges
    visited[u] = True
    reachable_height = heights[u]
    for v in g[u]:
        if v != e:
            if visited[v]:
                reachable_height = min(reachable_height, heights[v])
            else:
                heights[v] = heights[u] + 1
                dfs(v, u)
                reachable_height = min(reachable_height, reachable_heights[v])
                if heights[u] < reachable_heights[v]:
                    bridges += 1 #Edge between u and v is a bridge


    reachable_heights[u] = reachable_height