HW_SOURCE_FILE = __file__


def insert_items(lst, entry, elem):
    """Inserts elem into lst after each occurence of entry and then returns lst.

    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> double_lst = [1, 2, 1, 2, 3, 3]
    >>> double_lst = insert_items(double_lst, 3, 4)
    >>> double_lst
    [1, 2, 1, 2, 3, 4, 3, 4]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    >>> # Ban creating new lists
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'insert_items',
    ...       ['List', 'ListComp', 'Slice'])
    True
    """
    '''
    i = 0
    length = len(lst)
    while True:
        if i == length:
            return lst
        if lst[i] == entry:
            # 这个方法需要确保插入的是一个iterator, 所以是插入[elem], 如果插入elem会报错
            lst[i+1:i+1] = [elem]
            length += 1
            i += 1
        i += 1
    '''
    i = 0
    length = len(lst)
    while True:
        if i == length:
            return lst
        if lst[i] == entry:
            lst.insert(i + 1, elem)
            length += 1
            i += 1
        i += 1



def count_occurrences(t, n, x):
    """Return the number of times that x appears in the first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s2, 3, 10)
    2
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(s, 1, 3)
    1
    >>> count_occurrences(s, 4, 2)
    3
    >>> next(s)
    2
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> count_occurrences(s2, 6, 6)
    2
    """
    result = 0
    while n > 0:
        if next(t) == x:
            result += 1
        n -= 1
    return result


def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row.
    Iterate through the items such that if the same iterator is passed into
    the function twice, it continues in the second call at the point it left
    off in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    freq = 0
    pre = next(t)
    while True:
        cur = next(t)
        if cur == pre:
            freq += 1
            if freq == k:
                return pre
        else:
            freq = 1
            pre = cur
