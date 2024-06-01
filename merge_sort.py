def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Dind the midpoint of the list and divide into sublists
    Conquer: Recursive sort the sublists created in prev step
    Combine: Merge the sorted sublists in prev step
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Retrun two sublists - left and right
    """

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right