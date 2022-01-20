
def myhorner(dd, xi, x):
    res = 0

    for val in dd:
        calcul = val
        for i in range(dd.index(val)):
            calcul *= x-xi[i]

        res += calcul

    return res



# xi et yi doivent avoir le même nombre d'éléments
# à l'appel de la fonction result doit être None
def getInterpollationPoint(xi, yi, result,numberOfResult):
    if len(result) == 0:
        result.append(yi[0])

    if(len(result) != numberOfResult):
        tempYi = []

        for i in range(len(yi)-1):
            tempYi.append((yi[i]-yi[i+1])/(xi[i]-xi[i+1]))

        xi.pop(1)

        result.append(tempYi[0])
        getInterpollationPoint(xi, tempYi, result,numberOfResult)
        return result

def diffdiv(xi,yi):
    return getInterpollationPoint(xi, yi, [],len(xi))



def main():
    xi = [1, 3, 4, 7]
    yi = [-2, 6, 13, 46]
    interpollation = diffdiv(xi, yi)
    xi = [1, 3, 4, 7]
    print(interpollation)
    print(myhorner(interpollation, xi, 7))

if __name__ == '__main__':
    main()
