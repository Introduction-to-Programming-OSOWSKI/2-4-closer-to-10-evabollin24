def close10(x, y):
    if (10 - x) < (10 - y):
        return abs(x)
    elif (10 - x) > (10 - y):
        return abs(y)
    else:
        return abs(0)