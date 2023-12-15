def main(a):
    """
    Check the natural number. Natural numbers are numbers used in counting.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    b=(a>=1 and a<=9 and a*1.0==int(a))
    return b
print(main(7))