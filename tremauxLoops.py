#Algoritmo de Tremaux
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
        
        

        x = currentPos[0]
        y = currentPos[1]

        #If finish point is reached, return path
        if currentPos[0] == finish[0] and currentPos[1] == finish[1]:
            return path
        

        #Cheks if on a wall or been here before
        posMaze = maze[y][x]
        posVisited = visited[y][x]
        print("MazePos: " + str(posMaze))
        print("VisitedPos: " + str(posVisited))
       
        if posMaze == 1 or posVisited ==2:
            #return to prev position
            currentPos = prevPos.pop()
            path.pop()
            dir = spinDir(currentPos,dir)
            
            continue


        elif posVisited==1:
            print("mark again")
            visited[y][x]==2
        else:
            #Agregar en la posicion que ya pasee aqui
            print("mark")
            visited[y][x]=1
        
        

        if x != 0 and dir==3:
            prevPos.append(currentPos)
            currentPos = [x-1,y]
            path.append(["L"])
            continue

        if x != len(maze) - 1 and dir==1:
            prevPos.append(currentPos)
            currentPos = [x+1,y]
            path.append(["R"])
            continue

        if y != len(maze[0])-1 and dir==2:
            prevPos.append(currentPos)
            currentPos = [x,y+1]
           
            path.append(["D"])
            continue

        if y != 0 and dir==0:
            prevPos.append(currentPos)
            currentPos = [x,y-1]

            path.append(["U"])
            continue


        
        dir = reverseDir(currentPos,dir)

            
        
        
        
        

def spinDir(currentPos,dir):
        temp = dir
        cond=2
        while cond==2:
            dir =  switch(dir)
            cond = checkVisited(currentPos,dir)
            
        print(dir)
        return dir

def reverseDir(currentPos,dir):
        temp = dir
        cond=2
        while cond==2:
            
            dir =  reverse(dir)
            cond = checkVisited(currentPos,dir)
            
        print(dir)
        return dir


def checkMaze(currentPos,dir):
    x = currentPos[0]
    y = currentPos[1]

    print((x,y))
    
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
    return 1
    
    
    

def checkVisited(currentPos,dir):
    x = currentPos[0]
    y = currentPos[1]

   
    
    if dir==0 and y<size[1]-1:
        y += 1 
        return visited[y][x]
    if dir == 1 and x<size[0]-1:
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
    return 1

#funcion que invierte la direccion
def switch(x):
    return {
        0 : 1,
        1: 2,
        2: 3,
        3: 0
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

import sys
sys.setrecursionlimit(99000)

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
for y in range(int(size[0])):
    visited.append([])
    for x in range(int(size[1])):
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

#print(path[::-1])


