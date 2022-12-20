import astropy.io.fits as pf
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import math as m

##################################################### Графики
def plot_verticles(vertices, isosurf = False, filename = None, colour = None, cmap_ = None):
    # Create a new plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]
    z = [v[2] for v in vertices]
    if isosurf:
        ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True, color=colour, cmap = cmap_)
    else:
        ax.scatter(x, y, z, c='r', marker='o')
    # ax.set_xlabel('X')
    # ax.set_ylabel('Y')
    # ax.set_zlabel('Z')
    # Show or save the plot
    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)

def profile(xp, yp, type):
    global data, R
    srez = []
    data_vrem = []
    if type == "horisontal":
        plt.plot(data[yp][(xp-R):(xp+R)])
        plt.title("Горизонтальный профиль")
        plt.show()
    if type == "vertical":
        data_vrem = np.transpose(data)
        plt.plot(data_vrem[xp][(yp-R):(yp+R)])
        plt.title("Вертикальный профиль")
        plt.show()

    #
    # for i in range(-R, R):
    #     srez.append(0)
    #     srez[i+R] = data_vrem[yp][xp+i]
    # abciss = []
    # for i in range(xp - R, xp + R):
    #     abciss.append(i)

def profile_x():
    horisont = []
    for i in range(0, R):
        horisont.append(0)
        horisont[i] = data[y][x - (R-i)]
    for i in range(0, R):
        horisont.append(0)
        horisont[R + i] = data[y][x + i]
    abciss = []
    for i in range(y-R, y+R):
        abciss.append(i)

    plt.plot(abciss, horisont)
    plt.title("Горизонтальный профиль")
    plt.show()

def profile_y():
    vertikal = []
    for i in range(0, R):
        vertikal.append(0)
        vertikal[i] = data[y - (R-i)][x]
    for i in range(0, R):
        vertikal.append(0)
        vertikal[R + i] = data[y + i][x]
    ordinan = []
    for i in range(x-R, x+R):
        ordinan.append(i)

    plt.plot(ordinan, vertikal)
    plt.title("Вертикальный профиль")
    plt.show()

""" жалко удалять
def graph_3D_tochecny():
    ax = plt.axes(projection='3d')
    for j in range(0, R):

        coord_sreza = []
        srez = []
        for i in range(0, R + 1):
            coord_sreza.append(1)
            coord_sreza[i] = y - (R - i)
        for i in range(1, R + 1):
            coord_sreza.append(1)
            coord_sreza[R + i] = y + i
        print(coord_sreza)

        for i in range(0, R + 1):
            srez.append(1)
            srez[i] = data[y - (R - i)][x - (R - j)]
        for i in range(1, R + 1):
            srez.append(1)

        ax.scatter3D(x - (R - j), coord_sreza, srez, color="red")

    for j in range(0, R):

        coord_sreza = []
        srez = []
        for i in range(0, R + 1):
            coord_sreza.append(1)
            coord_sreza[i] = y - (R - i)
        for i in range(1, R + 1):
            coord_sreza.append(1)
            coord_sreza[R + i] = y + i
        print(coord_sreza)

        for i in range(0, R + 1):
            srez.append(1)
            srez[i] = data[y - (R - i)][x + j]
        for i in range(1, R + 1):
            srez.append(1)
            srez[R + i] = data[y + i][x + j]
        print("srez:", srez)

        ax.scatter3D(x + j, coord_sreza, srez, color="red")
"""
def graph_3D():
    gr = []
    for i in range(-R, R):
        for j in range(-R, R):
            gr.append([x + i, y + j, data[y + j][x + i]])
    plot_verticles(vertices=gr, isosurf=True, cmap_="BuPu_r")
    # #Reds Blues_r BrBG_r BuPu_r
####################################################### Сумма отсчетов
"""
def summing_staroe():
    global sum_otchetov
    ############# Вычисление среднего потока фона
    sum_fona = 0
    n_fona = 0
    sum_zvezda_istinnoe = 0

    for j in range(0, R_vnesh):
        for i in range (0, R_vnesh):
            if m.sqrt(i**2+j**2)<=R_vnesh and m.sqrt(i**2+j**2)>= R: #расстояние пикселя от центра звезды меньше R fona и больше R:
                n_fona += 1
                sum_fona += data[y-(R_vnesh-j)][x-(R-j)]
        for i in range (1, R_vnesh):
            if m.sqrt(i**2+j**2)<=R_vnesh and m.sqrt(i**2+j**2)>= R:
                n_fona += 1
                sum_fona += data[y + j][x-(R-j)]


    for j in range(1, R_vnesh+1):
        for i in range (0, R_vnesh):
            if m.sqrt(i**2+j**2)<=R_vnesh and m.sqrt(i**2+j**2)>= R:
                n_fona += 1
                sum_fona += data[y-(R_vnesh-j)][x+j]
        for i in range (1, R_vnesh):
            if m.sqrt(i**2+j**2)<=R_vnesh and m.sqrt(i**2+j**2)>= R:
                n_fona += 1
                sum_fona += data[y + j][x+j]


    srednee_fona = sum_fona/n_fona

    ############## Вычисление суммарного потока звезды
    n_zvezda = 0
    sum_zvezda = 0
    for j in range(0, r):
        for i in range(0, r):
            if  m.sqrt(i**2+j**2)<=r: # расстояние пикселя от центра звезды меньше r:
                n_zvezda += 1
                sum_zvezda += data[y - (r - j)][x - (r - j)]
        for i in range(1, r):
            if  m.sqrt(i**2+j**2)<=r:
                n_zvezda += 1
                sum_zvezda += data[y + j][x - (r - j)]

    for j in range(1, r + 1):
        for i in range(0, r):
            if  m.sqrt(i**2+j**2)<=r:
                n_zvezda += 1
                sum_zvezda += data[y - (r - j)][x + j]
        for i in range(1, r):
            if  m.sqrt(i**2+j**2)<=r:
                n_zvezda += 1
                sum_zvezda += data[y + j][x + j]
    sum_zvezda_istinnoe = sum_zvezda - n_zvezda*srednee_fona
    sum_otchetov = sum_zvezda_istinnoe
    #print("Истинная сумма отсчетов звезды=", int(sum_zvezda_istinnoe))
"""

def summing():
    global sum_otchetov
    ############# Вычисление среднего потока фона
    sum_fona = 0
    n_fona = 0

    for j in range(-R_vnesh, R_vnesh):
        for i in range(-R_vnesh, R_vnesh):
            if m.sqrt(i**2+j**2)<=R_vnesh and m.sqrt(i**2+j**2)>R:  # расстояние пикселя от центра звезды меньше R fona и больше R:
                n_fona += 1
                sum_fona += data[y + j][x + j]

    srednee_fona = sum_fona / n_fona

    ############## Вычисление суммарного потока звезды
    n_zvezda = 0
    sum_zvezda = 0
    for j in range(-r, r):
        for i in range(-r, r):
            if m.sqrt(i ** 2 + j ** 2) <= r:  # расстояние пикселя от центра звезды меньше r:
                n_zvezda += 1
                sum_zvezda += data[y + j][x + j]

    sum_zvezda_istinnoe = 0
    sum_zvezda_istinnoe = sum_zvezda - n_zvezda * srednee_fona
    sum_otchetov = sum_zvezda_istinnoe

#################################################################################   Command OK

def ok():
    global x, y, r, R, R_vnesh, file, data

    snimok = pf.open(txt.get(1.0, END).replace("\n", ""))
    data = snimok[0].data
    snimok.close()

    x = int(x_coord.get(1.0, END))
    y = int(y_coord.get(1.0, END))
    r = int(mesto_vvoda_r.get(1.0, END))
    R = int(mesto_vvoda_R.get(1.0, END))
    R_vnesh = int(mesto_vvoda_R_vnesh.get(1.0, END))
    global sum_otchetov
    if chk_X_state.get():
        profile(x, y, "horisontal")
    if chk_Y_state.get():
        profile(x, y, "vertical")
    if chk_3D_state.get():
        graph_3D()
    if chk_otchet_state.get():
        summing()
        messagebox.showinfo('Cумма отсчетов', int(sum_otchetov)) # как задать размеры вспл окна?
########################################## Открываем окно

window = Tk()
window.title("THE STAR")
window.geometry('600x300')



#############################################################################     Вводные данные

lbl_file = Label(window, text="Путь к файлу:", font=("Arial Bold", 10))
lbl_file.grid(column=0, row=0)

txt = Text(window,width=40,height=1)
txt.insert(INSERT, r'C:\Users\Aydar\Desktop\ИНФА 3 семестр\v523cas60s-001.fit')
txt.grid(column=1, row=0)

lbl_X = Label(window, text="Координата X:", font=("Arial Bold", 10))
lbl_X.grid(column = 0, row=1)

x_coord = Text(window, width=40, height=1)
x_coord.insert(INSERT, "671")
x_coord.grid(column=1, row=1)


lbl_Y = Label(window, text="Координата Y:", font=("Arial Bold", 10))
lbl_Y.grid(column = 0, row=2)

y_coord = Text(window, width=40, height=1)
y_coord.insert(INSERT, "1656")
y_coord.grid(column=1, row=2)


lbl_r = Label(window, text="Радиус звезды(r):", font=("Arial Bold", 10))
lbl_r.grid(column = 0, row=3)

mesto_vvoda_r = Text(window, width=40, height=1)
mesto_vvoda_r.insert(INSERT, "4")
mesto_vvoda_r.grid(column=1, row=3)


lbl_R = Label(window, text="Внутренний радиус кольца:", font=("Arial Bold", 10))
lbl_R.grid(column = 0, row=4)

mesto_vvoda_R = Text(window, width=40, height=1)
mesto_vvoda_R.insert(INSERT, "7")
mesto_vvoda_R.grid(column=1, row=4)


lbl_R_vnesh = Label(window, text="Внешний радиус кольца:", font=("Arial Bold", 10))
lbl_R_vnesh.grid(column = 0, row=5)

mesto_vvoda_R_vnesh = Text(window, width=40, height=1)
mesto_vvoda_R_vnesh.insert(INSERT, "20")

mesto_vvoda_R_vnesh.grid(column=1, row=5)

########################################################################      Checkbuttons
chk_X_state = IntVar()
chk_X_state.set(1)
chk_X = Checkbutton(window, text='Профиль по X', var=chk_X_state)
chk_X.grid(column=1, row=6)

chk_Y_state = IntVar()
chk_Y_state.set(1)
chk_Y = Checkbutton(window, text='Профиль по Y', var=chk_Y_state)
chk_Y.grid(column=1, row=7)

chk_3D_state = IntVar()
chk_3D_state.set(1)
chk_3D = Checkbutton(window, text='3D график      ', var=chk_3D_state)
chk_3D.grid(column=1, row=8)

chk_otchet_state = IntVar()
chk_otchet_state.set(1)
chk_otchet = Checkbutton(window, text='Сумма отсчетов', var=chk_otchet_state)
chk_otchet.grid(column=1, row=9)

btn_ok = Button(window, text="OK", command=ok)
btn_ok.grid(column=2, row=7)

################################################################# конец
window.mainloop()