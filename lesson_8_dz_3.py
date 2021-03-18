# Lesson 8 dz 3 Smirnov Artem

def type_logger(func):
    def wrapper(*args, **kwargs):
        n = [f"{func.__name__}({el}: {type(el)})" for el in args] + \
            [f"{func.__name__}({el}: {type(kwargs[el])})" for el in kwargs]
        print(*n, sep=",\n")

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(65, [55, 23], True, "AFROMAN", ds=100.05)
