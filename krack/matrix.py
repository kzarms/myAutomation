import numpy as np

m = np.array([[1, 2], [3, 4]], int)

result = np.rot90(m)
print(result)


############# Rotate matrix #################

matrix =[
            [1,  2,  3,  4],
            [5,  6,  7,  8],
            [9,  10, 11, 12],
            [13, 14, 15, 16]
        ]
def rotateMartix90(matrix):
    if not len(matrix):
        return

    top = 0
    btt = len(matrix) - 1

    left = 0
    right = len(matrix[0]) - 1

    while left < right and top < btt:
        # Store the element
        prev = matrix[top+1][left]

        for i in range(left, right + 1):
            curr = matrix[top][i]
            matrix[top][i] = prev
            prev = curr

        top += 1

        for i in range (top, btt + 1):
            curr = matrix[i][right]
            matrix[btt][i] = prev
            prev = curr

        right -= 1

        for i in range(right, left-1, -1):
            curr = matrix[btt][i]
            matrix[i][right] = prev
            prev = curr

        btt -= 1

        for i in range(btt, top-1, -1):
            curr = matrix[i][left]
            matrix[i][left] = prev
            prev = curr

        left += 1

    return matrix

print(rotateMartix90(matrix))
