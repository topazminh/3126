def recursive_search(arr, x, index=0):
    if index >= len(arr):
        return -1  # Không tìm thấy
    if arr[index] == x:
        return index  # Tìm thấy ở vị trí index
    return recursive_search(arr, x, index + 1)
