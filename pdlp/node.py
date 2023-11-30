from uuid import uuid4
from pdlp.style import Style
from pdlp.shape import Shape
from dataclasses import dataclass, field

@dataclass
class Edge:
    source: "Node"
    destination: "Node"
    label:str = ""
    color:str = ""
    constraint:bool = True

@dataclass
class Node:
    label: str = ""
    shape: Shape = Shape.BOX
    style: Style = Style.ROUNDED
    color: str = 'white'
    connections:list[Edge] = field(default_factory=list)
    
    def __hash__(self):
        return hash(f"{self.label}-{uuid4()}")  # 基于节点的标签生成哈希值

    def connect(self, node, label="", color="", constraint=True):
        self.connections.append(Edge(self, node, label, color, constraint))

@dataclass
class Graph(dict):
    pass
        
def generate_json(nodes) -> Graph:
    graph = Graph()
    for node in nodes:
        connected_nodes = []
        for edge in node.connections:
                connected_nodes.append(edge.destination)
        if connected_nodes:
            graph[node] = connected_nodes
    return graph

if __name__ == "__main__":
    A = Node("A")
    B = Node("B")
    C = Node("C")
    A.connect(B)
    A.connect(C)
    C.connect(A)
    graph = generate_json([A, B, C])
    assert graph == {A:[B, C], C:[A]}

