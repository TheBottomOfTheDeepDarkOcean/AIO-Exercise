def exercise4(source, target):
    distance = []
    for index in range(len(source) + 1):
        row = [0] * (len(target) + 1)
        distance.append(row)

    for index in range(len(source) + 1):
        distance[index][0] = index
    for index in range(len(target) + 1):
        distance[0][index] = index

    del_cost = 0
    insert_cost = 0
    replace_cost = 0

    for index in range(1, len(source) + 1):
        for index2 in range(1, len(target) + 1):
            if source[index - 1] == target[index2 - 1]:
                distance[index][index2] = distance[index - 1][index2 - 1]
            else:
                del_cost = distance[index - 1][index2]
                insert_cost = distance[index][index2 - 1]
                replace_cost = distance[index - 1][index2 - 1]

                if del_cost <= insert_cost and del_cost <= replace_cost:
                    distance[index][index2] = del_cost + 1
                elif insert_cost <= del_cost and insert_cost <= replace_cost:
                    distance[index][index2] = insert_cost + 1
                else:
                    distance[index][index2] = replace_cost + 1

    edit_distance = distance[len(source)][len(target)]
    return edit_distance


if __name__ == "__main__":
    source = 'hola'
    target = 'hello'
    print(exercise4(source, target))
