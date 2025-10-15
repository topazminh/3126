def reverse_array_new(arr):
    if len(arr) == 0:
        return []
    return [arr[-1]] + reverse_array_new(arr[:-1])
