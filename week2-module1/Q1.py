def sliding_window(num_list, k):
    result = []
    for index in range(len(num_list) - k + 1):
        max_num = max(
            [num_list[index], num_list[index + 1], num_list[index + 2]])
        result.append(max_num)
    return result


if __name__ == "__main__":
    num_list = [1, 2, 3, 4, 5, 6]
    k = 3
    print(sliding_window(num_list, k))
