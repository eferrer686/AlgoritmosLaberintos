import random
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

#dar una vuelta y regresar el mejor camino
def spinDir(currentPos,walls,lastDec):
        visits = visitAround(currentPos)
        pas=[]
        
        #Left
        if walls[0]==0 and visits[0]!=2:
            pas.append(3)
        #right
        if walls[1]==0 and visits[1]!=2:
            pas.append(1)
        #up
        if walls[2]==0 and visits[2]!=2:
            pas.append(0)
        #down
        if walls[3]==0 and visits[3]!=2:
            pas.append(2)
        print("Pas :" + str(pas))
        return selectBestDir(currentPos,pas,lastDec)
def selectBestDir(currentPos,pas,lastDec):
    temp=2
    dir=4
    for p in pas:
        if temp>checkVisited(currentPos,p):
            temp=checkVisited(currentPos,p)
            dir = p
        elif temp==checkVisited(currentPos,p)and dir!=lastDec and bool(random.getrandbits(1)):
            temp=checkVisited(currentPos,p)
            dir = p
    return dir

#Encontrar paredes
def wallsAround(currentPos):
    x = currentPos[0]
    y = currentPos[1]
    l=0
    r=0
    u=0
    d=0

    cont = 0
    

    if x==0 or maze[y][x-1]==1:
        l=1
        cont+=1        

    if x==(size[0]-1) or maze[y][x+1]==1:
        r=1
        cont+=1

    if y==(size[1]-1) or maze[y+1][x]==1:
        u=1
        cont+=1

    if y==0 or maze[y-1][x]==1:
        d=1
        cont+=1


    return [l,r,u,d,cont]

def visitAround(currentPos):
    x = currentPos[0]
    y = currentPos[1]

    

    cont = 0

    if x==0:
        l=2
    else:
        l = visited[y][x-1]

    if x==(size[0]-1):
        r=2
    else:
        r = visited[y][x+1]

    if y==(size[1]-1):
        u=2  
    else:
        u = visited[y+1][x]
        
    if y==0:
        d=2
    else:
        d = visited[y-1][x]

    return [l,r,u,d]

def caminosDisponibles(visits,walls):
    cont=0
    for c in range(4):
        if visits[c]!=2 and walls[c]==0:
            cont+=1
    return cont
#Ver mapa del Laberinto
def checkMaze(currentPos,dir):
    x = currentPos[0]
    y = currentPos[1]
    
    if dir==0 and y<size[1]-1:
        y += 1 
        return maze[y][x]
    if dir == 1 and x<size[0]-1:
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
    
   

    if dir==0 and y<(size[1]-1):
        y += 1 
        return visited[y][x]
    if dir == 1 and x<(size[0]-1):
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
        
    return 2


def tremaux():
    path = list()
    currentPos = begin
    prevPos = list([begin])
    

    #0 - U, 1 - R, 2 - D, 3 -L
    dir = 0 
    lastDec=0
    
    while True:
        
        x = currentPos[0]
        y = currentPos[1]

        print((x,y))
        for v in visited:
            print(v)

        


        #Ver si ya acabe
        if x==finish[0] and y==finish[1]:
            return path

        #Estoy en pared? En teoria nunca pasaria
        if maze[y][x]==1:
            path.pop()
            currentPos = prevPos.pop()



        #Ver posibles camninos
        walls = wallsAround(currentPos)
        visits = visitAround(currentPos)
        cam = caminosDisponibles(visits,walls)
        
        #Ver si hay dead end
        
        if walls[4]>2:
            
            visited[y][x]=2

        elif visited[y][x]==1  and cam < 2:
            
            visited[y][x]=2
        #Marcar en donde paso
        elif visited[y][x]==0:
            
            visited[y][x]=1
        
        dir = spinDir(currentPos,walls,lastDec)


        #Tomar el camino
        if x != 0 and dir==3:
            prevPos.append(currentPos)
            currentPos = [x-1,y]
            lastDec=3
            path+="L"
            continue

        if x != len(maze[0]) - 1 and dir==1:
            prevPos.append(currentPos)
            currentPos = [x+1,y]
            lastDec=1
            path+="R"
            continue

        if y != 0 and dir==2:
            prevPos.append(currentPos)
            currentPos = [x,y-1]
            lastDec=2
            path+="D"
            continue

        if y != len(maze)-1 and dir==0:
            prevPos.append(currentPos)
            currentPos = [x,y+1]
            lastDec=0
            path+="U"
            continue



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



path = tremaux()
final = ""
for p in path:
    final+=p

print(final)