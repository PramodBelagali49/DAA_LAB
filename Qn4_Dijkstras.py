import heapq

def dijkstras(graph, src, V):
    shortest_path = [float('inf')] * V
    shortest_path[src - 1] = 0  # Distance to source vertex is 0
    priority_q = [(0, src - 1)]  # (distance, vertex_index) starting with source

    while priority_q:
        current_dist, u = heapq.heappop(priority_q)
        
        if current_dist > shortest_path[u]:
            continue
        
        for neighbour, weight in graph[u]:
            distance = current_dist + weight

            if distance < shortest_path[neighbour]:
                shortest_path[neighbour] = distance
                heapq.heappush(priority_q, (distance, neighbour))

    print("\nVertex\tDistance from src")
    for i in range(V):
        print(f"{i + 1}\t{shortest_path[i]}")  # Print results with 1-based indexing

# Input the graph
V = int(input("Enter the number of vertices: "))
graph = [[] for i in range(V)]

e = int(input("Enter the number of edges: "))
print("Enter edges in the form (u, v, weight):")
for _ in range(e):
    u, v, weight = map(int, input().split())
    graph[u - 1].append((v - 1, weight))  # Add edge from u to v
    graph[v - 1].append((u - 1, weight))  # Add edge from v to u for undirected graph

print("Adjacency List:")
for i in range(V):
    print(f"{i + 1} : {graph[i]}")  # Display adjacency list with 1-based indexing

src = int(input("Enter the source vertex (1-based index): "))
dijkstras(graph, src, V)  # Execute Dijkstra's algorithm from the specified source
