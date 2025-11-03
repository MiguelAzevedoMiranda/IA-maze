import numpy as np

class Node:
    #paramentros state,parent(a casa anterior), g(custo), h(heuristica que é quanto falta para o exit)
    def __init__(self, state, parent=None, g=0.0,h=0.0):
        self.state=state
        self.parent=parent
        self.g=g #custo
        self.h=h #heuristica
        self.depth=0 if parent is None else parent.depth+1 #profundidade, quantidade de nós
    
    #_eq_ quando eu comparar dois nós ele vai comparar se os seus states são iguais 
    def __eq__(self,other):
        return np.array_equal(self.state,other.state)
    
    #transformar meu state em bytes(.tobytes() que é imutavel) e depois passar para hash que e como o .set lê
    def __hash__(self):
        return hash(self.state.tobytes())

    #para transformar o meu print do nó em state 
    def __str__(self):
        return f'{self.state[0]},{self.state[1]}'

    #funcao para mostrar o caminho feito pelo meu agente(essa funcao roda depois da funcao search)
    def get_solution(node):
        solution=[]
        solution.append(node.state.tolist())#adiciona o ultimo no(g) na minha lista solution

        while node.parent: #toda vez que o meu no(g) tiver um .parent ele entra no while
            node=node.parent #agora meu nó passa a ser o parente de g
            solution.append(node.state.tolist()) #adiciona o parente de g no solution
        solution.reverse() #inverte a lista pois ela pega o caminho de trás pra frente
        return solution
    #f= Fronteira (linha que divide quem eu vistei de quem eu ainda nao visitei)
    def add_last(F,s):
        F.append(s)
    
    #Pega o ultimo adicionado na lista fronteira BFS
    def get_first(F):
        return F.pop(0)
    
    #Pega o primeiro adicionado na lista fronteira DFS
    def get_last(F):
        return F.pop(-1)
        



class AgentMaze:
    def __init__(self,env,add_fcn,get_fcn,cost_fcn, h_fcn):
        self.env=env
        self.add_fcn=add_fcn
        self.get_fcn=get_fcn
        self.cost_fcn=cost_fcn
        self.h_fcn=h_fcn

        self.G=self.env.initial_percents()['exit']
        self.visited=set()

    def search(self):
        s0=Node(self.env.initial_percents()['start'],
                None, 
                g=0.0, 
                h=self.h_fcn(self.env.initial_percents()['start'],self.G)
               )
        F=[]
        self.add_fcn(F,s0)

        while F:
            s=self.get_fcn(F)

            if (s.state==self.G).all(): #.all porque estou compoarando um arrayNp ([2,2]==[2,2] isso retorna [True, True] so que eu quero so [True])
                return s

            self.visited.add(s)#ja foi visitado entao adiciono ele no visited

            for s_neighbors in self.env.get_neighbors(s.state):
                s_node=Node(s_neighbors,s, self.cost_fcn(s_neighbors,s), self.h_fcn(s_neighbors,self.G))
                if s_node not in self.visited:
                    self.add_fcn(F,s_node)
        return None

       




        
    


