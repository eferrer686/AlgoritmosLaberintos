import time
start_time = time.time()

import fileinput
size = []
begin = []
finish = []
maze = []

cont = 0

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
        maze.append(line.replace("\n",''))
    cont += 1

print(size)
print(begin)
print(finish)
print(maze)

#Voltear laberinto sobre el eje x
maze.reverse()
print(maze)


elapsed_time = time.time() - start_time
print("Time:")
print(elapsed_time)
