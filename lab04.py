#lab04.py

from Stack import Stack

def solveMaze(maze, startX, startY):
    s = Stack()
    counter = 1

    s.push([startX,startY])
    currentX = s.peek()[0]
    currentY = s.peek()[1]
    maze[currentX][currentY] = counter

    while s.isEmpty != False:
        currentX = s.peek()[0]
        currentY = s.peek()[1]

        if maze[currentX][currentY] == 'G':
            return True

        #North
        elif maze[currentX - 1][currentY] == ' ' or maze[currentX - 1][currentY] == 'G':
            if maze[currentX - 1][currentY] == 'G':
                return True
            counter += 1
            maze[currentX - 1][currentY] = counter
            s.push([currentX - 1,currentY])

        #West
        elif maze[currentX][currentY - 1] == ' ' or maze[currentX][currentY - 1] == 'G':
            if maze[currentX][currentY - 1] == 'G':
                return True
            counter += 1
            maze[currentX][currentY - 1] = counter
            s.push([currentX,currentY - 1])

        #South
        elif maze[currentX + 1][currentY] == ' ' or maze[currentX + 1][currentY] == 'G':
            if maze[currentX + 1][currentY] == 'G':
                return True
            counter += 1
            maze[currentX + 1][currentY] = counter
            s.push([currentX + 1,currentY])

        #East
        elif maze[currentX][currentY + 1] == ' ' or maze[currentX][currentY + 1] == 'G':
            if maze[currentX][currentY + 1] == 'G':
                return True
            counter += 1
            maze[currentX][currentY + 1] = counter
            s.push([currentX,currentY + 1])

        else:
            if s.size() > 1:
                s.pop()
            else:
                return False
