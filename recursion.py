def fibonacci(n):
    """Function that takes INT "n" and returns the "nth" number in the fibonacci sequence.
    param: n: A int representing the value from the fibonacci sequence to return
    return: nth: The requested number from the sequence
        """

    # check to see if input value is a integer
    if type(n) != int:
        raise TypeError('n must be a positive int')

    # check to see if input value is positive    
    if n < 1:
        raise ValueError('n must be a positive int')

    # if 1 was passed in as nth
    if n == 1: 
        return 1
    
    # if 2 was passed in as the nth
    elif n == 2:
        return 1
    
    # all other values greater than 2
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


def gcd(a, b):
    """Function that takes in two integers and returns the greatest common divisor.
    param: a: first number 
    param: b: second number 
    return: gcd: greatest common divisor of both numbers
    """

    # check to see if input valaues are positive integer
    if type(a) != int or type(b) != int:
        raise TypeError('n must be a positive int')
    
    # check to see if b is equal to zero
    if b == 0:
        return a
    
    else:
        return gcd(b, a%b)


def compareTo(s1, s2):
    """Function that takes in two strings and returns an output based on a length comparison.
    param: s1: First string to compare.
    param: s2: Second string to compare.
    Returns: 0 if strings are of equal lenght, 1 if the s1 is longer, -1 if the s2 is longer.
    """
    
    # if both strings don't have any letters in them, they should be the same length
    if s1 == '' and s2 == '':
        return 0
    
    # if string 1 is blank, but not string 2
    elif s1 == '':
        return -1
    
    # if string 2 is blank, but not string 1
    elif s2 == '':
        return 1
    
    else:
        # call compareTo and pass in both strings starting at index 1
        return compareTo(s1[1:], s2[1:])
