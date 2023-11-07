import numpy as np
import matplotlib.pyplot as plt
import random
from collections import deque

def generateMaze(m, n):
    # Create an empty maze with walls
    maze = np.ones((m, n), dtype=int)

    # Set the start and end points
    start = (random.randrange(m), random.randrange(n))
    end = (random.randrange(m), random.randrange(n))
    maze[start] = 0  # Start point
    maze[end] = 2  # End point

    return maze

def drawMaze(maze, m, n, algo):
    for i in range(m):
        for j in range(n):
            if maze[i, j] == 0:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, color='green'))
            if maze[i, j] == 2:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, color='red'))
            if maze[i, j] == 1:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, color='black'))
                # ax.add_patch(plt.Rectangle((j, i), m, n, fill=False, edgecolor='blue'))

    ax.set_xlim(0, n)
    ax.set_ylim(0, m)
    graph = Graph()
    graph.traverse(m, n, algo)

def drawLine(direction, i, j):
    if direction == 1:
        ax.add_patch(plt.Rectangle((j + 0.5, i), 0.1, 1, color='white'))
    elif direction == 0:
        ax.add_patch(plt.Rectangle((j, i + 0.5), 1, 0.1, color='white'))

class Graph:
    def traverse(self, m, n, algo):
        seen = set()
        path = []
        
        def getNeighbors(r, c):
            return [
                (r-1, c),
                (r, c+1),
                (r+1, c),
                (r, c-1)
            ]
        
        def isValid(r, c):
            return r > -1 and c > -1 and r < m and c < n

        def dijkstra(r, c):
            ""

        def bfs(r, c):
            unvisited_nodes = deque()
            unvisited_nodes.append((r, c))
            start = (r, c)
            # Key: Neighbor Node, Value: Source Node
            # Dictionary to traverse nodes, by storing the neighbor and source node
            parent = {}

            while unvisited_nodes:
                temp_node = unvisited_nodes.popleft()
                r, c = temp_node[0], temp_node[1]

                if maze[r][c] == 2:
                    # End found, construct path
                    # Iterate backwards from the end to the start
                    while (r, c) != (start[0], start[1]):
                        path.append((r, c))
                        # Traverse through the nodes
                        r, c = parent[(r, c)][0], parent[(r, c)][1]
                    path.append((start[0], start[1]))  # Add the start point
                    # Start from the start, not end node
                    path.reverse
                    return

                seen.add(temp_node)
                for neighbor in getNeighbors(r, c):
                    if isValid(neighbor[0], neighbor[1]) and neighbor not in seen:
                        seen.add(neighbor)
                        # Store the source node of the neighbor
                        parent[neighbor] = (r, c)
                        unvisited_nodes.append(neighbor)

        def dfs(r, c):
            path.append((r, c))  # Add the current cell to the path
            if maze[r][c] == 2:
                return True  # Found the end point
            for neighbor in getNeighbors(r, c):
                if isValid(neighbor[0], neighbor[1]) and neighbor not in seen:
                    seen.add(neighbor)
                    if dfs(neighbor[0], neighbor[1]):
                        return True  # Return True if the end point is found in this branch
            path.pop()  # Remove the current cell from the path when backtracking
            return False

        # DFS
        if algo == 1: 
            for r in range(m):
                for c in range(n):
                    if (r, c) not in seen and maze[r][c] == 0:
                        seen.add((r, c))
                        path = []
                        if not dfs(r, c):
                            path = []  # Clear the path if it's not valid
        
        # BFS
        if algo == 2:
            for r in range(m):
                for c in range(n):
                    if (r, c) not in seen and maze[r][c] == 0:
                        path.append((r, c))
                        bfs(r, c)

        # Dijkstra
        if algo == 3:
            ""

        def drawCorner(i, j, r1, c1, r3, c3):
            if (i == r1 and j == c3 and r3 < r1 and c3 < c1) or (i == r3 and j == c1 and r1 < r3 and c1 < c3):
                # Top left corner
                ax.add_patch(plt.Rectangle((j + 0.5, i), 0.1, 0.6, color='white'))
                ax.add_patch(plt.Rectangle((j + 0.5, i + 0.5), 0.6, 0.1, color='white'))               
            elif (i == r3 and j == c1 and r3 < r1 and c1 < c3) or (i == r1 and j == c3 and r1 < r3 and c3 < c1):
                # Bottom left corner
                ax.add_patch(plt.Rectangle((j + 0.5, i + 0.5), 0.1, 0.5, color='white'))
                ax.add_patch(plt.Rectangle((j + 0.5, i + 0.5), 0.5 , 0.1, color='white'))
            elif (i == r1 and j == c3 and r3 < r1 and c1 < c3) or (i == r3 and j == c1 and r1 < r3 and c3 < c1):
                # Top right corner
                ax.add_patch(plt.Rectangle((j + 0.5, i), 0.1, 0.6, color='white'))
                ax.add_patch(plt.Rectangle((j, i + 0.5), 0.6 , 0.1, color='white'))
            elif (i == r1 and j == c3 and r1 < r3 and c1 < c3) or (i == r3 and j == c1 and r3 < r1 and c3 < c1):
                # Bottom right corner
                ax.add_patch(plt.Rectangle((j + 0.5, i + 0.5), 0.1, 0.5, color='white'))
                ax.add_patch(plt.Rectangle((j, i + 0.5), 0.6 , 0.1, color='white'))          

        def draw():
            for i in range(1, len(path) - 1):
                r1, c1 = path[i - 1]
                r2, c2 = path[i]    
                r3, c3 = path[i + 1]
                # Check horizontal straight lines
                if r1 == r2 == r3:
                    drawLine(0, r2, c2)
                # Check vertical straight lines
                elif c1 == c2 == c3:
                    drawLine(1, r2, c2)
                else:
                    drawCorner(r2, c2, r1, c1, r3, c3)
                
            #     plt.draw()  # Redraw the figure
            #     plt.pause(0.01)  # Add a short delay to see the updates
            # plt.show()
        draw()
        plt.show()

# Example: Create and display a 20x20 maze
maze_size = (20, 20)
maze = generateMaze(*maze_size)
fig, ax = plt.subplots(figsize=(8, 8))
drawMaze(maze, 20, 20, 3)
