from math import sqrt
def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    b=sqrt(a)
    return b%(int(b))==0
print(main(121))