#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 20:45:23 2022

@author: austenwilliams
"""

import Data_Structures
from Search import Search_Class

def pick_level():
    "Pick level of difficulty for specified search"
    
    level = eval(input("What level of difficulty would you like?\n1. Easy\n2. Medium\n3. Hard\nPlease input numeric value between 1 - 3: "))
    
    while(level < 1 or level > 3):
        level = eval(input("What level of difficulty would you like?\n1. Easy\n2. Medium\n3. Hard\nPlease input numeric value between 1 - 3: "))
    print()
    return level

def print_results(result_arr):
    "Prints results of historical searches"
    
    print()
    if len(result_arr) == 0:
        print("No search Results")
        return
    for result in result_arr:
        print(result)

def pick_search():
    "Function used to determine which type of search will be implemented"
    
    text = eval(input("What type of search would you like today?\n1. BFS\n2. DFS\n3. UCS\n4. GBF\n5. A*\n6. Results\nPlease input numeric value between 1 - 6: "))
    
    while (text < 1 or text > 6):
        text = eval(input("What type of search would you like today?\n1. BFS\n2. DFS\n3. UCS\n4. GBF\n5. A*\n6. Results\nPlease input numeric value between 1 - 6: "))
    return text

def pick_heuristic():
    "Function used to determine which implementation of A* should be chosen"
    
    search = eval(input("Which A* search would you like to implement?\n1. A*(h1)\n2. A*(h2)\n3. A*(h3): "))
    while (search < 1 or search > 3):
        search = eval(input("Which A* search would you like to implement?\n1. A*(h1)\n2. A*(h2)\n3. A*(h3): "))
    return search
    

def main():
    "Main UI function for Algorithm and Difficulty Selection"
    
    problem = dict()
    problem[1] = ("Easy", [1,3,4,8,6,2,7,0,5])
    problem[2] = ("Medium", [2,8,1,0,4,3,7,6,5])
    problem[3] = ("Hard", [5,6,7,4,0,8,3,2,1])
    goal = [1,2,3,8,0,4,7,6,5]

    run = "yes"
    
    result_arr = list()
    
    
    while (run != "exit"):
        choice = pick_search()
        if choice == 1:
            #BFS Algorithm
            level = pick_level()
            queue = Data_Structures.Queue()
            print(f'BFS on {problem[level][0]}')
            print()
            result = Search_Class(problem[level][1], goal, queue)
            result_arr.append(f'BFS on {problem[level][0]},' + ' ' + result.search())
        elif choice == 2:
            #DFS Algorithm
            level = pick_level()
            stack = Data_Structures.Stack()
            print(f'DFS on {problem[level][0]}')
            print()
            result = Search_Class(problem[level][1], goal, stack)
            result_arr.append(f'DFS on {problem[level][0]},' + ' ' + result.search())
        elif choice == 3:
            #UCS Algorithm
            level = pick_level()
            p_queue = Data_Structures.PriorityQueue()
            print(f'UCS on {problem[level][0]}')
            print()
            result = Search_Class(problem[level][1], goal, p_queue)
            result_arr.append(f'UCS on {problem[level][0]},' + ' ' + result.search())
        elif choice == 4:
            #GBF Algorithm
            level = pick_level()
            gbfs_queue = Data_Structures.GBFSPriorityQueue()
            print(f'GBF on {problem[level][0]}')
            print()
            result = Search_Class(problem[level][1], goal, gbfs_queue)
            result_arr.append(f'GBF on {problem[level][0]},' + ' ' + result.search())
        elif choice == 5:
            #A* Searches
            search = pick_heuristic()
            if search == 1:
                #A*(h1) Algorithm
                level = pick_level()
                ah1_queue = Data_Structures.Ah1PriorityQueue()
                print(f'A*(h1) on {problem[level][0]}')
                print()
                result = Search_Class(problem[level][1], goal, ah1_queue)
                result_arr.append(f'A*(h1) on {problem[level][0]},' + ' ' + result.search())
            elif search == 2:
                #A*(h2) Algorithm
                level = pick_level()
                ah2_queue = Data_Structures.Ah2PriorityQueue()
                print(f'A*(h2) on {problem[level][0]}')
                print()
                result = Search_Class(problem[level][1], goal, ah2_queue)
                result_arr.append(f'A*(h2) on {problem[level][0]},' + ' ' + result.search())
            elif search == 3:
                #A*(h3) Algorithm
                level = pick_level()
                ah3_queue = Data_Structures.Ah3PriorityQueue()
                print(f'A*(h3) on {problem[level][0]}')
                print()
                result = Search_Class(problem[level][1], goal, ah3_queue)
                result_arr.append(f'A*(h3) on {problem[level][0]},' + ' ' + result.search())
            else:
                print(f'***Invalid input {search}')
        elif choice == 6:
            print_results(result_arr)
        else:
            print("invalid input")
            
        
        run = input("\nWould you like to run another search algorithm?\nPress any key to continue or type \"exit\" to quit: ").lower()
        
        
if __name__ == "__main__":
    main()
            
