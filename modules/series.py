def fibonacci(n=1):
    """
    Function that takes in a number and calculates the
    term of that number in the Fibonacci sequence.
    :param n: nth term in the sequence
    :return: term number
    """
    # print(fibonacci(n))

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n=1):
    """
    Function that takes in a number and calculates the
    term of that number in the Lucas sequence.
    :param n: nth term in the sequence
    :return: term number
    """
    # print(lucas(n))

    if n <= 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)


def sum_series(n, start=0, add_to_start=1):
    """
    Function that mimics the logic of the fibonacci and lucas functions;
    Takes in a number and calculates the term of that number
    in the sequence depending on the start and add_to_start params
    :param n: nth term in the sequence
    :param start: starting number in the sequence
    :param add_to_start: number added to start in beginning of sequence
    :return:
    """
    # print(n, start, add_to_start)

    if n <= 0 <= start and add_to_start:
        return start
    elif n <= 0 and start <= 0 and add_to_start <= 0:
        return 0
    elif n == 1:
        return add_to_start
    else:
        return sum_series(n - 1, start, add_to_start) + sum_series(n - 2, start, add_to_start)
