import numpy as np
class labyrinth:
    def __init__ (self,matrix,start,exit):
        self.matrix=np.array(matrix)
        self.start=start
        self.exit=exit
        self.height=len(self.matrix)
        self.width=len(self.matrix[0])
    
    def initial_percents(self):
        return {'start':self.start,
                'exit':self.exit}
    
    def get_initial_state(self):
        return self.start

    def get_neighbors(self,state):

        (row,col)=state
        neighbors=[]

        possible_moves=np.array([
            (-1, 0),#subir
            (1, 0),#descer
            (0, 1),#direita
            (0, -1),#esquerda
        ])

        for cd, de in possible_moves:
            new_row,new_col= row+cd, col+de

            if (0 <= new_row < self.height and 0 <= new_col < self.width):
                if(self.matrix[new_row][new_col]==0 ):
                    new_state=np.array([new_row,new_col])
                    neighbors.append(new_state)
        
        return neighbors



if __name__=='__main__':
    m = [
        [0, 0, 0, 0, 0, 0, 0, 0],  
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 'g', 0, 0, 0, 0, 0], 
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 's', 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    env=labyrinth(m, [5,3],[2,2])

    print(f"Estado Inicial: {env.get_initial_state()}")
    print(f"É objetivo? {env.is_goal((2, 2))}")
    print(f"Vizinhos de (0,0): {env.get_neighbors((0,0))}")
    print(f"Vizinhos de (3,0): {env.get_neighbors((3,0))}")
    
