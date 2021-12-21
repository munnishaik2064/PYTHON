def add(x):
    for i in range(x):
        value = i+x
        yield value
output=add(5)
next(output)