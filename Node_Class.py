#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 20:39:23 2022

@author: austenwilliams
"""

class Node:
    
    def __init__(self, state, index_0 , action="Start", path_cost=0, depth=0, parent=None):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.action = action
        self.index = index_0
        self.path_cost = path_cost
        self.children = None
        self.h = 0
        self.h1 = 0
        self.h2 = 0
        self.h3 = 0
        
    def adjacency_list(self):
        """ Creates adjacency list for node instance"""
        adj_nodes = list()
        index = self.index
        depth = self.depth + 1
        state = self.state.copy()
        path_cost = 0
        if((index - 3) >= 0): #Up is equivelent to 3 linear moves left when representing an array as a 3 x 3 board
            up_index = index - 3
            path_cost = self.state[up_index]
            up_node = Node(self._swap(state,up_index, index), up_index, "Up", path_cost, depth, self)
            adj_nodes.append(up_node)
        if((index + 3) < (len(self.state) - 1) ):#Down is equivelent to 3 linear moves right when representing an array as a 3 x 3 board
            down_index = index + 3
            path_cost = self.state[down_index]
            down_node = Node(self._swap(state,down_index, index), down_index, "Down", path_cost, depth, self )
            adj_nodes.append(down_node)
        if((index - 1) >= 0 and index % 3 != 0): #Left is equivelent to 1 linear move to the left when representing an array as a 3 x 3 board
            left_index = index - 1
            path_cost = self.state[left_index]
            left_node = Node(self._swap(state,left_index, index),left_index, "left", path_cost, depth, self)
            adj_nodes.append(left_node)
        if((index + 1) <= (len(self.state) - 1) and (index+1) % 3 != 0): #Right is equivelent to 1 linear move to the right when representing an array as a 3 x 3 board
            right_index = index + 1
            path_cost = self.state[right_index]
            right_node = Node(self._swap(state,right_index, index),right_index, "Right", path_cost, depth, self)
            adj_nodes.append(right_node)
        self.children = adj_nodes
        return adj_nodes
    
    
    def _swap(self, lst, new, old):
        """"Utility functioned used to move from one state to the next"""
        state = lst.copy()
        temp = state[new]
        state[new] = state[old]
        state[old] = temp
        return state

