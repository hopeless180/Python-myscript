from tkinter import filedialog
import os,shutil,time
import networkx as nx

# 创建一个空图
G = nx.DiGraph()

selectedDirectory = filedialog.askdirectory()

G.add_node(os.path.basename(selectedDirectory))

for root, dirs, files in os.walk(selectedDirectory):
    for dir in dirs:
        level = root.replace(selectedDirectory, '').count(os.sep)
        print(f'root: {root}, folder: {dir}, level: {level}')
        G.add_node(os.path.basename(dir))
        G.add_edge(os.path.basename(root), os.path.basename(dir))

print(nx.info(G))