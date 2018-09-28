"""
Eduardo Ferrer Mac Gregor Ruiz	A01651867
Jorge Akio Olvera Arao 		    A01651395
Jesús Iván Tapia Romero		    A01338275
"""
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

#Solo para verlo Borrar despues
def printMaze(maze, begin, finish, pathTracer):
    print("Starting point: (" + str(begin[0]) + ", " + str(begin[1]) + ")")
    print("Finish point:   (" + str(finish[0]) + ", " + str(finish[1]) + ")")
    #Starting point displayed on maze
    maze[begin[0]][begin[1]] = 2
    print("Maze:")
    print("Start = 2")
    print("Finish: 3")
    for row in maze:
        print(row)
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

#Pinta la linea recta hacia el final que va a dividir el laberinto
def LineaChain(begin,finish):
    path=[]
    x1=begin[0]
    y1=begin[1]
    x2=finish[0]
    y2=finish[1]
    while x1!=x2 or y1!=y2:
        xdiff=ydiff=0
        if x1<x2:
            xdiff=1
        elif x1>x2:
            xdiff=-1
        else:
            ydiff=0
        if y1<y2:
            ydiff=1
        elif y1>y2:
            ydiff=-1
        else:
            ydiff=0
        x1=x1+xdiff
        y1=y1+ydiff
        current=(y1,x1)
        if maze[x1][y1]==0:
            maze[x1][y1]=4
            path.append(current)
    return path

linea=LineaChain(begin,finish)
print (linea)
printMaze(maze, begin, finish, pathTracer)
#SOLO PARA VISUALIZARLO, BORRAR DESPUÉS
#Imprimir solución

