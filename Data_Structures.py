#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 21:39:23 2022

@author: austenwilliams
"""



class Stack(list):
    """LIFO Stack for DFS Algorithm"""
        
    def _insert(self, node):
        
        self.append(node)
        return
        
    def _pop(self):
        if len(self) < 1:
            return None
        else:
            return self.pop()
        
    


class Queue(list):
    """""FIFO Queue for BFS"""
    
    def _insert(self, node):
        
        self.append(node)
        return
    
    def _pop(self):
        if len(self) < 1:
            return None
        else:
            return self.pop(0)
    
    
    
    
class PriorityQueue(list):
    """Queue for UCS, sorted by least cost path"""
    def _insert(self, node):
        
        if len(self) == 0:
            self.append(node)
        else:
            i = 0
            while (i < len(self) and node.path_cost > self[i].path_cost):
                i += 1

            self.insert(i, node)
            return
        
    def _pop(self):
        return self.pop(0)

class GBFSPriorityQueue(list):
    
    """Priority Queue for GBF Algorithm, sorted by number of tiles not in correct position"""
    
    def _insert(self,node):
        
        if len(self) == 0:
            self.append(node)
        else:
            i = 0
            while (i < len(self) and node.h > self[i].h):
                i += 1

            self.insert(i, node)
            return
        
    def _pop(self):
        return self.pop(0)
    
    
class Ah1PriorityQueue(list):
    """Priority Queue for A*(h1) Algorithm, sorted by number of tiles not in correct position + path cost"""
    
    def _insert(self,node):
        if len(self) == 0:
            self.append(node)
        else:
            i = 0
            while (i < len(self) and node.h1 > self[i].h1):
                i += 1

            self.insert(i, node)
            return
        
    def _pop(self):
        return self.pop(0)




class Ah2PriorityQueue(list):
    """Priority Queue for A*(h2) Algorithm, sorted by sum of Manhattan dist + path cost"""
    
    def _insert(self,node):
        if len(self) == 0:
            self.append(node)
        else:
            i = 0
            while (i < len(self) and node.h2 > self[i].h2):
                i += 1

            self.insert(i, node)
            return
        
    def _pop(self):
        return self.pop(0)
    




class Ah3PriorityQueue(list):
    """Priority Queue for A*(h3) Algorithm, sorted by sum of tile values X Manhattan distances to correct positon"""
    
    def _insert(self,node):
        if len(self) == 0:
            self.append(node)
        else:
            i = 0
            while (i < len(self) and node.h3 > self[i].h3):
                i += 1

            self.insert(i, node)
            return
        
    def _pop(self):
        return self.pop(0)
