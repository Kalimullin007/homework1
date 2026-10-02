nums = [1, 2, 3, 4, 5, 6, 4]
target = 7
nums2 = [i for i in nums if i * 2 != target]
used = []
pairs = []
for i in nums:
    if i * 2 == target and nums.count(i) >= 2 and i not in used:
        pairs.append([i, target - i])
        used.append(i)
    elif target - i in nums2 and i not in used and target - i not in used:
        pairs.append([i, target - i])
        used.append(target - i)
        used.append(i)
for pair in pairs:
    print(tuple(pair))