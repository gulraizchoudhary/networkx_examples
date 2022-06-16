# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 10:56:06 2022

@author: gulrch
"""

import networkx as nx

G = nx.DiGraph()

#sample json keys are labels and list contains sequences (A sequence can a be a set of temporal ICD-10 codes)
data = {'1': {'gender':'M' ,'age':'20-30', 'sequence': ['B', 'D']},
         '2':{'gender':'M','age':'20-30', 'sequence': ['B', 'D', 'E']},
         '3': {'gender':'F','age':'20-30','sequence':['A', 'F']},
         '4': {'gender':'F','age':'20-30', 'sequence':['B']},
         '5': {'gender':'M', 'age':'20-30', 'sequence':['B', 'D', 'C']},
         '6': {'gender':'F', 'age':'20-30', 'sequence': ['E', 'F']}}


#iterate through the graph
for lst, key in enumerate(data.keys()):
     
       gender = data[key]['gender']
       age_group = data[key]['age']
       
        
       start = 'STR'
       term = 'END'
       
       #Add nodes if they don't exist
       if not start in G.nodes:
           G.add_node(start)
       if not term in G.nodes:
           G.add_node(term)
            
       if not gender in G.nodes:
           G.add_node(gender)
            
       if not age_group in G.nodes:
           G.add_node(age_group)
            
       #add starting edges if the don't exist
       if not G.has_edge(start, gender):
           G.add_edge(start, gender)
           G.edges[start, gender]['weight']=0
    
       if not G.has_edge(gender, age_group):    
           G.add_edge(gender,age_group)
           G.edges[gender, age_group]['weight']=0
       flag = True
       prev = ""
       for item in data[key]['sequence']:
          
           #maintain frequencies of occurrence of a node in data
           if item not in G.nodes():
               G.add_node(item)
               G.nodes[item][gender]={}
               G.nodes[item][gender][age_group]={}
               G.nodes[item][gender][age_group]['weight']=1               
           else:
               if gender not in G.nodes[item]:
                   G.nodes[item][gender]={}
                    
               if age_group not in G.nodes[item][gender]:
                    G.nodes[item][gender][age_group]={}
                    G.nodes[item][gender][age_group]['weight']=1  
               else:
                    G.nodes[item][gender][age_group]['weight']+=1
           if flag:
               flag = False
               prev =age_group
               
           if not G.has_edge(prev, item):  
               G.add_edge(prev, item)
               G.edges[prev, item]['weight'] ={}
               G.edges[prev, item]['weight'][gender] ={}
               G.edges[prev, item]['weight'][gender][age_group] =[key]
           else:
               if gender not in G.edges[prev, item]['weight']:
                   G.edges[prev, item]['weight'][gender] ={}
                    
                    
               if age_group not in G.edges[prev, item]['weight'][gender]:
                   G.edges[prev, item]['weight'][gender][age_group] =[key]
               else:    
                   G.edges[prev, item]['weight'][gender][age_group].append(key)
                
           prev = item
           
        #Termination node
       if not G.has_edge(item, term):  
           G.add_edge(item, term)
           G.edges[item, term]['weight'] ={}
           G.edges[item, term]['weight'][gender] ={}
           G.edges[item, term]['weight'][gender][age_group] =[key]
       else:
           if gender not in G.edges[item, term]['weight']:
                G.edges[item, term]['weight'][gender] ={}
           if age_group not in G.edges[item, term]['weight'][gender]:
                G.edges[item, term]['weight'][gender][age_group] =[key]
           else:
                G.edges[item, term]['weight'][gender][age_group].append(key)