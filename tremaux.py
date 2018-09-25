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
        maze.append(list(map(int, line.replace("\n",''))))
    cont += 1

#Voltear laberinto sobre el eje x
maze.reverse()
print(maze)

#Create a marker and the right path matrix
pathTracer = [[0]*len(maze[0]) for _ in range(len(maze))]
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

#Just to give some space
print()
print()

#Convert begin and finish to list of integers
begin = getNumbers(begin)
finish = getNumbers(finish)

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