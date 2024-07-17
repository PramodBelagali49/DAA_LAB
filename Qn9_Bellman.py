def bellmanFord(graph,src,V):
    dist=[float('inf')]*V
    dist[src]=0

    for i in range(V-1):
        for u,v,w in graph:
            if dist[u] != float('inf') and dist[u]+w<dist[v]:
                dist[v]=dist[u]+w

    for u,v,w in graph:
        if dist[u] != float('inf') and dist[u]+w<dist[v]:
            print("Graph has negative weight cycle")
            return

    print("vertex\tdistance from source")
    for i in range(V):
        print(i,"\t",dist[i])

graph=[]
V=int(input("Enter the no. of vertices:"))
E=int(input("Enter the no. of directed edges:"))

print("Enter edges in the form(u,v,wt)")
for i in range(E):
    u,v,wt=map(int,input(f"Edge {i+1} : ").split())
    graph.append( (u,v,wt) )

print("Graph:",graph)
src=int(input("Enter the source vertex:"))
bellmanFord(graph,src,V)








































# def BellmanFord(graph, src, V):
#     dist = [float('inf')] * V
#     dist[src] = 0

#     for i in range(V - 1):
#         for u, v, w in graph:
#             if dist[u] != float('inf') and dist[u] + w < dist[v]:
#                 dist[v] = dist[u] + w

#     for u, v, w in graph:
#         if dist[u] != float('inf') and dist[u] + w < dist[v]:
#             print("Graph contains negative weight cycle")
#             return

#     print("\nVertex\tDistance from source")
#     for i in range(V):
#         print(f"{i}\t{dist[i]}")

# V = int(input("Enter number of Vertices: "))
# E = int(input("Enter number of directed edges: "))

# graph = []
# print("\nEnter adjacency list edges [u, v, weight] separated by space:")
# for i in range(E):
#     graph.append(list(map(int, input(f"Edge {i+1}: ").split())))

# src = int(input("\nEnter source vertex: "))
# print("\nGraph:", graph)

# BellmanFord(graph, src, V)
