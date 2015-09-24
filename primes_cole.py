# Author: Cole Howard
#
# Creates a list from 1 to n of integers.
# Then creates a new list of positive results from is_prime

from math import floor, sqrt


def is_prime(y):
    """Check if a number is prime
    
    Args:
        y - an integer

    Return:
        a boolean
    """
    for i in range(2, floor(sqrt(y))+1):
        if y % i == 0:
            return False
    return True
        

def list_primes(n):
    """ Makes a list of integers up to n)

    Args:
        n - an integer

    Returns:
        a list
    """
    lst_to_test = [x+1 for x in range(n)]
    ans_list = [y for y in lst_to_test if (y != 1) and(is_prime(y))]
    return ans_list


if __name__ == '__main__':
    
    assert list_primes(1) == []
    assert list_primes(2) == [2]
    assert list_primes(7) == [2, 3, 5, 7]
    assert list_primes(9) == list_primes(7)
    n = eval(input("Let's have an int, please. "))
    print(list_primes(n))



