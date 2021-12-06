def list_sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + list_sum(list[1:])

if __name__ == "__main__":
    print("Test list sum recursion function")
    print(list_sum([1, 3, 5, 7, 9, 11]))
