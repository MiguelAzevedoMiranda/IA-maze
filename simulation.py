from ambient import labyrinth
from agent import *
import numpy as np





matrix = [[0,1,1,1,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [1,0,0,0,0,1,0,1,0,0],
          [1,1,0,0,0,1,0,1,0,0],
          [0,0,0,0,0,0,0,1,0,0],
          [0,0,0,1,0,0,0,1,1,0],
          [0,0,0,1,0,0,0,0,1,1],
          [0,0,0,1,0,0,0,0,0,0]]

env=labyrinth(matrix,np.array([0,0]),np.array([len(matrix)-1,len(matrix[0])-1]))

bfs=AgentMaze(env, Node.add_last,Node.get_first,lambda s,s_neighbors:0.0, lambda s,G:0.0)
dfs=AgentMaze(env,Node.add_last, Node.get_last, lambda s,s_neighbors:1.0,lambda s,G:0.0)

res=bfs.search()
res2=dfs.search()
print(res)
print(res.depth)
print(Node.get_solution(res))
print(res2)
print(res2.depth)
print(Node.get_solution(res2))