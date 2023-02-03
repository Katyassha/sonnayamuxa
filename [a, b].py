def summ_recursive(a, b):
    if a == b:
        return a
    else:
        print(a)
        return summ_recursive(a + 1, b)


def interval_recursive(a, b):
    if a == b:
        return a
    else:
        return a + interval_recursive(a + 1, b)


c = input()
d = input()
print(summ_recursive(c, d))
print(interval_recursive(c, d))
