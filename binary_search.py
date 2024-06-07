import random

def binary_search(data, target):
    low_idx = 0
    high_idx = len(data) - 1
    

    while(low_idx <= high_idx):
        middle_idx = (high_idx - low_idx) // 2

        if data[middle_idx] == target:
            return middle_idx

        if data[middle_idx] > target:
            high_idx = middle_idx - 1
        else:
            low_idx = middle_idx + 1

    return -1

n = 10
max_val = 100
# data = [random.randint(1, max_val) for i in range(n)]
#data.sort()
data = [1,2,3,4,5,6]
print("Data: ", data)

target = int(input("Enter target value: "))
target_pos = binary_search(data, target)
if target_pos == -1:
    print("Not in the list")
else:
    print("Found at index ", target_pos)