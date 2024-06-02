def linear_search(data, target):
    for idx, val in enumerate(data):
        if val == target:
            return idx
    return -1

data = [4, 5, 2, 7, 1, 8]
target = 1
result = linear_search(data, target)
if result == -1:
    print("item not found")
else:
    print(f"item found on position {result}")