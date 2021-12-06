
def recursion_list_sum(list):
    total = 0
    for element in list:
        if type(element) == type([]):
            total = total + recursion_list_sum(element)
        else:
            total = total + element
    return total


if __name__ == "__main__":
    print("Test recursion list sum")
    data = [1, 2, 3, [5, 6], 7, [3, 2], 8]
    print(recursion_list_sum(data))
