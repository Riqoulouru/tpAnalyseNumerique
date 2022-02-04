import math
import tkinter
import numpy
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

X = numpy.poly1d([1, 0])
def concat(i, xi, x=X):
    concat_mult = 1
    for j in range(0, i):
        concat_mult = concat_mult * (x - xi[j])
    return concat_mult

def myHorner(dd, xi):
    polynomial = dd[0]

    for i in range(1, len(dd)):
        polynomial = polynomial + dd[i] * concat(i, xi)
    return polynomial


def diffdiv(xi, yi):
    a_result = []
    dd = [yi[0]]
    result = []
    for i in range(0, len(yi) - 1):
        for j in range(0, len(yi) - 1):
            a_result.append((yi[j] - yi[j + 1]) / (xi[j] - xi[j + (i + 1)]))
        yi = a_result.copy()
        result.append(a_result[0])
        a_result.clear()
    dd.extend(result)
    return dd

def getFunctionResult(function,xi):
    res = []
    for i in xi:
        res.append(function(i))
    return res

def comparaison(f, a, b, n):
    xi = []
    for i in range(1, n + 1):
        xi.append(f(a, b, i, n))
    return xi

def equirepartis(a, b, i, n):
    return a+((i-1)*((b-a)/(n-1)))


def tchbychev(a, b, i, n):
    return ((a + b) / 2) * a + ((b - a) / 2) * math.cos((2 * i - 1) * (math.pi / (2 * n)))

def calcul_yi(xi, f):
    yi = []
    for i in range(0, len(xi)):
        yi.append(f(xi[i]))
    return yi




def function1Tchebychev(n):
    comparaisonTchbychev = comparaison(tchbychev, -2, 2, n)
    diffDivTchebychev = diffdiv(comparaisonTchbychev, calcul_yi(comparaisonTchbychev, function1))
    polynomeTchebychev = myHorner(diffDivTchebychev, comparaisonTchbychev)

    return polynomeTchebychev

def function1(x):
    if x == 0:
        return 1
    return math.sin(2 * math.pi * x) / (2 * math.pi * x)


def function2(x):
    return 1 / (1 + pow(x, 2))

def function1Equi(n):
    comparaisonEquiReparti = comparaison(equirepartis, -2, 2, n)
    diffDivEquiReparti = diffdiv(comparaisonEquiReparti, calcul_yi(comparaisonEquiReparti, function1))
    polynomeEquireparti = myHorner(diffDivEquiReparti, comparaisonEquiReparti)
    return polynomeEquireparti

def function1Tchbychev(n):
    comparaisonTchbychev = comparaison(tchbychev, -2, 2, n)
    diffDivTchbychev = diffdiv(comparaisonTchbychev, calcul_yi(comparaisonTchbychev, function1))
    polynomeEquireparti = myHorner(diffDivTchbychev, comparaisonTchbychev)
    return polynomeEquireparti


def function2Equireparti(n):
    comparaisonEquiReparti = comparaison(equirepartis, -5, 5, n)
    diffDivEquiReparti = diffdiv(comparaisonEquiReparti, calcul_yi(comparaisonEquiReparti, function1))
    polynomeEquireparti = myHorner(diffDivEquiReparti, comparaisonEquiReparti)
    return polynomeEquireparti



def function2Tchbychev(n):
    comparaisonTchbychev = comparaison(tchbychev, -5, 5, n)
    diffDivTchbychev = diffdiv(comparaisonTchbychev, calcul_yi(comparaisonTchbychev, function1))
    polynomeEquireparti = myHorner(diffDivTchbychev, comparaisonTchbychev)
    return polynomeEquireparti

def main():
    f1 = numpy.vectorize(function1)
    f2 = numpy.vectorize(function2)
    xp1 = numpy.linspace(-2, 2)
    xp2 = numpy.linspace(-5, 5)

    plt.figure(1)
    plt.legend("P1 equirépartis et fonction 1")
    plt.plot(xp1, f1(xp1))
    for i in range(5, 12):
        plt.plot(xp1, function1Equi(i)(xp1))

    plt.figure(2)
    plt.legend("Tchebychev et fonction 1")
    plt.plot(xp1, f1(xp1))
    for i in range(5, 12):
        plt.plot(xp1, function1Tchbychev(i)(xp1))

    plt.figure(3)
    plt.legend("P1 equirépartis et fonction 2")
    plt.plot(xp1, f2(xp2))
    for i in range(5, 12):
        plt.plot(xp2, function2Equireparti(i)(xp1))

    plt.figure(4)
    plt.legend("Tchebychev et fonction 2")
    plt.plot(xp1, f2(xp2))
    for i in range(5, 12):
        plt.plot(xp2, function2Tchbychev(i)(xp1))

    plt.show()

if __name__ == '__main__':
    main()
