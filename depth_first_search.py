from maze_plot import *
import matplotlib.pyplot as plt
from get_neighbors import *


def depth_first_search(dfs_maze, display=True):
    dfs_maze=dfs_maze.copy()
    source = (0,0)
    goal = (len(dfs_maze)-1, len(dfs_maze)-1)
    dfs_maze[source] = -1
    dfs_stack = [source]
    dfs_path = []
    flag = 0

    while len(dfs_stack) != 0 and flag == 0:
        cur_node = dfs_stack.pop()
        dfs_path.append(cur_node)
        dfs_maze[cur_node] = -2
        neighbors = traversable_neighbors(dfs_maze, cur_node)
        if len(neighbors) == 0:
            dfs_path.pop()
        else:
            for node in neighbors:
                if node == goal:
                    
                    dfs_maze[goal] = -2
                    if display:
                        print("Path found!!!")
                        maze_plot_final(dfs_maze)
                    flag = 1
                    return 1
                dfs_stack.append(node)
        dfs_maze[cur_node] = -1
    if flag == 0:
        
        if display:
            print("No path found :(")
            maze_plot_final(dfs_maze)
        return 0
