def add(*args):
    """Return the sum of all numbers provided."""
    return sum(args)

def subtract(*args):
    """Subtract all following numbers from the first one."""
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result
