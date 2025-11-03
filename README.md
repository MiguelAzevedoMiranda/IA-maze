# 🤖 Agente de Busca em Labirinto

Este projeto implementa um agente de busca genérico para encontrar caminhos em labirintos 2D. A arquitetura separa o **ambiente** (o labirinto), a **estrutura de dados** (o nó) e o **agente** (o algoritmo de busca), permitindo configurar e executar facilmente diferentes estratégias de busca, como Busca em Largura (BFS) e Busca em Profundidade (DFS).

## 🎯 Sobre o Projeto

O objetivo é encontrar um caminho da posição inicial (`s`) até a posição final (`g`) dentro de uma matriz que representa um labirinto.

* **`0`**: Caminho livre
* **`1`**: Parede (obstáculo)

O agente utiliza uma "fronteira" (lista de nós a explorar) e um conjunto de "visitados" para navegar pelo labirinto de forma eficiente.

## 🛠️ Componentes Principais

O código é dividido em três classes principais, que idealmente ficariam em arquivos separados (ex: `agent.py` e `ambient.py`).

### 1. Classe `Node` (em `agent.py`)

Esta classe representa um ponto (estado) na busca. Ela armazena toda a informação necessária para o algoritmo e para reconstruir o caminho.

* `state`: A coordenada (linha, coluna) atual no labirinto.
* `parent`: O nó `Node` do qual este nó se originou (essencial para reconstruir o caminho).
* `g`: O custo acumulado para chegar até este nó a partir do início.
* `h`: O custo heurístico estimado deste nó até o objetivo (usado em algoritmos como A*).
* `depth`: A profundidade do nó na árvore de busca (quantos passos desde o início).
* `get_solution(node)`: Uma função estática crucial que, ao receber o nó final (objetivo), percorre a cadeia de `parent` de volta ao início para montar a lista de coordenadas do caminho encontrado.

### 2. Classe `labyrinth` (em `ambient.py`)

Esta classe define o ambiente (o labirinto) onde o agente irá operar.

* `matrix`: A matriz (labirinto) em si.
* `start`: Coordenada inicial.
* `exit`: Coordenada do objetivo.
* `get_neighbors(state)`: O método mais importante. Dado um estado (coordenada), ele retorna uma lista de todos os vizinhos válidos (para cima, baixo, esquerda, direita) que estão dentro dos limites da matriz e **não são paredes** (valor `1`).

### 3. Classe `AgentMaze` (em `agent.py`)

Este é o cérebro do projeto. É um agente de busca **genérico** que implementa a lógica central de exploração.

Sua flexibilidade vem do fato de que as funções de controle da fronteira são passadas como parâmetros no construtor:

* `env`: A instância do ambiente `labyrinth`.
* `add_fcn`: A **função** que define *como* adicionar um nó à fronteira.
* `get_fcn`: A **função** que define *como* remover um nó da fronteira.
* `cost_fcn`: A função que calcula o custo `g` (ex: 1.0 para custo uniforme).
* `h_fcn`: A função de heurística `h` (ex: 0.0 para BFS/DFS, ou Distância de Manhattan para A*).

O método `search()` implementa o algoritmo de busca:
1.  Inicia a fronteira `F` com o nó inicial.
2.  Inicia um conjunto `visited` para evitar ciclos e trabalho repetido.
3.  Entra em loop:
    * Remove um nó `s` da fronteira (usando `get_fcn`).
    * Verifica se `s` é o objetivo. Se sim, retorna `s`.
    * Adiciona `s` aos `visited`.
    * Para cada vizinho de `s` (usando `env.get_neighbors`):
        * Cria um novo `Node` para o vizinho.
        * Se o vizinho **não** estiver em `visited`, adiciona-o à fronteira (usando `add_fcn`).

---

## ⚙️ Como Funciona: BFS vs. DFS

A genialidade do `AgentMaze` está em como ele pode ser configurado para ser diferentes algoritmos de busca, simplesmente mudando as funções `add_fcn` e `get_fcn`.

### 1. Busca em Largura (BFS)

O BFS explora o labirinto "camada por camada", garantindo encontrar o caminho mais curto (em número de passos).

* **Como?** Usando uma **Fila (FIFO - First-In, First-Out)**.
* **Implementação no código:**
    * `add_fcn`: `Node.add_last` (adiciona no final da lista)
    * `get_fcn`: `Node.get_first` (remove do início da lista `F.pop(0)`)

```python
# O agente 'bfs' usa a fronteira como uma Fila
bfs = AgentMaze(env, 
                Node.add_last,      # Adiciona no fim
                Node.get_first,     # Remove do início
                lambda s,s_neighbors: 0.0, 
                lambda s,G: 0.0)

### 2. Busca em profundidade (DFS)

O DFS explora um caminho o mais fundo possível antes de fazer "backtrack" e tentar outro. Ele encontra um caminho, mas não necessariamente o mais curto.

* **Como?** Usando uma **Pilha (LIFO - Last-In, First-Out)**.
* **Implementação no código:**
    * `add_fcn`: `Node.add_last` (adiciona no final da lista)
    * `get_fcn`: `Node.get_last` (remove do final da lista `F.pop(-1)`)

```python
# O agente 'dfs' usa a fronteira como uma Pilha
dfs = AgentMaze(env, 
                Node.add_last,      # Adiciona no fim
                Node.get_last,      # Remove do fim
                lambda s,s_neighbors: 1.0, 
                lambda s,G: 0.0)

