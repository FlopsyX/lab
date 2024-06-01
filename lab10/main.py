import sys


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # Ініціалізація двовимірного масиву розміром vertices x vertices заповненого нулями
        self.graph = []
        for i in range(vertices):
            row = [0] * vertices  # Створюємо рядок з нулями
            self.graph.append(row)  # Додаємо рядок до графу

    def print_solution(self, dist):
        print("Вершина \tВідстань від джерела")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def min_distance(self, dist, spt_set):
        min_index = -1
        min_value = sys.maxsize

        for v in range(self.V):
            if not spt_set[v] and dist[v] < min_value:
                min_value = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        spt_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not spt_set[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(dist)


# Приклад використання графа
g = Graph(6)
g.graph = [
    [0, 11, 0, 12, 26, 0],
    [0, 0, 15, 0, 16, 0],
    [0, 0, 0, 0, 0, 20],
    [0, 0, 0, 0, 13, 0],
    [0, 0, 0, 0, 0, 14],
    [0, 0, 0, 0, 0, 0]
]

g.dijkstra(6)  # Починаємо з вершини з індексом "1"
