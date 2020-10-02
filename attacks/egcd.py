#Extended Eucledian Algorithm
# with input from https://github.com/lapets/egcd, Lisenced under MIT


def egcd(a, b):
    '''
    Given two integers (a, b), returns (gcd(a, b), m, n) such that
    a*m + b*n = gcd(a,b).
    '''   

    (x0, x1, y0, y1) = (1, 0, 0, 1)
    while b != 0:
        (q, a, b) = (a // b, b, a % b)
        (x0, x1) = (x1, x0 - q * x1)
        (y0, y1) = (y1, y0 - q * y1)
    return (a, x0, y0)
