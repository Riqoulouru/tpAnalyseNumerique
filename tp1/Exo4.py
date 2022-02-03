import numpy as np


def produitMatriciel(m1, m2):
    m = []
    if len(m1[0]) != len(m2):
        return False
    for i in range(len(m1)):
        ligne = []
        for j in range(len(m2[0])):
            element = 0
            for k in range(len(m1[0])):
                element = element + m1[i][k] * m2[k][j]
            ligne.append(element)
        m.append(ligne)
    return m


def displayMatrice(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j], end="\t")
        print()


def transposMToL(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i != j:
                M[i][j] = -M[i][j]

    return M


def factoLU(A):
    Ls = []

    for i in range(len(A[0]) - 1):
        res = pivotColumn(A, i)
        if res is None:
            return None
        A, L = res[0], res[1]
        L = transposMToL(L)
        Ls.append(L)

    L = Ls[0]

    for i in range(1, len(Ls)):
        L = produitMatriciel(L, Ls[i])

    return A


def pivotColumn(A, n):
    L = []
    for i in range(len(A)):
        l = []
        for j in range(len(A[0])):
            if i == j:
                l.append(1)
            else:
                l.append(0)
        L.append(l)

    for i in range(len(A)):
        for j in range(len(A[0])):

            if j == n and i > n:
                newRow = []
                coef = A[i][j] / A[n][j]

                if abs(coef) < 0.0000000001:
                    return None

                for k in range(len(A[i])):
                    newRow.append(A[i][k] - A[n][k] * coef)
                    L[i][j] = -coef
                A[i] = newRow
                break

    return [A, L]


def main():
    A = [[1, 0, 3], [2, 1, 2], [1, 1, 2]]
    A = factoLU(A)
    if A is None:
        print("Error, coef en dessous de 10^-10")
    else:
        displayMatrice(A)


if __name__ == "__main__":
    main()
