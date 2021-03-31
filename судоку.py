import itertools as it

import pycosat

n = 9
n3 = 3
clauses = []


def varnum(i, j, k):
    assert i in range(n) and j in range(n) and k in range(n)
    return i * n * n + j * n + k + 1


def f(t):  # из 0..8 пару 0..3,0..3
    return t // n3, t % n3


A = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        if A[i][j] != 0:
            clauses.append([varnum(i, j, A[i][j]-1)])
#


# each row contains at least one queen |
for k in range(n):
    for i in range(n):
        clauses.append([varnum(i, j, k) for j in range(n)])
# ---- чемто
for k in range(n):
    for j in range(n):
        clauses.append([varnum(i, j, k) for i in range(n)])

# each row contains at most one queen
for i in range(n):
    for j in range(n):
        for (k1, k2) in it.combinations(range(n), 2):
            clauses.append([-varnum(i, j, k1), -varnum(i, j, k2)])

for k in range(n):
    for t in range(n):
        arr = []
        for y in range(n):
            p1, p2 = f(t)
            l1, l2 = f(y)
            arr.append(varnum(p1 * n3 + l1, p2 * n3 + l2, k))
        clauses.append(arr)
# each column contains at most one queen
# for j in range(n):
#     for (i1, i2) in it.combinations(range(n), 2):
#         clauses.append([-varnum(i1, j), -varnum(i2, j)])
# no two queens stay on the same diagonal
# for (i1, i2) in it.combinations(range(n), 2):
#     for (j1, j2) in it.product(range(n), repeat=2):
#         if i2 - i1 == abs(j2 - j1):
#             clauses.append([-varnum(i1, j1), -varnum(i2, j2)])
# print(clauses)
assignment = pycosat.solve(clauses)
# print(assignment)
if assignment == 'UNSAT':
    print('NO')
else:
    print('YES')
    for i in range(n):
        # print("| ", end="")
        for j in range(n):
            for k in range(n):
                assert abs(assignment[varnum(i, j, k) - 1]) == varnum(i, j, k)
                if assignment[varnum(i, j, k) - 1] > 0:
                    print(k + 1, "", end="")
                # else:
            print("", end="")
        print("")
