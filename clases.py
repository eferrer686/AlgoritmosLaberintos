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
        nodos = []
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
                        nodos.append(Node(x,y,None,None,None,None))
                       
                    elif self.onlyOne(up,right,left,down):
                        nodos.append(Node(x,y,None,None,None,None))
                        
        return nodos



class Node(object):
    #Funcion constructora
    def __init__(self,x,y,up,down,left,right):
        self.x = x
        self.y = y
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        
    #Funcion que regresa un String al ser impresa la clase
    #print(Node)
    def __repr__(self):
        return str([self.x,self.y])
                

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

#Crear Grafo
g = Graph(begin,finish)
#Convertir maze a nodos e imprimirlos
print(g.createNodes(maze))
#imprimir info de grafo
print(g)