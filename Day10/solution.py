import pathlib
from typing import List


def read_input(path):
    f_path = pathlib.Path(path).resolve()

    with open(f_path, "r") as f:
        lines = f.read().splitlines()

    data = []

    for line in lines:
        data.append([int(char) for char in line])

    return data


class Node:

    def __init__(self, height, r, c):
        self.height = height
        self.r = r
        self.c = c

    def __str__(self):
        return f"({self.height}, {self.r}, {self.c})"

    def __repr__(self):
        return f"({self.height}, {self.r}, {self.c})"


class Graph:

    def __init__(self, top_map):

        self.v = {}
        self.e = {}
        self.populate_nodes(top_map)
        self.populate_edges(top_map)

    def populate_nodes(self, top_map: List[List[int]]):

        height = len(top_map)
        width = len(top_map[0])

        for i in range(height):
            for j in range(width):

                self.v[(i, j)] = Node(top_map[i][j], i, j)

    def populate_edges(self, top_map: List[List[int]]):

        height = len(top_map)
        width = len(top_map[0])

        for i in range(height):
            for j in range(width):

                neightbours = []

                if i >= 1:
                    if self.v[(i - 1, j)].height - self.v[(i, j)].height == 1:
                        neightbours.append(
                            self.v[(i - 1, j)]
                        )  # north neighbour
                if j >= 1:
                    if self.v[(i, j - 1)].height - self.v[(i, j)].height == 1:
                        neightbours.append(
                            self.v[(i, j - 1)]
                        )  # west neighbour
                if i < height - 1:
                    if self.v[(i + 1, j)].height - self.v[(i, j)].height == 1:
                        neightbours.append(
                            self.v[(i + 1, j)]
                        )  # south neighbour
                if j < width - 1:
                    if self.v[(i, j + 1)].height - self.v[(i, j)].height == 1:
                        neightbours.append(
                            self.v[(i, j + 1)]
                        )  # east neighbour

                self.e[(i, j)] = neightbours


def dfs(node_graph, curr, goal, path):

    if curr == goal:
        print(f"({path[0].r},{path[0].c}),({goal.r},{goal.c})")
        return 1

    count = 0
    for n in node_graph.e[(curr.r, curr.c)]:
        count += dfs(node_graph, n, goal, path + [curr])

    return count


def problem_1(arr_map):

    my_graph = Graph(arr_map)

    starts = []
    goals = []

    for i in range(len(arr_map)):
        for j in range(len(arr_map[0])):
            if my_graph.v[(i, j)].height == 0:
                starts.append(my_graph.v[(i, j)])
            elif my_graph.v[(i, j)].height == 9:
                goals.append(my_graph.v[(i, j)])

    count = 0
    for start in starts:
        for goal in goals:
            count += dfs(my_graph, start, goal, [])
            # print(f"{start}, {goal}")

    return count


def main():
    arr_map = read_input("Day10/input.txt")
    result = problem_1(arr_map)
    print(result)


if __name__ == "__main__":
    main()
