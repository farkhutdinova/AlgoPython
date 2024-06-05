INF = float("infinity")

graph = {
    "U": { "V": 6, "W": 7 },
    "V": { "U": 6, "X": 10 },
    "W": { "U": 7, "X": 1 },
    "X": { "W": 1, "V": 10 },
}

unvisited_min_distances = {vertex: INF for vertex in graph}
visited_vertices = {}
current_vertex = "U"
unvisited_min_distances[current_vertex] = 0

while len(unvisited_min_distances) > 0:
    current_vertex, current_distance = sorted(unvisited_min_distances.items(), key=lambda x: x[1]) [0]

    for neighbour, neighbour_distance in graph[current_vertex].items():
        if neighbour in visited_vertices:
            continue
        potential_new_distance = current_distance + neighbour_distance
        if potential_new_distance < unvisited_min_distances[neighbour]:
            unvisited_min_distances[neighbour] = potential_new_distance
    visited_vertices[current_vertex] = current_distance
    del unvisited_min_distances[current_vertex]

print(sorted(visited_vertices.items()))