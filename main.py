from MazeGraph import *

maze_str1 = """
#####B#
##### #
####  #
#### ##
     ##
A######
"""


maze_str2 = """
###                 #########
#   ###################   # #
# ####                # # # #
# ################### # # # #
#                     # # # #
##################### # # # #
#   ##                # # # #
# # ## ### ## ######### # # #
# #    #   ##B#         # # #
# # ## ################ # # #
### ##             #### # # #
### ############## ## # # # #
###             ##    # # # #
###### ######## ####### # # #
###### ####             #   #
A      ######################
"""

maze_str3 = """
##    #
## ## #
#B #  #
# ## ##
     ##
A######
"""

maze_str = """
##############
#####B     ###
####  #### ###
#### ###   ###
         #####
#######A######
"""

def DFS(grafo, start, end):

     set_node = []
     frontier = [start]

     while(True):
        
          name_node = frontier.pop()
          set_node.append(name_node)

          for i in grafo.get_neighbours(grafo.get_node(name_node)):
               if i in set_node:
                    continue
               frontier.append(i)

          if name_node == end:
               break


     return set_node

def BFS(grafo, start, end):

     set_node = []
     frontier = [start]

     while(True):
        
          name_node = frontier.pop(0)
          set_node.append(name_node)

          for i in grafo.get_neighbours(grafo.get_node(name_node)):
               if i in set_node:
                    continue
               frontier.append(i)

          if name_node == end:
               break


     return set_node


if __name__ == '__main__':
    
     M = Maze(maze_str2, 'start', 'end')

     M.image_maze()
     graph = M.maze_to_graph()
     print(graph)

     path = DFS(graph, 'start', 'end')

     print(path)

     M.solution_search_image(path)



       