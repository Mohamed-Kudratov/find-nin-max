# print(min([1, 26, 8, 4, 1, 9, 2, 5]))
# print(max([1, 26, 8, 4, 1, 9, 2, 5]))

def number(x):
    min_n = max_n = x[0]
    for i in x[1:]:
        if i < min_n:
            min_n = i
        else:
            if i > max_n:
                max_n = i
    return (min_n, max_n)


print(number([1, 26, 8, 4, 1, 9, 2, 5]))
