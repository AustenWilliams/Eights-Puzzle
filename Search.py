#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 20:33:23 2022

@author: austenwilliams
"""

import time
from Node_Class import Node





class Search_Class:

    def __init__(self, problem, goal, data_structure):
        self.root = Node(problem, self._find_root(problem))
        self.goal = goal
        self.data_struct = data_structure
        self.visited = list()
        self.solution = list()
        self.moves = 0
        self.cost = 0
        self.nodes_popped = 0
        self.max_queue = 0
        self.start_time = time.gmtime(time.time())
        
        

        
    
    def _find_root(self, problem):
        """Function used to find the root node"""
        for i in range(0, len(problem) - 1):
            if problem[i] == 0:
                return i    

        
    def search(self):
        """Function used to implement various search algorithms"""

        self.solution.insert(0, self.root)
        
        if self.root.state == self.goal:
            self._print(self.solution)
            return f'Length = {self.moves}, Cost = {self.cost}, Time = {self.nodes_popped}, Space = {self.max_queue}'
        
        self.heuristics(self.root)
        
        self.data_struct.append(self.root)
        
        while len(self.data_struct) > 0:
            
            elapsed_time = time.gmtime(time.time())
            
            if (abs(elapsed_time[4] - self.start_time[4]) >= 5):
                text = f'Function surpassed excecution time of 5 min. Elapsed time = {elapsed_time[4] - self.start_time[4]} Length = {self.moves}, Cost = {self.cost}, Time = {self.nodes_popped}s, Space = {self.max_queue}'
                print(text)
                return text
            
            
            
            self.max_queue = max(len(self.data_struct), self.max_queue)
            
            popped_node = self.data_struct._pop()
            
            self.nodes_popped += 1
            
            for node in popped_node.adjacency_list():
                
                if node.state not in self.visited:
                    
                    if node.state == self.goal:
                        while(node.parent):
                            self.moves += 1
                            self.solution.insert(1, node)
                            node = node.parent
                        self._print(self.solution)
                        return f'Length = {self.moves}, Cost = {self.cost}, Time = {self.nodes_popped}, Space = {self.max_queue}'
                    self.heuristics(node)
                    self.data_struct._insert(node)
            self.visited.append(popped_node.state)

            
            
    
    def heuristics(self, node):
        """Function used to calculate Heuristics for particular node/state"""
        node_misplaced_tiles = 0
        node_manhattan = 0
        sum_tiles = 0
        path_cost = node.path_cost
        for i in range(0, len(node.state)):
            tile_value = node.state[i]
            if tile_value == 0:
                tile_value += 0
            elif tile_value != self.goal[i]:
                node_misplaced_tiles += 1
                manhattan_s = abs(i - self.goal.index(node.state[i]))
                if manhattan_s >= 3:
                    manhattan_s = (manhattan_s % 3) + (manhattan_s // 3)
                node_manhattan += manhattan_s
                sum_tiles += (tile_value * manhattan_s)
        node.h = node_misplaced_tiles
        node.h1 = node_misplaced_tiles + path_cost
        node.h2 = path_cost + node_manhattan
        node.h3 = sum_tiles + path_cost 
        
            
            
    def convert(self, lst):
        """Converts list into 2d matrix representation of 8-puzzle"""
        k = 0
        new = [[],[],[]]
        for i in range(0,3):
            for j in range(0,3):
                new[i].append(lst[k])
                k +=1
        return new
    
    
    def _print(self, node_list):
        """Function to print states in 2d format to the screen"""
        cost = 0
        for node in node_list:
            count = 0
            matrix = self.convert(node.state)
            for row in matrix:
                count += 1
                if count == 2:
                    cost += node.path_cost
                    print(f'{row} Action = {node.action}, depth = {node.depth}, cost = {node.path_cost}, total cost = {cost} misplaced tiles = {node.h}')
                else:
                    print(row)
            print()
        self.cost = cost
        print(f'Length = {self.moves}, Cost = {self.cost}, Time = {self.nodes_popped}, Space = {self.max_queue}')
    

    
            
            
    


    
        
        
    

    
