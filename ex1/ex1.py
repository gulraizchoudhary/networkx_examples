# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 21:49:05 2022

@author: gulrch
"""

import networkx as nx

G = nx.DiGraph()

#sample json keys are labels and list contains sequences
data = {'1': ['B', 'D'],
         '2': ['B', 'D', 'E'],
         '3': ['A', 'F'],
         '4': ['B'],
         '5': ['B', 'D', 'C'],
         '6': ['C', 'E']}


#iterate through the graph
for lst, key in enumerate(data.keys()):
       prev = "STR"
       
       for item in data[key]:
            #maintain frequencies of occurrence of a node in data            
            if item not in G.nodes():
                G.add_node(item)
                G.nodes[item]['labels']=1               
            else:
                G.nodes[item]['labels']+=1
                
            #maintain labels of termopral co-occurrence in data
            if not G.has_edge(prev, item):  
                G.add_edge(prev, item)
                G.edges[prev, item]['weight'] =[key]
            else:
                G.edges[prev, item]['weight'].append(key)
                    
            prev = item


G.nodes['B']['labels']
#Out: 4

G['B']['D']['weight']
#Out: ['1', '2', '5']


#write graph in gml format
nx.write_gml(G, "graph.gml")


#read back the graph
H = nx.read_gml("graph.gml")
H.nodes['B']['labels']
# out: 4


H['B']['D']['weight']
#Out: ['1', '2', '5']

