# 定义拼图
pieces = [
    [[1, 1], [1, 1]],
    [[1], [1], [1], [1]],
    [[1, 1, 1], [0, 1, 0]],
    [[0, 1], [1, 1], [1, 0]],
    [[0, 1], [1, 1], [0, 1]]
]

# 定义搜索函数
def dfs(array, pieces_left):
    # 找到一个可行的解，停止搜索
    if not pieces_left:
        return True
    
    # 依次尝试每个拼图
    for piece in pieces_left:
        for i in range(len(array) - len(piece) + 1):
            for j in range(len(array[0]) - len(piece[0]) + 1):
                # 检查是否能把拼图放在这个位置
                can_place = True
                for pi in range(len(piece)):
                    for pj in range(len(piece[0])):
                        if piece[pi][pj] == 1 and array[i+pi][j+pj] == 0:
                            can_place = False
                            break
                    if not can_place:
                        break
                
                # 如果能放，就放进去，然后继续搜索
                if can_place:
                    for pi in range(len(piece)):
                        for pj in range(len(piece[0])):
                            if piece[pi][pj] == 1:
                                array[i+pi][j+pj] = 2
                    pieces_left.remove(piece)
                    if dfs(array, pieces_left):
                        return True
                    pieces_left.append(piece)
                    for pi in range(len(piece)):
                        for pj in range(len(piece[0])):
                            if piece[pi][pj] == 1:
                                array[i+pi][j+pj] = 0
    
    # 所有拼图都试过了，没有找到可行解
    return False

# 初始化数组和拼图
array = [
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0]
]

pieces_left = [p.copy() for p in pieces]

# 开始搜索
if dfs(array, pieces_left):
    print("可以塞进拼图")
else:
    print("无法塞进拼图")


for row in array:
    print(row)  

