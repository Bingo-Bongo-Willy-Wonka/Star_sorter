import numpy as np
#дано T(t) - изменение температуры по времени
T = [279, 280, 288, 289, 290, 293, 296]
t = [2006, 2008, 2010, 2012, 2014, 2016, 2018]

def inter(year):

    for i in range(0, len(t)):
        if t[i]-year > 0:
            coor_1 = i-1
            coor_2 = i
            print(i-1, i)
            break
    value = T[coor_1] + (year-t[coor_1])*((T[coor_2] - T[coor_1])/(t[coor_2] - t[coor_1]))
    return value
print(inter(2015))


