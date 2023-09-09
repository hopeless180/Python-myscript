from scipy.special import comb

def calculate_probability(n):
    p = (n**2)+2*n*(1-n)  # 选手赢得一场比赛的概率
    q = 1 - p  # 选手输掉一场比赛的概率
    probability = 0

    for k in range(9, 12):
        probability += comb(11, k) * (p**k) * (q**(11-k))

    return probability

# 假设选手的单局胜率为0.6
win_rate = 0.6
result = calculate_probability(win_rate)
print("选手晋级的概率为:", result)