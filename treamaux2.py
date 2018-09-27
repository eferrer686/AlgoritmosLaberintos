def tremaux():
    path = list()
    currentPos = begin
    prevPos = list([begin])

    #0 - U, 1 - R, 2 - D, 3 -L
    dir = 0 

    while True:


        print("path: " + str(path))
        print("----------------------------------")
        print("Current: " + str(currentPos))
        print("Prev: " + str(prevPos))
        print("Dir: " + str(dir))
        
        dir = spinDir(currentPos)
        x = currentPos[0]
        y = currentPos[1]

        print("Maze: " + str(maze[y][x]))
        print("Visited: " + str(visited[y][x]))
        

        #If finish point is reached, return path
        if currentPos[0] == finish[0] and currentPos[1] == finish[1]:
            return path

        #Cheks if on a wall or been here before
        posMaze = maze[y][x]
        posVisited = visited[y][x]

        if posMaze == 1:
            #return to prev position
            currentPos = prevPos.pop()
            path.pop()
            dir = spinDir(currentPos)
            continue
        elif posVisited ==2:
            dir = spinDir(currentPos)
        elif posVisited==1:
            visited[y][x]=2
            
        else:
            visited[y][x]=1

        setDeadEnd(currentPos)

        if x != 0 and dir==3:
            prevPos.append(currentPos)
            currentPos = [x-1,y]
            path+="L"
            continue

        if x != len(maze) - 1 and dir==1:
            prevPos.append(currentPos)
            currentPos = [x+1,y]
            path+="R"
            continue

        if y != 0 and dir==2:
            prevPos.append(currentPos)
            currentPos = [x,y-1]
           
            path+="D"
            continue

        if y != len(maze[0])-1 and dir==0:
            prevPos.append(currentPos)
            currentPos = [x,y+1]

            path+="U"
            continue

        
        dir = spinDir(currentPos)



#Manejo de direcciones
def turnRigh(x):
    return {
        0 : 1,
        1: 2,
        2: 3,
        3: 0
    }[x]
def turnLeft(x):
    return {
        0 : 3,
        1: 0,
        2: 1,
        3: 2
    }[x]
def reverse(x):
    return {
        0 : 2,
        1: 3,
        2: 0,
        3: 1
    }[x]
def getDir(x):
    return {
        0: "Derecha",
        1: "Arriba",
        2: "Izquierda",
        3: "Abajo"
    }[x]



#Ver mapa del Laberinto
def checkMaze(currentPos,dir):
    x = currentPos[0]
    y = currentPos[1]

    print((x,y))
    
    if dir==0 and y<size[0]-1:
        y += 1 
        return maze[y][x]
    if dir == 1 and x<size[1]-1:
        x+=1
        return maze[y][x]
    if dir == 2 and y>0:
        y-=1
        return maze[y][x]
    if dir == 3 and x>0:
        x-=1
        return maze[y][x]
    if dir==4:
        return maze[y][x]
    return 2
    

#Ver mapa de lo visitado
def checkVisited(currentPos,dir):
    x = currentPos[0]
    y = currentPos[1]
    
    print("Size"+str(size))
    print(x)

    if dir==0 and y<(size[0]-1):
        y += 1 
        return visited[y][x]
    if dir == 1 and x<(size[1]-1):
        x+=1
        return visited[y][x]
    if dir == 2 and y>0:
        y-=1
        return visited[y][x]
    if dir == 3 and x>0:
        x-=1
        return visited[y][x]
    if dir == 4:
        return visited[y][x]
        print("local")
    return 2


#dar una vuelta y regresar caminos disponibles
def spinDir(currentPos):
        pas=[]

        for dir in range(4):
            v = checkVisited(currentPos,dir)
            m = checkMaze(currentPos,dir)
            print("Dir: " + str(dir))
            print("V: " + str(v))

            if v!=2 and m != 1:
                pas.append(dir)
        print("Passages: " + str(pas))
        return selectBestDir(currentPos,pas)
        
def selectBestDir(currentPos,pas):
    temp=2
    dir=4
    for p in pas:
        print(str(p)+"-"+str(checkVisited(currentPos,p)))
        if temp>checkVisited(currentPos,p):
            temp=checkVisited(currentPos,p)
            dir = p
    return dir

def setDeadEnd(currentPos):
    x = currentPos[0]
    y = currentPos[1]

    cont = 0

    l = maze[y][x-1]
    r = maze[y][x+1]
    u = maze[y+1][x]
    d = maze[y-1][x]

    if l == 1 or x==0:
        cont+=1
    if r == 1 or x==(size[1]-1):
        cont+=1
    if u == 1 or y==0:
        cont+=1
    if d == 1 or y==(size[0]-1):
        cont+=1

    
    print("#Walls: " + str(cont))

    if cont>2:
        visited[y][x] = 2


#Logica para correr el algoritmo


import fileinput
size = []
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




#Crear marcador de camino recorrido
pathTracer = [[0]*len(maze[0]) for _ in range(len(maze))]
#Crear marcador de camino correcto
rightPath = [[0]*len(maze[0]) for _ in range(len(maze))]

#Funcion que encuentra 2 numeros separados por uno o varios espacios
def getNumbers(text):
    s1=""
    s2=""
    flag = True
    text = str(text)
    for c in text:
        
        if c != ' ' and flag:
            
            s1 = str(s1) + str(c)
            
        elif c != ' ' and c != '\n':
            s2 = s2 + (c)
        else:
            flag = False
    
    
    r = [int(s1),int(s2)]
    
    return r





#Ajustar la matriz a la orientación del sistema en la web
maze = maze[::-1]


#Ajustar begin y finish
size = getNumbers(size)
begin = getNumbers(begin)
finish = getNumbers(finish)


visited = []



#Create visited
for y in range(int(size[1])):
    visited.append([])
    for x in range(int(size[0])):
        visited[y].append(0)


print("size: " + str(size))
print("Begin: " + str(begin))
print("Finish: " + str(finish))

cx=0
cy=0
for y in maze:
    cx=0

    for x in y:
        print(str((cx,cy))+"-"+str(x))
        cx+=1

    cy+=1

#print maze

for m in maze:
    print(m)


path = tremaux()
final = ""
for p in path:
    final+=p

print(final)