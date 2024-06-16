def max_kernel(num_list, k):
    if k > len(num_list):
        return []

    result_list = []
    for i in range(len(num_list) - k + 1):
        window = num_list[i:i + k]
        result_list.append(max(window))

    return result_list


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))
