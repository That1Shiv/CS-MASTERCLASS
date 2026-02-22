def first_non_repeated(lst):
    """Return the first non-repeated item in the list."""
    for item in lst:
        if lst.count(item) == 1:
            return item
    return None
