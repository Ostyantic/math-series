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


def lucas(n=1):
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
    else:
        return lucas(n - 2) + lucas(n - 1)


def sum_series(n, start=0, add_to_start=1):
    """
    Function that mimics the logic of the fibonacci and lucas functions;
    takes in a number and calculates the term of that number
    in the sequence depending on the start and add_to_start params
    :param n: nth term in the sequence
    :param start: starting number in the sequence
    :param add_to_start: number added to start in beginning of sequence
    :return:
    """

    if n <= 0:
        return start
    elif n == 1:
        return start + add_to_start

    return n
