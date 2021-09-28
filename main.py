def close10(x, y):
    if (10 - x) < (y - 10):
        return abs(x)
    elif (10 - x) > (y - 10):
        return abs(y)
    else:
        return 0
print(close10(5, 12))