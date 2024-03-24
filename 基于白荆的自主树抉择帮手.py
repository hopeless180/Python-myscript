class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs():
    pass

def initgraph():
    import networkx as nx
    import matplotlib.pyplot as plt

    # 创建一个有向图
    G = nx.DiGraph()

    # 添加节点
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)

    # 添加边
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    G.add_edge(4, 1)

    # 绘制图形
    pos = nx.spring_layout(G)  # 设置节点位置
    nx.draw(G, pos, with_labels=True, arrows=True)
    plt.show()


def main():
    return 0

if __name__ == '__main__':
    initgraph()
    pass