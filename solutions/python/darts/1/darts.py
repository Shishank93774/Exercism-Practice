def score(x, y):
    squared_distance = x*x + y*y
    if squared_distance > 100:
        return 0
    elif squared_distance > 25:
        return 1
    elif squared_distance > 1:
        return 5
    return 10
