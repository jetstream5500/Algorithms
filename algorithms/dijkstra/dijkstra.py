from sets import Set

def fetch_adj_matrix(filename):
    adjacency_matrix = []
    with open('test.in', 'r') as fin:
        for line in fin:
            node_connections = map(float, line.split())
            adjacency_matrix.append(node_connections)
    return adjacency_matrix

def closest_node(to_process, dists):
    min_dist = float('inf')
    min_node = -1
    for node in to_process:
        if dists[node] < min_dist:
            min_node = node
            min_dist = dists[node]
    return min_node

def adjust_dists(adjacency_matrix, min_node, dists, to_process):
    for i,weight in enumerate(adjacency_matrix[min_node]):
        if dists[min_node]+weight < dists[i]:
            if dists[i] == float('inf'):
                to_process.add(i)
            dists[i] = dists[min_node]+weight

def dijkstra(filename, start_node=0, end_node=None):
    adjacency_matrix = fetch_adj_matrix(filename)
    num_nodes = len(adjacency_matrix)
    dists = [float('inf')]*num_nodes

    dists[start_node] = 0.0
    to_process = Set([start_node])

    while len(to_process) > 0:
        min_node = closest_node(to_process, dists)
        if end_node == min_node:
            return dists[min_node]
        to_process.remove(min_node)
        adjust_dists(adjacency_matrix, min_node, dists, to_process)

    return dists

if __name__ == '__main__':
    print(dijkstra('test.in'))
