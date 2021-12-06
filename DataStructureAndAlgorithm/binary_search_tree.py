
def binary_search(data, target, low_index, high_index):

    if low_index > high_index:
        return False
    else:
        mid = (low_index + high_index) // 2
        if target == data[mid]:
            # return true if find ratget in data at midle position
            return True
        elif target < data[mid]:
            # search left
            return binary_search(data, target, low_index, mid - 1)
        else:
            # search right
            return binary_search(data, target, mid + 1, high_index)


if __name__ == "__main__":
    print("Test binary search tree")
    data = [1, 2, 5, 6, 8, 9, 10, 13, 14, 15, 20, 23, 25, 28, 30, 31]
    print(binary_search(data, 2, 0, len(data) - 1))
    print(binary_search(data, 8, 0, len(data) - 1))
    print(binary_search(data, 16, 0, len(data) - 1))
    print(binary_search(data, 25, 0, len(data) - 1))
    
