from services.nth_fibonacci import nth_fib

def fib(n: int) -> int:
    res = nth_fib(n) # taken from services/nth_fibonacci.py
   # save_request(operation="fibonacci", input=n, output=res)
    return res