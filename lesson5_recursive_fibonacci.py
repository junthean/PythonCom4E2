'''Exercise 5: Recursive Fibonacci with Memoization

- Implements a recursive function `fibonacci(n)`.
- Uses a dictionary cache to memoize results for optimal performance.
- Prints the Fibonacci sequence for n = 0..10.
'''

def fibonacci(n, cache=None):
    """Return the nth Fibonacci number using recursion with memoization.

    Args:
        n (int): The index (non‑negative) of the Fibonacci number to compute.
        cache (dict, optional): Dictionary used to store previously computed values.
                                 If None, a new cache is created.
    Returns:
        int: The nth Fibonacci number.
    """
    if cache is None:
        cache = {}
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Check cache
    if n in cache:
        return cache[n]
    # Recursive computation
    result = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    cache[n] = result
    return result

if __name__ == "__main__":
    # Print Fibonacci sequence for n = 0..10
    for i in range(0, 11):
        print(f"F({i}) = {fibonacci(i)}")
