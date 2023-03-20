def min_of_two(x, y):
    if x < y:
        return x
    else:
        return y


def min_of_three(x, y, z):
    return min_of_two(x, min_of_two(y, z))


print(min_of_three(3, 5, 9))
