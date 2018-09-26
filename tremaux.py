import sys
sys.setrecursionlimit(99000)

import fileinput
size = ''
begin = []
finish = []
maze = []
solutionPath = ''  

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
        maze.append(list(map(int, line.replace("\n",''))))
    cont += 1

#Voltear laberinto sobre el eje x
maze.reverse()


#Crear marcador de camino recorrido
pathTracer = [[0]*len(maze[0]) for _ in range(len(maze))]
#Crear marcador de camino correcto
rightPath = [[0]*len(maze[0]) for _ in range(len(maze))]

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



#Transformar begin y finish
begin = getNumbers(begin)
finish = getNumbers(finish)

#Ajustar la matriz a la orientación del sistema en la web
maze = maze[::-1]

#Ajusta coordenadas de los puntos a la orientación de la matriz en el sistema de prueba
def adjustCoordinates(coordinates):
    aux = coordinates[1]
    coordinates[1] = coordinates[0]
    coordinates[0] = (len(maze)-1) - aux
    return coordinates

#Ajustar begin y finish
begin = adjustCoordinates(begin)
finish = adjustCoordinates(finish)

#Algoritmo de Tremaux
def tremaux(x, y):
    path = ""
    #If finish point is reached, return true
    if x == finish[0] and y == finish[1]:
        return path
    #Cheks if on a wall or been here before
    if maze[x][y] == 1 or pathTracer[x][y] == 1:
        return None
    pathTracer[x][y] = 1
    #If not on left edge
    if x != 0:
        path = tremaux(x-1, y)
        if path !=None:
            rightPath[x][y] = 1
            return path + "U"
    #If not on right edge
    if x != len(maze) - 1:
        path = tremaux(x + 1, y)
        if path!=None:
            rightPath[x][y] = 1
            return path + "D"
    #If not on top edge
    if y != 0:
        path = tremaux(x, y - 1)
        if path!=None:
            rightPath[x][y] = 1
            return path + "L"
    #If not in bottom edge
    if y != len(maze[0]) - 1:
        path = tremaux(x, y + 1)
        if  path != None:
            rightPath[x][y] = 1
            return path + "R"
    return path

#SOLO PARA VISUALIZARLO, BORRAR DESPUÉS
#Imprimir solución

path = tremaux(begin[0], begin[1])

print(path[::-1])

