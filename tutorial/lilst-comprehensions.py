# LINK:  https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# Marc D. Holman
# 9 / 26 / 2022

#  Let's learn about list comprehensions!
#  You are given three integers x, y, z representing the dimensions of a cuboid
#  along with an integer n. Print a list of all possible coordinates given by (i, j, k) on
#  a 3D grid where the sum i + j + k of is not equal to n.

#  USE LIST COMPREHENSIONS

from itertools import permutations

if __name__ == '__main__':
    X = int(input())
    Y = int(input())
    Z = int(input())
    N = int(input())

    # combinations = permutations([x, y, z], 3)
    # result = [index for index if permutations[index].sum() != n]
    result = [[i, j, k] for i in range(X + 1) for j in range(Y + 1) for k in range(Z + 1) if i + j + k != N]

    # result = ()

    # combinations = list(permutations([1, 2, 3], 3))

    # for index in range(len(combinations)):
    #     total = sum(combinations[index])
    #     if total != N:
    #         new_tuple = result + (combinations(index))

    print(result)

    # print(ans)