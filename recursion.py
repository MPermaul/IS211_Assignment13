def fibonacci(n):
    """Function that takes INT "n" and returns the "nth" number in the fibonacci sequence.
    param: n: A int representing the value from the fibonacci sequence to return
    return: nth: The requested number from the sequence
        """

    # check to see if input value is a integer
    if type(n) != int:
        return 'n must be of type int'

    # check to see if input value is positive    
    if n < 1:
        return 'n must greater or equal to 1'

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
    return: greatest common divisor of both numbers
    """

    # check to see if input valaues are positive integer
    if type(a) != int or type(b) != int:
        return 'n must be an int'
    
    # check to see if b is equal to zero
    if b == 0:
        return a
    
    else:
        return gcd(b, a % b)


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

 
if __name__ == '__main__':
    

    # print displays for some calls to fibonacci function

    print()
    print('Part 1:')
    print('-' * 10)
    print()

    print(fibonacci(0))     # message printed about size
    print(fibonacci('A'))   # message printed about type
    print(fibonacci(2.1))   # message printed about type
    print(fibonacci(1))     # 1
    print(fibonacci(2))     # 1
    print(fibonacci(9))     # 34
    
    # print displays for some calls to gcd function

    print()
    print('Part 2:')
    print('-' * 10)
    print()

    print(gcd(1, 1))        # 1
    print(gcd(100, 25))     # 25
    print(gcd(50, 1000))    # 50
    print(gcd(1, 'a'))      # message printed about type         
    print(gcd(-10, 100))    # 10

    # print displays for some calls to comparTo function

    print()
    print('Part 3:')
    print('-' * 10)
    print()

    print(compareTo('Same Length', 'Same Length'))              # 0
    print(compareTo('String 1 is Longer than', 'String 2'))     # 1
    print(compareTo('String 1', 'is shorter than String 2'))    # -1
