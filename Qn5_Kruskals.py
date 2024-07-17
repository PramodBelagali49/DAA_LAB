def kruskal(num_vertices, edges):
    parent = list(range(num_vertices))
    
    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]
    
    def union(u, v):
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            parent[root_v] = root_u
    
    mst = []
    edges.sort(key=lambda edge: edge[2])  # Sort edges by weight
    min_cost=0

    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))
            min_cost+=weight
    return mst,min_cost

num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))
edges = []

print("Enter edges in the form (u, v, weight):")
for _ in range(num_edges):
    u, v, weight = map(int, input().split())
    edges.append((u-1, v-1, weight))
    edges.append((v-1, u-1, weight))   # for undirected graph

mst,min_cost = kruskal(num_vertices, edges)
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u+1} - {v+1}: {weight}")
print(f"Minimum cost : {min_cost}")
