import random
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math

root = tkinter.Tk()
root.wm_title("Embedding in Tk")
root.geometry("1000x500")
current_list = ['Polynome P(x)']


fig = Figure(figsize=(2, 3), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def calculPolynome(x):
    firstCalcul = (2* pow(x, 2))-(3*x)+1
    secondCalcul = (math.sqrt(6)/2)*((-4*pow(x, 2))+4*x)
    thirdCalcul = (math.sqrt(2)*((2*pow(x, 2))-x))
    result = firstCalcul + secondCalcul + thirdCalcul
    return result

def polynomeResult(iteration):

    result = []
    for i in range(iteration):
        result.append(calculPolynome(i/iteration))

    return result

def fonctionResult(iteration):
    result = []
    for i in range(iteration):
        result.append(math.sqrt(1+i/iteration))

    return result

def errorResult(fonction,polynome):
    result = []
    for i in range(len(fonction)):
        result.append(fonction[i]-polynome[i])

    return result


def main():
    iteration = 100
    abscisse = []

    for i in range(iteration):
        abscisse.append(i)

    courbePolynome = polynomeResult(iteration)
    courbeFonction = fonctionResult(iteration)
    courbeErreur = errorResult(courbePolynome,courbeFonction)

    ax.plot(abscisse, courbePolynome, label='polynome')
    ax.plot(abscisse, courbeFonction, label='fonction', color='red')
    ax.plot(abscisse, courbeErreur, label='f(x) - p(x)', color='black')

    fig.legend()

    canvas.draw()
    canvas.flush_events()


    root.mainloop()


if __name__ == "__main__":
    main()
