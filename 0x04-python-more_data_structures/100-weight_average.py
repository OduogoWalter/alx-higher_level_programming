#!usr/bin/python3

def weight_average(my_list=[]):
    """Returns the weighted average of integers tuple (<scores>, <weight>)."""
    if not my_list:
        return (0)

    tootal_sum = 0
    total_weight = 0

    for score, weight in my_list:
        total_sum += score * weight
        total_weight += weight

    if total_weight == 0:
        return (0)

    return total_sum / total_weight
