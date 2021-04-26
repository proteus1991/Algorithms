#   B---D
#  /|  /|\
# A | / | F
#  \|/  |
#   C---E

# https://www.youtube.com/watch?v=9wV1VxlfBlI&list=PLAnjpYDY-l8IacYv_2lIZxNrQmkY3paSN&index=4

graph = {'A': {'B': 5, 'C': 1},
         'B': {'A': 5, 'C': 2, 'D': 1},
         'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
         'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
         'E': {'C': 8, 'D': 3},
         'F': {'D': 6}}

import heapq as pq
import math


def initiate_distance(graph, s):
    distance = {s: 0}
    for i in graph:
        if i not in distance:
            distance[i] = math.inf
    return distance


# Dijkstra method
def dijkstra(graph, s):
    pqueue = []                 # priority queue
    pq.heappush(pqueue, [0, s])
    seen = set()
    parent = {s: None}
    distance = initiate_distance(graph, s)

    while pqueue:
        dist, node = pq.heappop(pqueue)
        seen.add(node)      # put the node in seen set to denote it has been processed.
        for i in graph[node]:
            if i not in seen:
                if dist + graph[node][i] < distance[i]:
                    pq.heappush(pqueue, [dist + graph[node][i], i])
                    parent[i] = node
                    distance[i] = dist + graph[node][i]
    return parent, distance


if __name__ == '__main__':
    parent, distance = dijkstra(graph, 'A')
    print(parent)
    print(distance)

    # shortest distance to a node
    start_node = 'D'
    node = start_node
    stack = []
    while parent[node]:
        stack.append(node)
        node = parent[node]
    stack.append(node)
    print(stack)

    while stack:
        temp = stack.pop()
        if temp != start_node:
            print(temp, end='->')
        else:
            print(temp)
