def is_palindrome(number):
    return True if str(number) == str(number)[::-1] else False
    pass
    
def error_test(min,max):
    if min>max:
        raise ValueError("min must be <= max")
    pass
    
def getFirstPalindrome(numbers, products):
    for value in products:
        if is_palindrome(value):
            multiples = []
            multiple_couples = []
            for val in numbers:
                if val not in multiples and value % val == 0 and value/val in numbers:
                    multiples.append(val)
                    multiples.append(value//val)
                    multiple_couples.append([val, value//val])
            if len(multiple_couples) > 0:
                print((value, multiple_couples))
                return ((value, multiple_couples))
    return ((None,[]))
    pass
    
def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    error_test(min_factor, max_factor)
    numbers = range(min_factor, max_factor+1)
    products = range((max_factor**2), (min_factor**2)-1, -1)
    return getFirstPalindrome(numbers, products)
    pass


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    error_test(min_factor, max_factor)
    numbers = range(min_factor, max_factor+1)
    products = range((min_factor**2),(max_factor**2))
    return getFirstPalindrome(numbers, products)
    pass
