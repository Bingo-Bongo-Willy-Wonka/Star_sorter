def timeformule(hjd):
    a = int(hjd) + 32044
    b = (4*a+3)//146097
    c = a - (146097*b)//4
    d = (4*c + 3)//1461
    e = c - (1461*d)//4
    m = (5*e+2)//153
    day = e - (153*m + 2)//5 + 1
    month = m + 3 - 12*(m//10)
    year = 100*b + d - 4800 + m//10
    dola = hjd - int(hjd) + 0.5
    if dola >= 1:
        day += 1
        dola -= 1
    dola_hours = 24*dola
    hours = int(dola_hours)
    dola_minutes = (dola_hours % 1)*60
    minutes = int(dola_minutes)
    dola_seconds = (dola_minutes % 1)*60
    seconds = int(dola_seconds)
    day = str(day)
    month = str(month)
    hours = str(hours)
    minutes = str(minutes)
    seconds = str(seconds)
    if len(day) == 1: day = "0" + day
    if len(month) == 1: month = "0" + month
    if len(hours) == 1: hours = "0" + hours
    if len(minutes) == 1: minutes = "0" + minutes
    if len(seconds) == 1: seconds = "0" + seconds
    return f'{day}.{month}.{year} {hours}:{minutes}:{seconds}'

txt = open(r'C:\Users\Aydar\Desktop\STARS\task2_data.dat', 'r')
Spisok_strok = txt.readlines()
txt.close()

Names = []
HJDs = []
Filters = []
Magns = []

for i in range (1, len(Spisok_strok) - 1):
    a = Spisok_strok[i].split("    ")
    Names.append(a[0])
    HJDs.append(a[1])
    Filters.append(a[2])
    Magns.append(a[3])

print("\nЗвезды: ", set(Names))

for i in range(0, len(Filters)):              #чистилка от \n и пробелов
    Filters[i] = Filters[i].replace(" ", "")
    Filters[i] = Filters[i].replace("\n", "")

for i in range(0, len(Magns)):              #чистилка от \n и пробелов
    Magns[i] = Magns[i].replace(" ", "")
    Magns[i] = Magns[i].replace("\n", "")


print("Фильтры:", set(Filters))

Needed_stars = input("\nВведите имя звезды:")

Needed_filters = []
One_of_filters = 0
while One_of_filters != "":
    One_of_filters = input("Введите фильтр:")
    if One_of_filters != "":
        Needed_filters.append(One_of_filters)

Data_of_HJD = []
Data_of_magn = [] #[[0,0]]
for i in range(0, len(Names)):
    if Needed_stars == Names[i]:
        for k in range(0, len(Needed_filters)):
            if Needed_filters[k] == Filters[i]:
                Data_of_HJD.append(HJDs[i])
                Data_of_magn.append([])
                for t in range(0, len(Needed_filters)):
                    Data_of_magn[-1].append("none")
                    if t == k:
                        Data_of_magn[-1][t] = Magns[i]
                    else:
                        Data_of_magn[-1][t] = "-"

Dict = []
for i in range(len(Data_of_HJD)):
    Dict.append([0, 0])
    Dict[i][0] = Data_of_HJD[i]
    Dict[i][1] = Data_of_magn[i]
Dict = dict(Dict)

Dict = sorted(Dict.items(), key=lambda x: x[0])
Dict = dict(Dict)

done = open(r'C:\Users\Aydar\Desktop\STARS\DONE.dat', 'w')
done.write("The gregorian date:    ")
done.write("HJDs 24")

for i in range(0, len(Needed_filters)):
    done.write("        ")
    done.write(Needed_filters[i])

for key in Dict:
    done.write("\n")
    key_float = float("24" + str(key))
    done.write(timeformule(key_float))
    done.write("    ")
    key_str = str(key)
    done.write(key_str)
    done.write("    ")
    for i in range(0, len(Needed_filters)):
        done.write(Dict[key][i])
        done.write("        ")

done.close()
print("\nСохранено в файл Done.dat")