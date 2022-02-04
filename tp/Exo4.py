import math

import numpy as np

# fonction pour transposer les lignes où la diagonal est = 0 avec une pas égale à 0
def transposAllIfNeeded(A, b):

    copyA = A
    copyB = b

    for i in range(len(A)):
        for j in range(len(A[0])):

            if i == j:
                if A[i][j] == 0:
                    for k in range(len(A)):
                        if A[len(A) - k - 1][j] != 0:
                            temp = copyA[i]
                            copyA[i] = A[len(A) - k - 1]
                            copyA[len(A) - k - 1] = temp

                            temp2 = copyB[i]
                            copyB[i] = b[len(A) - k - 1]
                            copyB[len(A) - k - 1] = temp2
                            break

    return copyA, copyB

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
            if abs(A[i][j]) < 0.000000000001:
                print(0, end="\t")
            else:
                print(A[i][j], end="\t")
        print()


def displayMatriceColumnTension(A):
    for i in range(len(A)):
        print("T", i+1," =  ", A[i], end="\n")


# Après réponse pour petit a) (résolution de x (b) directement pour le que le petit c) soit plus simple)
def convertMToL(M):
    for i in range(len(M)):
        for j in range(len(M[0])):

            if i != j:
                M[i][j] = -M[i][j]

    return M


def factoLU(A, b):
    Ls = []

    # pour chacune des colones
    for i in range(len(A[0]) - 1):
        res = pivotColumnInf(A, i, b)
        if res is None:
            return None
        A, L, b = res[0], res[1], res[2]

        L = convertMToL(L)
        Ls.append(L)

    L = Ls[0]

    for i in range(1, len(Ls)):
        L = produitMatriciel(L, Ls[i])

    return L, A, b


def pivotColumnInf(A, n, b):
    # créer le M de base
    M = []
    for i in range(len(A)):
        l = []
        for j in range(len(A[0])):
            if i == j:
                l.append(1)
            else:
                l.append(0)
        M.append(l)

    for i in range(len(A)):
        for j in range(len(A[0])):

            if j == n and i > n:
                newRow = []
                coef = A[i][j] / A[n][j]

                # vérifier si pas inférieur à 10^-10
                if A[i][j] != 0 and abs(coef) < 0.0000000001:
                    return None

                # pré-résolution de x
                b[i] = b[i] - b[n] * coef

                # annuler (0) les colonnes en dessous
                for k in range(len(A[i])):
                    newRow.append(A[i][k] - A[n][k] * coef)
                    M[i][j] = -coef
                A[i] = newRow
                break

    return [A, M, b]


# Après réponse pour petit b)

def drLU(C, b):
    A = []

    # Pour chacune des colones, utiliser le pivot pour mettre les éléments à 0 sauf sur la diagonal
    for n in range(len(C[1]) - 1):
        res = pivotColumnSup(C[1], len(C[1]) - n - 1, b)
        A, b = res[0], res[1]

    return A, b


def pivotColumnSup(A, n, b):
    for i in range(len(A)):
        for j in range(len(A[0])):

            if len(A[0]) - j - 1 == n and len(A) - i - 1 < n:
                newRow = []
                # Définir le coef
                coef = A[len(A) - i - 1][len(A[0]) - j - 1] / A[n][len(A[0]) - j - 1]

                # Traiter la matrice de résultat
                b[len(A) - i - 1] = b[len(A) - i - 1] - b[n] * coef

                # Traiter la matrice pour la diagonaliser supérieur
                for k in range(len(A[len(A) - i - 1])):
                    newRow.append(A[len(A) - i - 1][k] - A[n][k] * coef)
                A[len(A) - i - 1] = newRow

    return A, b


# Après réponse pour petit b)
def solveLU(A, b):

    res = transposAllIfNeeded(A, b)
    A, b = res[0], res[1]

    displayMatrice(A)
    print()

    res = factoLU(A, b)

    if res is None:
        print("Error, coef en dessous de 10^-10")
        return None
    else:
        L, U, b = res[0], res[1], res[2]

        print("L : ")
        displayMatrice(L)
        print()

        print("U : ")
        displayMatrice(U)
        print()

        res = drLU((L, U), b)
        A, b = res[0], res[1]

        print("A après pivot de Gauss: ")
        displayMatrice(A)

        print()
        displayMatriceColumnTension(b)
        return b


def main():

    A = [
        [-math.cos(math.pi / 6), 0, math.cos(math.pi / 4), 1, 0, 0, 0, 0, 0, 0, 0],
        [-math.sin(math.pi / 6), 0, math.sin(math.pi / 4), 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, -math.cos(math.pi / 4), 0, math.cos(math.pi / 4), 1, 0, 0, 0, 0, 0],
        [0, 0, math.sin(math.pi / 4), 0, math.sin(math.pi / 4), 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, -math.cos(math.pi / 4), 0, math.cos(math.pi / 4), 1, 0, 0, 0],
        [0, 0, 0, 0, -math.sin(math.pi / 4), 0, -math.sin(math.pi / 4), 0, 0, 0, 0],
        [0, 0, 0, 0, 0, -1, -math.cos(math.pi / 4), 0, math.cos(math.pi / 4), 1, 0],
        [0, 0, 0, 0, 0, 0, math.sin(math.pi / 6), 0, math.sin(math.pi / 4), 0, 0],
        [0, 0, 0, 0, 0, 0, 0, -1, -math.cos(math.pi / 4), 0, math.cos(math.pi / 6)],
        [0, 0, 0, 0, 0, 0, 0, 0, -math.sin(math.pi / 4), 0, -math.sin(math.pi / 6)],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -math.cos(math.pi / 6)]
    ]

    b = [0, 0, 0, 10000, 0, 0, 0, 20000, 0, 0, 0]

    b = solveLU(A, b)




if __name__ == "__main__":
    main()
