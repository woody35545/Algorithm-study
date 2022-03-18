import copy


class Undirected_Graph():
    inheritance_test = 0

    def __init__(self, _size):
        self.size = _size
        self.graph = [[0 for _ in range(_size)] for _ in range(_size)]

    def add(self, _vertex1, _vertex2):
        self.graph[_vertex1][_vertex2] = 1
        self.graph[_vertex2][_vertex1] = 1

    def show_graph(self):
        for i in range(self.size):
            print(f"[{i}]-> ", end="")
            for j in range(self.size):

                if (self.graph[i][j] == 1):
                    print(f"{j}", end=" ")
            print("")

    def get_size(self):
        return self.size


class Directed_Graph(Undirected_Graph):
    def __init__(self, _size):
        super().__init__(_size)


test_Directed_Graph = Directed_Graph(2)
test_Directed_Graph.show_graph()
print(test_Directed_Graph.get_size())
#
aGraph = Undirected_Graph(10)
aGraph.add(0, 1)
aGraph.add(2, 3)
aGraph.show_graph()
#

a = [0,1,2]
b = copy.deepcopy(a)
b[1] = 100
print(f"id(a): {id(a)} id(b): {id(b)}")
print(f"a: {a}, b: {b}")