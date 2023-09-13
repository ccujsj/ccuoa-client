import math
import numpy as np

def jaccard_similarity(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    similarity = intersection / union
    return similarity

def cosine_similarity(list1, list2):
    dot_product = sum([list1[i]*list2[i] for i in range(len(list1))])
    norm1 = math.sqrt(sum([x**2 for x in list1]))
    norm2 = math.sqrt(sum([x**2 for x in list2]))
    similarity = dot_product / (norm1 * norm2)
    return similarity

def variance_max(data:list):
    # variance max val
    # 计算所有项的距离方差
    variances = []
    for i in range(len(data)):
        distances = [abs(data[i] - x) for x in data]
        variance = np.var(distances)
        variances.append(variance)

    # 找到距离方差相差最大的两个项
    max_diff = -1
    max_diff_indices = (-1, -1)
    for i in range(len(variances)):
        for j in range(i + 1, len(variances)):
            diff = abs(variances[i] - variances[j])
            if diff > max_diff:
                max_diff = diff
                max_diff_indices = (i, j)
    # 距离方差最大的项
    item1, item2 = data[max_diff_indices[0]], data[max_diff_indices[1]]
    return item1,item2
def in_seq_max(data:list):
    # time or sequence independent max val
    max_v = data[0]
    for i in data:
        if i > max_v:
            max_v = i
    return max_v

