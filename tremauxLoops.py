#Algoritmo de Tremaux
def tremaux():
    path = ""
    currentPos = begin
    prevPos = list([begin])
    print(prevPos.pop())
    print(prevPos)

    while True:
        
        #Acabo
        if currentPos == finish:
            return path

        return True

            

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
    
    
    r = (int(s1),int(s2))
    
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

#print maze

for m in maze:
    print(m)


path = tremaux()

#print(path[::-1])


