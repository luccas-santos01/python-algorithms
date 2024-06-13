def merge_sort(input_string):
    if len(input_string) <= 1:
        return input_string
    mid = len(input_string) // 2
    left_half = merge_sort(input_string[:mid])
    right_half = merge_sort(input_string[mid:])
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    if left:
        merged.extend(left[left_index:])
    if right:
        merged.extend(right[right_index:])
    return "".join(merged)


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return ("", "", False)
    first_string = first_string.lower()
    second_string = second_string.lower()
    sorted_first_string = merge_sort(first_string)
    sorted_second_string = merge_sort(second_string)
    result = sorted_first_string == sorted_second_string
    return (sorted_first_string, sorted_second_string, result)
