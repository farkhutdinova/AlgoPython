def selection_sort(data):
    for i in range(len(x) - 1):
        min_idx = i
        for j in range(i + 1, len(x)):
            if data[j] < data[min_idx]:
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]

        

x = [3, 2, 1, 5, 4]
print(x)
selection_sort(x)
print(x)

print(all(x[i] <= x[i + 1] for i in range(len(x) - 1)))