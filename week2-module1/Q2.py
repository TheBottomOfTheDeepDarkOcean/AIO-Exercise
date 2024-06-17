def exercise2(my_str):
    my_dict = {}
    for char in my_str:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict


if __name__ == "__main__":
    my_str = 'CielSensei'
    print(exercise2(my_str))
