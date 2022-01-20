

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


if __name__ == '__main__':

    xi = [1,3,4,7]
    yi = [-2,6,13,46]
    interpollation = diffdiv(xi,yi)
    print(interpollation)