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

class node:
    def __init__(self, name = ""):
        self.nextNode = None
        self.name = name
    def setNextNode(self, nextNode):
        self.nextNode = nextNode
    def getNextNode(self):
        return self.nextNode
    
    


def main():
    return 0

if __name__ == '__main__':
    start = node("开始")
    end = node("结束")
    start.setNextNode(end)
    print(start.nextNode.name.center(6))
    print("|".center(6))
    print("|".center(6))
    print("|".center(6))
    print("|".center(6))
    print(start.name.center(6))