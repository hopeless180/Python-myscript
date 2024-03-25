from scipy.special import comb

def probability(k):
    return 1 - (comb(3, k) * comb(12, 6-k)) / comb(15, 6)

probs = [probability(k) for k in range(1,4)]
print(probs)