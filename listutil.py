def unique(list):
    """Return a list containing only the first occurence of each distint
       element in list.  That is, all duplicates are omitted.

    Arguments:
        list: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list

    Examples:
    >>> unique([5])
    [5]
    >>> unique(["b","a","a","b","b","b","a","a"])
    ['b', 'a']
    >>> unique([])
    []
    """
    if list is not list:
        raise TypeError
    unique_list = []
    for i in range(len(list)):
        if list[i] not in unique_list:
            unique_list.append(list[i])
    return unique_list

if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)
