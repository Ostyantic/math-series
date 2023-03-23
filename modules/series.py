def fibonacci(n=1):
    """
    Function that takes in a number and calculates the
    term of that number in the fibonacci sequence.
    :param n: nth term in the sequence
    :return: term number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    Function that takes in a number and calculates the
    term of that number in the fibonacci sequence.
    :param n: nth term in the sequence
    :return: term number
    """
    if n <= 0:
        return 2
    elif n == 1:
        return 1



def sum_series(n, start=0, add_to_start=1):
    """

    :param n:
    :param start:
    :param add_to_start:
    :return:
    """
    return n
