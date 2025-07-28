import logging

fib_dict = {0: 0, 1: 1}
fib_cache = {}


def nth_fib(n: int) -> int:
    if n in fib_cache:
        logging.info(f"[CACHE HIT] nth_fib({n})")
        return fib_cache[n]
    if n in fib_dict:
        return fib_dict[n]
    else:
        fib_dict[n] = nth_fib(n - 1) + nth_fib(n - 2)
        fib_cache[n] = fib_dict[n]
        return fib_dict[n]
