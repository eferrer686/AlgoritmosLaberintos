import fileinput
size = []
begin = []
finish = []
maze = []

cont = 0

for line in fileinput.input():
    if cont==0:
        size = line
    elif cont==1:
        begin = line
    elif cont==2:
        finish = line
    if cont>2:
        maze.append(line.replace("\n",''))
    cont += 1

print(size)
print(begin)
print(finish)
print(maze)

