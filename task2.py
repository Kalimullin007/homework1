nums = [4, 1, 7, 7, 3]
nums = sorted(list(set(nums)))
if len(nums) > 1:
    print(nums[-2])
else:
    print('Второго по величине элемента нет.')