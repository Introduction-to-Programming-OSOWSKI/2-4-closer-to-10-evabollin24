def close10(x, y):
    if (10 - x) < (abs(10 - y)):
        return x
    elif (10 - x) > (abs(10 - y)):
        return y
    else:
        return 0