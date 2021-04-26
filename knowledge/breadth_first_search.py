#   B---D
#  /|  /|\
# A | / | F
#  \|/  |
#   C---E


graph = {'A': ['B', 'C'],
         'B': ['A', 'C', 'D'],
         'C': ['A', 'B', 'D', 'E'],
         'D': ['B', 'C', 'E', 'F'],
         'E': ['C', 'D'],
         'F': ['D']}


# Breadth-first Search (BFS)
def BFS(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    parent = {s: None}
    while queue:
        node = queue.pop(0)
        ad_nodes = graph[node]     # find its adjacent nodes
        for i in ad_nodes:
            if i not in seen:
                queue.append(i)
                seen.add(i)
                parent[i] = node
        print(node)
    return parent


if __name__ == '__main__':
    parent = BFS(graph, 'A')

    # shortest distance to a node
    node = 'D'
    out = 0
    while parent[node]:
        out += 1
        node = parent[node]
    print(out)