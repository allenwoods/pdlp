import pdlp
from pdlp import create_graph, Node


with create_graph(name="Demo", type=pdlp.digraph, compund=True) as graph:
    with Node("subgraph #A") as subgraph_a:
        a = Node()

    with Node("subgraph #B", style=pdlp.style.filled, color="#00d9ff") as subgraph_b:
        subgraph_a.node.set(shape=pdlp.shape.box, style=pdlp.style.filled, color="#e5ff00")
        b = Node(shapr=pdlp.shape.star)
        d = Node()
        b.connect(b, color='blue')
        b.connect(d, color="#ff0000")

    c = Node()

    a.connect(b, color='red')
    a.connect(c)
    a.connect(d, constraint=False)

    subgraph_a['s'].connect(subgraph_b['n'], label="subgraph_link")


def test_graph_source():
    assert graph.source == """
    digraph {
        compound=true;
        subgraph cluster_A{
        cluster_node_a  [style=invisible, width=0, height=0, label=""];
        { rank=sink; cluster_node_a; }
        a; 
        }

        subgraph cluster_B{
            style=filled;
            color="#00d9ff";
            node [shape=box, style=filled,color="#e5ff00"];
            label = "subgraph #1";
            cluster_node_b  [style=invisible, width=0, height=0, label=""];
            { rank=source; cluster_node_b; }
            b;
            b -> b [color=blue]
            b -> d [color="#ff0000"];
        }


        a -> b [color=red];
        a -> c;
        a -> d [constraint=false,];
        cluster_node_a:s -> cluster_node_b:n [label="subgraph_link" ltail="cluster_A" lhead="cluster_B"];
    }
    """

"""
以上代码是我设计的一个使用案例，请根据以上代码，帮我生成pdlp（python-style dot language parser）。请首先根据graphviz/dot的语法，帮我生成pdlp.style，pdlp.shape等enum数据类型，然后生成`Node`类型，最后生成create_graph函数。

在你完成以上过程后，请创建python环境，看看你的代码是否能够通过`test_graph_source`测试
 """