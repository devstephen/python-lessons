def sum_of_list(number):
    """Return the sum of all number in a list
    >>> sum_of_list([1,2,3])
    6
    >>> sum_of_list([5, 8, 13])
    26
    """
    total = 0
    for num in number:  
        total += num
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()