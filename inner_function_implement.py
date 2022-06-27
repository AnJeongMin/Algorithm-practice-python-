def abs_py(x):
    if x < 0:
        x *= -1
    return x

def all_py(iter) -> bool:
    check = True
    for x in iter:
        if not x:
            check = False
    return check

def any_py(iter) -> bool:
    check = False
    for x in iter:
        if x:
            check = True
    return check

def divmod_py(a, b) -> tuple:
    if a < b: a, b = b, a
    quotient = a//b
    remainder = a%b
    return (quotient, remainder)

def enumerate_py(iter) -> list:
    temp = []
    for i in range(len(iter)):
        temp.append((i, iter[i]))
    return temp

def filter_py(func, iter) -> list:
    temp = []
    for x in iter:
        if func(x):
            temp.append(x)
    return temp

def list_py(iter) -> list:
    temp = []
    for x in iter:
        temp.append(x)
    return temp

def set_py(iter) -> set:
    temp = {None} # for generate default set
    for x in iter:
        temp.add(x)
    temp.remove(None)
    return temp

