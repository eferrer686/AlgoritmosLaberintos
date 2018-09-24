import time
start_time = time.time()

import fileinput
size = ''
begin = []
finish = []
maze = []

cont = 0


#Leer archivo
for line in fileinput.input():
    if cont==0:
        #Leer Tamaño de laberinto
        size = line
    elif cont==1:
        #Leer coordenada de inicio
        begin = line
    elif cont==2:
        #Leer coordenada de final
        finish = line
    if cont>2:
        #Leer laberinto quitando el caracter "Enter"
        maze.append(line.replace("\n",''))
    cont += 1

#Voltear laberinto sobre el eje x
maze.reverse()
print(maze)


#Funcion que encuentra 2 numeros separados por uno o varios espacios
def getNumbers(text):
    s=[]
    s.append([])
    s.append([])
    flag = True
    for c in text:
        if c != ' ' and flag:
            s[0] += c
        elif c != ' ' and c != '\n':
            s[1].append(c)
        else:
            flag = False

    r = []
    r.append(int(''.join(s[0])))
    r.append(int(''.join(s[1])))
    return r


size = getNumbers(size)
begin = getNumbers(begin)
finish = getNumbers(finish)

#Imprime los valores ya en Int
print(size)
print(begin)
print(finish)



#Imprime el tiempo que tomo todo el proceso
elapsed_time = time.time() - start_time
print("Time:")
print(elapsed_time)
