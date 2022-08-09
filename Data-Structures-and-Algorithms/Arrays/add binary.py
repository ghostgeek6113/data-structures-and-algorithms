def add_binary(a, b):
    """
    Given two binary strings a and b, return their sum as a binary string.
    :type a: str
    :type b: str
    :rtype: str
    """
    a = int(a, 2)
    b = int(b, 2)
    c = str(format((a + b), "b"))
    return c
