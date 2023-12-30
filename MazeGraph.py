import numpy as np
import matplotlib.pyplot as plt

class UndirectedGraph():
    def __init__(self):
        self.graph = {}
        
    def add_node(self, node):
        self.node = node

        if self.node in self.graph:
            return "Node already in graph"
        self.graph[self.node] = []


    def add_edge(self, edge):
        n1 = edge.get_n1()
        n2 = edge.get_n2()

        if not(n1 in self.graph):
            raise ValueError(f"node {n1.get_name()} not added")
        if not(n2 in self.graph):
            raise ValueError(f"node {n2.get_name()} not added")
        self.graph[n1].append(n2) 
        self.graph[n2].append(n1)

    def get_node(self, node_name):
        for n in self.graph:
            if node_name == n.get_name():
                return n

    def node_in_graph(self, node):
        return node in self.graph
    
    
    def get_neighbours(self, node):
        return [n.get_name() for n in self.graph[node]]
    

    def __str__(self):
        edges = ''
        for n1 in self.graph:
            for n2 in self.graph[n1]:
                edges += f"{n1.get_name()} ---> {n2.get_name()} \n"

        return edges 
    

    
class Node():
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.name
    
class Edge():
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def get_n1(self):
        return self.n1
    
    def get_n2(self):
        return self.n2
    
    def __str__(self):
        return f"{self.n1.get_name()} ----> {self.n2.get_name()}"

class Maze(UndirectedGraph):

    def __init__(self, maze_str, starting_point_name, end_point_name):
        super().__init__()

        self.wall = 255
        self.color_start_point = 200
        self.color_goal_point = 100
        self.maze = maze_str
        self.starting_point_name = starting_point_name
        self.end_point_name = end_point_name

    def __generating_array(self, maze_str):

        row = []
        col = []
    
        for i in maze_str:

        
            if i == '#':
                row.append(self.wall)
            elif i == ' ':
                row.append(0)
            elif i == 'A':
                row.append(self.color_start_point)
            elif i == 'B':
                row.append(self.color_goal_point)
            else:
                if row == []:
                    continue
                else:
                    col.append(row)
                    row = []

        maze_array = np.array(col)

        
        return maze_array
    
    def __generating_dict(self, maze_array):

        coor_row = np.where(maze_array == 0)[0]
        coor_col = np.where(maze_array == 0)[1]
        coor_tuple = tuple(zip(coor_row,coor_col))

        coor_row_goalstate = np.where(maze_array == 100)[0][0]
        coor_col_goalstate = np.where(maze_array == 100)[1][0]
        coor_tuple_goalstate = (coor_row_goalstate,coor_col_goalstate)
       
        coor_row_instate = np.where(maze_array == 200)[0][0]
        coor_col_instate = np.where(maze_array == 200)[1][0]
        coor_tuple_instate = (coor_row_instate,coor_col_instate)
       

        node_coor = {self.starting_point_name: coor_tuple_instate, self.end_point_name: coor_tuple_goalstate}

        for n, i in enumerate(coor_tuple):
                node_coor['n' + str(n)] = i
        
        return node_coor
    
    def maze_to_graph(self):

        maze_array = self.__generating_array(self.maze)
        dict_coor = self.__generating_dict(maze_array)

        graph = UndirectedGraph()

        for n in dict_coor: 
            graph.add_node(Node(n))

        for from_n in dict_coor:
            for to_n in dict_coor:
                row_from_n = dict_coor[from_n][0]
                col_from_n = dict_coor[from_n][1]

                row_to_n = dict_coor[to_n][0]
                col_to_n = dict_coor[to_n][1]

                if row_from_n + 1 == row_to_n and col_from_n == col_to_n:
                    graph.add_edge(Edge(graph.get_node(from_n),graph.get_node(to_n)))
            
                if col_from_n + 1 == col_to_n and row_from_n == row_to_n:
                    graph.add_edge(Edge(graph.get_node(from_n), graph.get_node(to_n)))

        return graph
    
    def solution_search_image(self, path_solution):

        maze_array = self.__generating_array(self.maze)
        dict_coor = self.__generating_dict(maze_array)

        _, axis = plt.subplots(1,2)

        axis[0].imshow(maze_array, cmap = 'pink', extent=[0, maze_array.shape[1], 0, maze_array.shape[0]])
        axis[0].set_xticks(range(0, maze_array.shape[1]))
        axis[0].set_yticks(range(0, maze_array.shape[0]))
        axis[0].tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False, right=False, left=False, labelleft=False)
        axis[0].grid(True)

        

        for j in path_solution:
            
            if self.starting_point_name == j or self.end_point_name == j:
                continue
            y, x = dict_coor[j]
            maze_array[y,x] = 150

        axis[1].imshow(maze_array, cmap = 'pink', extent=[0, maze_array.shape[1], 0, maze_array.shape[0]])
        axis[1].set_xticks(range(0, maze_array.shape[1]))
        axis[1].set_yticks(range(0, maze_array.shape[0]))
        axis[1].tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False, right=False, left=False, labelleft=False)
        axis[1].grid(True)
        plt.show()

        
    def image_maze(self):   

        image_array = self.__generating_array(self.maze)

        _, ax = plt.subplots(1,1)

        ax.imshow(image_array, cmap = 'pink', extent=[0, image_array.shape[1], 0, image_array.shape[0]]) 
        ax.set_xticks(range(0, image_array.shape[1]))
        ax.set_yticks(range(0, image_array.shape[0]))

        plt.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False, right=False, left=False, labelleft=False)
        plt.grid(True)
        plt.show()