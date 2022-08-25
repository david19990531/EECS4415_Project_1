#Q4. Computing the network statistic
#Student Name: Changhong He
#Student ID: 215873201
import networkx as nx
import argparse



parser = argparse.ArgumentParser(description = 'Given a Yelp social network as an edge list in a text file and answer the four questions')
parser.add_argument('user_id_file', type = str, help = 'The txt files which contains the yelp users id')
args = parser.parse_args()

G = nx.Graph()
with open(args.user_id_file) as f:
    #open the file and read the lines, each line is a list['str']
    lines = f.readlines()
    #so get the str in the list
    for friendstr in lines:
    #separate them by space, because the format of output of Q3
        friendslist = [i.strip() for i in friendstr.split(' ')]
        if friendslist[0] not in G:
            G.add_node(friendslist[0])
        if friendslist[1] not in G:
            G.add_node(friendslist[1])
        G.add_edge(friendslist[0], friendslist[1])

# It will help to count the number of neighbor and help to calculate average
totalneighbor = 0.0
for eachuserneighbor in G:
    #the method in the G, G.neighbor(x) will return a list of neighbor
    totalneighbor = totalneighbor + len(list(G.neighbors(eachuserneighbor)))
avgneighbor = totalneighbor / nx.number_of_nodes(G)
#the way to calculate connected components is that using the method number_connected_components(G)
numberofcomponents = nx.number_connected_components(G)
#Find the triangles relationship in the graph
numberoftriangles = int(sum(nx.triangles(G).values()) / 3)
#output
with open('Q4.out','w') as f:
    f.write(str(nx.number_of_nodes(G)) + '  ' + str(nx.number_of_edges(G)) + '\n')
    f.write(str(round(avgneighbor, 2)) + '\n')
    f.write(str(numberofcomponents) + '\n')
    f.write(str(numberoftriangles) + '\n')