def output_decorator(name):

    def decorator(func):

        def wrapper(a, b):
            result = func(a, b)

            print("#" * 26)
            print("#", name)
            print("# input:", a, ",", b)
            print("# output:", result)
            print("#" * 26)

        return wrapper

    return decorator


@output_decorator("Adding")
def add(a, b):
    return a + b


add(4, 3)