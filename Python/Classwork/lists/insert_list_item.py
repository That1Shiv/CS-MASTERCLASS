def insert_list_item(lst, start, end, items):
    """Replace items in lst from start to end with the given items."""
    lst[start:end] = items
    return lst
