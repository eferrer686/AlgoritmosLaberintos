import time
start_time = time.time()

class Graph(object):
    
    #Funcion constructora
    def __init__(self,begin,finish):
        self.begin = begin
        self.finish = finish
        
    #Funcion que regresa un String al ser impresa la clase
    #print(Graph)
    def __repr__(self):
        return "Begin: " + str(self.begin) + "Finish: " + str(self.finish)

    #Funcion que resuelve los nodos
    def algorithm(self):
        return "Aqui va el algoritmo"

    #If only one is true
    def onlyOne(self,*args):
        return sum(args) == 1

    #Funcion que crea los nodos a partir de un arreglo de 0s y 1s
    def createNodes(self, maze):
        nodes = []
        #Iterar sobre renglones
        for y in range(len(maze)):
            #iterar sobre columnas
            for x in range(len(maze[y])):
                
                #Banderas de bloques
                up = False
                down = False
                right = False
                left = False

                #Ver si es camino o pared (0|1)
                
                if maze[y][x] == 0:
                   
                    #Cuadro de la derecha - x menor a size
                    if (x+1)<len(maze[y]) and maze[y][x+1]==0 :
                        right =True
                        
                    #Cuadro de la izquierda
                    if (x-1)>=0 and maze[y][x-1]==0 :
                        left = True
                       
                    #Cuadro de arriba
                    if (y+1)<len(maze) and maze[y+1][x]==0:
                        up = True
                        
                    #Cuadro de abajo
                    if (y-1)>=0 and maze[y-1][x]==0:
                        down = True
                        

                    #Busqueda de areas de interes
                    #----Basicamente que se encuentre un angulo recto
                    if (right and down) or (down and left) or (left and up) or (up and right):
                        nodes.append(Node(x,y,None,None,None,None))
                       
                    elif self.onlyOne(up,right,left,down):
                        nodes.append(Node(x,y,None,None,None,None))
        self.mapNodes(nodes,maze)

    def mapNodes(self,nodes,maze):
        for n in nodes:
            if n == self.begin:
                self.begin.closestRight(nodes)
                self.begin.closestLeft(nodes)
                self.begin.closestUp(nodes)
                self.begin.closestDown(nodes,maze)
            elif n == self.finish:
                self.finish.closestRight(nodes)
                self.finish.closestLeft(nodes)
                self.finish.closestUp(nodes)
                self.finish.closestDown(nodes,maze)
            else:
                n.closestRight(nodes)
                n.closestLeft(nodes)
                n.closestUp(nodes)
                n.closestDown(nodes,maze)
    def tremaux():
        return None



class Node(object):
    #Funcion constructora
    def __init__(self,x,y,up,down,left,right):
        self.x = int(x)
        self.y = int(y)
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        
    #Funcion que regresa un String al ser impresa la clase
    #print(Node)
    def __repr__(self):
        return str([self.x,self.y])

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
      
    #Distancia a nodos
    def distUp(self):
        return int(self.up.y - self.y)
    def distDown(self):
        return int(self.down.y - self.y)
    def distRight(self):
        return int(self.right.x - self.x)
    def distLeft(self):
        return int(self.left.x - self.x)
    
    #Busca el nodo mas cercano, si es que hay uno, en una direccion
    def closestUp(self,nodes):
        dist=float('Inf')
        for n in nodes:
            temp = n.y-self.y
            #Checar si hay paredes
            wall = True
            for y in range(n.y,self.y):
                if maze[y][n.x]==1:
                    wall=False

            if  n.x == self.x and temp < dist and temp > 0:
                self.up = n
                dist = temp
        return True
    def closestDown(self,nodes,maze):
        dist=float('Inf')
        for n in nodes:
            temp = n.y-self.y
            #Checar si hay paredes
            wall = True
            for y in range(self.y,n.y):
                if maze[y][n.x]==1:
                    wall=False
            #Ver si es el nodo mas cercano
            if  wall and n.x == self.x and temp < dist and temp < 0:
                self.down = n
                dist = temp
        return True
    def closestLeft(self,nodes):
        dist=float('Inf')
        for n in nodes:
            temp = n.x-self.x
            #Checar si hay paredes
            wall = True
            for x in range(n.x,self.x):
                
                if maze[n.y][x]==1:
                    wall=False
            if  wall and n.y == self.y and temp < dist and temp < 0:
                self.left = n
                dist = temp
        return True
    def closestRight(self,nodes):
        dist=float('Inf')
        for n in nodes:
            temp = n.x-self.x
            #Checar si hay paredes
            wall = True
            for x in range(self.x,n.x):
                if maze[n.y][x]==1:
                    wall=False
            if  n.y == self.y and temp < dist and temp > 0:
                self.right = n
                dist = temp
        return True
    
        
                

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

#Crear Grafo
begin = Node(begin[0],begin[1],None,None,None,None)
finish = Node(finish[0],finish[1],None,None,None,None)
g = Graph(begin,finish)
#Convertir maze a nodos e imprimirlos
g.createNodes(maze)
#imprimir info de grafo
maze = maze[::-1]

for m in maze:
    print(m)
print(begin)
print("Begin nodes:")
print(g.begin.right)
print(g.begin.left)
print(g.begin.up)
print(g.begin.down)

#Imprime el tiempo que tomo todo el proceso
elapsed_time = time.time() - start_time
print("Time:")
print(elapsed_time)