import random
import tkinter


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tkinter.Tk()
root.wm_title("Embedding in Tk")
root.geometry("1000x500")
current_list = ['Polynome P(x)']


fig = Figure(figsize=(2, 3), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)



def getResult():

    result = []
    for i in range(100):
        result.append(i)

    return result

def main():
    xs = []
    for i in range(100):
        xs.append(i)

    ys = getResult()

    ax.plot(xs, ys, label='polynome')

    fig.legend()

    canvas.draw()
    canvas.flush_events()


    root.mainloop()


if __name__ == "__main__":
    main()
