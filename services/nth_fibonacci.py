fib_dict = {0: 0, 1: 1}
def nth_fib(n: int) -> int:
    """
    Return the n-th fibonacci number given input n.    :param n: input param (int)
    :return: fibonacci(n)
    >>> nth_fib(0)
    0
    >>> nth_fib(1)
    1
    >>> nth_fib(8)
    21
    >>> nth_fib(10)
    55
    >>> nth_fib(4)
    3
    """
    if n in fib_dict:
        return fib_dict[n]
    else:
        fib_dict[n] = nth_fib(n - 1) + nth_fib(n - 2)
        return fib_dict[n]