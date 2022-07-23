import time


def timer(fn):
    def inner_function(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print(f"The '{fn.__name__}' took {end - start} to complete")

    return inner_function


@timer
def add(a, b):
    return a * b


print(add(3, 5))
