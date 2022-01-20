
def myhorner(dd, xi, x):
    n = len(dd)
    valeur = dd[n - 1]
    for i in range(n - 2, -1, -1):
        valeur = valeur * x + dd[i]
    return valeur


def prog():
    print(myhorner([-2, 4, 2, 1/18], [], 4))


if __name__=="__main__":
    prog()