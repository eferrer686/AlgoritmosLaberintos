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
print(maze)

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

#Un poco de espacio
print()
print()

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

#SOLO PARA VISUALIZARLO, BORRAR DESPUÉS
#Imprime matrix
def printMaze(maze, begin, finish, pathTracer):
    print("Starting point: (" + str(begin[0]) + ", " + str(begin[1]) + ")")
    print("Finish point:   (" + str(finish[0]) + ", " + str(finish[1]) + ")")
    #Starting point displayed on maze
    maze[begin[0]][begin[1]] = 2
    #Finish point displayed on maze
    maze[finish[0]][finish[1]] = 3
    print("Maze:")
    print("Start = 2")
    print("Finish: 3")
    for row in maze:
        print(row)

#Algoritmo de Tremaux
def tremaux(x, y):
    #If finish point is reached, return true
    if x == finish[0] and y == finish[1]:
        return True
    #Cheks if on a wall or been here before
    if maze[x][y] == 1 or pathTracer[x][y] == 1:
        return False
    pathTracer[x][y] = 1
    #If not on left edge
    if x != 0:
        if tremaux(x-1, y):
            rightPath[x][y] = 1
            return True
    #If not on right edge
    if x != len(maze) - 1:
        if tremaux(x + 1, y):
            rightPath[x][y] = 1
            return True
    #If not on top edge
    if y != 0:
        if tremaux(x, y - 1):
            rightPath[x][y] = 1
            return True
    #If not in bottom edge
    if y != len(maze[0]) - 1:
        if tremaux(x, y + 1):
            rightPath[x][y] = 1
            return True
    return False

#SOLO PARA VISUALIZARLO, BORRAR DESPUÉS
#Imprimir solución
def showSolution(begin):
    if tremaux(begin[0], begin[1]):
        #Convert finish point to 1
        rightPath[finish[0]][finish[1]] = 1
        print("Solution:")
        for row in rightPath:
            print(row)
    else:
        print("No solution")

printMaze(maze, begin, finish, pathTracer)
showSolution(begin)

print(begin[0])
print(begin[1])
print(begin[0])
print(begin[1]+1)
print(rightPath[begin[0]][begin[1]+1]+rightPath[begin[0]][begin[1]])

def printSolution(begin, rightpath, solutionPath): 
    while begin != finish:
        if rightpath[begin[0]][begin[1]+1] + rightpath[begin[0]][begin[1]] == 2:
            solutionPath = solutionPath + "R"
            rightpath[begin[0]][begin[1]] = 0
            begin[0] = begin[0]
            begin[1] = begin[1]+1
        else:
            if rightpath[begin[0]+1][begin[1]] + rightpath[begin[0]][begin[1]] == 2:
                solutionPath = solutionPath + "D"
                rightpath[begin[0]][begin[1]] = 0
                begin[0] = begin[0]+1
                begin[1] = begin[1]
            else:
                if rightpath[begin[0]][begin[1]-1] + rightpath[begin[0]][begin[1]] == 2:
                    solutionPath = solutionPath + "L"
                    rightpath[begin[0]][begin[1]] = 0                    
                    begin[0] = begin[0]
                    begin[1] = begin[1]-1
                else:
                    if rightpath[begin[0]-1][begin[1]] + rightpath[begin[0]][begin[1]] == 2:
                        solutionPath = solutionPath + "U"
                        rightpath[begin[0]][begin[1]] = 0                        
                        begin[0] = begin[0]-1
                        begin[1] = begin[1]
    print(solutionPath)
printSolution(begin, rightPath, solutionPath)



