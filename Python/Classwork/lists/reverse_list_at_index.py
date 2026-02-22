def reverse_list_at_index(lst, index):
    """Reverse the list from the given index onward."""
    if index < 0 or index >= len(lst):
        return "Index out of range"
    return lst[:index] + lst[index:][::-1]
