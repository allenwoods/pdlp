from typing import Dict, List, Optional
from pdlp.node import Node

class Graph(Dict[Node, List[Node]]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = None  # 用于存储根节点（如果存在）
        self.visited = set()  # 用于存储访问过的节点，防止循环访问
        self._find_possible_root()

    def _find_possible_root(self):
        """
        尝试找到一个可能的根节点。
        """
        node_parents = self._find_parents()
        for node in self.keys():
            if node_parents[node] == 0:
                self.root = node
                break

    def _find_parents(self) -> Dict[Node, int]:
        """
        计算每个节点的父节点数量。
        """
        node_parents = {node: 0 for node in self}
        for node, connections in self.items():
            for connected_node in connections:
                node_parents[connected_node] += 1
        return node_parents

    def get_root(self) -> Optional[Node]:
        """
        返回一个可能的根节点。
        """
        return self.root

    def explore_graph(self) -> Dict:
        """
        探索图中的节点关系。
        """
        if self.root:
            return self._explore_recursive(self.root)
        else:
            # 如果没有根节点，从任意节点开始探索
            start_node = next(iter(self))
            return self._explore_recursive(start_node)

    def _explore_recursive(self, node: Node) -> Dict:
        """
        递归地探索图。
        """
        if node in self.visited:
            return {node.label: ["..."]}  # 遇到已访问的节点，表示循环
        self.visited.add(node)

        if node not in self or not self[node]:
            return {node.label: []}
        return {node.label: [self._explore_recursive(child) for child in self[node]]}

if __name__ == "__main__":
    # 创建节点
    R = Node("Root")
    A = Node("A")
    B = Node("B")
    C = Node("C")

    # 建立连接
    R.connect(A)
    R.connect(B)
    R.connect(C)
    A.connect(B)
    A.connect(C)
    C.connect(A)

    # 构建图
    nodes = [A, B, C]
    graph = Graph()
    for node in nodes:
        graph[node] = [edge.destination for edge in node.connections]
    
    print(graph.root)
    print(graph.explore_graph())
