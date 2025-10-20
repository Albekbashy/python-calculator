def add(*args):
    """Return the sum of all numbers provided."""
    return sum(args)

def subtract(*args):
    print("Running improved subtract function")
    result = args[0]
    for num in args[1:]:
        result -= num
    return result
