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


def factoLU(A):

    Ls = []

    for i in range(len(A[0]) - 1):
        res = pivotColumn(A, i)
        A, L = res[0], res[1]
        Ls.append(L)
        print()

    L = Ls[0]

    for i in range(1, len(Ls)):
        L = produitMatriciel(Ls[i], L)
        displayMatrice(L)
        print()

    displayMatrice(produitMatriciel(L, A))
    print()
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
                for k in range(len(A[i])):
                    newRow.append(A[i][k] - A[n][k] * coef)
                    L[i][j] = -coef
                A[i] = newRow
                break

    return [A, L]


def main():

    A = [[1, 0, 3], [2, 1, 2], [1, 1, 2]]
    A = factoLU(A)
    displayMatrice(A)


if __name__ == "__main__":
    main()
