def gcd(m, n):
    """Returns the largest common devisor for m and n.

    k, m, and n are all positive integers.

    >>> gcd(12,8)
    4
    >>> gcd(20, 12)
    4
    >>> gcd(16, 8)
    8
    >>> gcd(2, 16)
    2
    >>> gcd(5, 5)
    """
    if n % m == 0:
        return m
    elif m < n:
        return gcd(n,m)
    else:
        return gcd(m-n, n)
