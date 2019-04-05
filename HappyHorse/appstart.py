from GA import GA

ga = GA(100)
l = ga.resolver()

tabla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
         24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

for i in range(0, 36):
    tabla[l.genes[i]] = i

str = "\n"
k = 0
for i in range(0, 36):
    k += 1
    if tabla[i] > 9:
        str += tabla[i].__str__() + ' '
    else:
        str += tabla[i].__str__() + ' ' + ' '
    if k == 6:
        str += '\n'
        k = 0

print(str)
