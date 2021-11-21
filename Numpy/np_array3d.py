import numpy as np

if __name__ == "__main__":

    arr_page1 = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 1, 4]
    ]

    arr_page2 = [
        [4, 1, 8],
        [9, 3, 7],
        [8, 5, 4]
    ]

    arr_page3 = [
        [8, 1, 3],
        [4, 7, 2],
        [2, 9, 7]
    ]

    all_page = [arr_page1, arr_page2, arr_page3]
    arr3d = np.array(all_page)

    print(arr3d.ndim)
    print(arr3d[2][1][1]) # deep , row, column
