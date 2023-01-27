class Undirected_Graph():

    def __init__(self, _size):
        self.size = _size
        self.graph = [[0 for _ in range(_size)] for _ in range(_size)]

    def add(self, _vertex1, _vertex2):
        # _vertex1, vertex2 는 각각 연결할 두 정점(vertex)
        self.graph[_vertex1][_vertex2] = 1
        self.graph[_vertex2][_vertex1] = 1

    def show_graph(self):
        # 그래프 정보 출력 메서드
        for i in range(self.size):
            print(f"[{i}]-> ", end="")
            for j in range(self.size):

                if (self.graph[i][j] == 1):
                    print(f"{j}", end=" ")
            print("")

    def get_size(self):
        return self.size
