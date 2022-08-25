#Q3. Creating the Yelp Social Network
#Student Name: Changhong He
#Student ID: 215873201
import argparse
import re
import json
import networkx as nx

#set the n number, n must >= 100, otherwise it will have exception
def my_regex_type_usefulvote(arg_value, pat = re.compile(r"^0*[1-9]\d{2,}$")):
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError
    return int(arg_value)


#use parser to set input
parser = argparse.ArgumentParser(description = 'Doing the Social Network to the yelp_academic_dataset_user.json')
parser.add_argument('fileName', type = str, help = 'the Json file name with the path')
parser.add_argument('useful_votes', type = my_regex_type_usefulvote, help = 'the number of useful vote for the yelp user, number >= 100')

args = parser.parse_args()

#create the graph
G = nx.Graph()
#record the user object from the user.json. each user object is a dict.
userlist = []
#each user object will have >= n number of useful number
usefuluserlist = []
#Graph(V, E): V is a set of vertices representing the Yelp users
#Graph(V, E): E is a set of edges representing friendships between Yelp users
#Because this data file has more than one json object, then put them into a list
with open(args.fileName, encoding= "UTF-8") as f:
    for jsonObject in f:
        userDict = json.loads(jsonObject)
        userlist.append(userDict)

for eachuser in userlist:
    #add user with >= usefulvote number into a new list
    if eachuser['useful'] >= args.useful_votes:
        usefuluserlist.append(eachuser['user_id'])

for eachuser in userlist:
    if eachuser['useful'] >= args.useful_votes:
        if eachuser['user_id'] not in G:
            #Add vertice
            G.add_node(eachuser['user_id'])
        #get the friend string from the user dict
        friendstr = str(eachuser['friends'])
        # because it is the string, so separate by comma(',') and add them into a new list called friend list
        friendslist = [i.strip() for i in friendstr.split(',')]
        for eachfriends in friendslist:
            #check if the friends has valid useful number and if the graph has the edge between (eachuser['user_id'], eachfriends)
            if eachfriends in usefuluserlist and not G.has_edge(eachuser['user_id'], eachfriends):
                #Add friends node and add edge between them
                G.add_node(eachfriends)
                G.add_edge(eachuser['user_id'], eachfriends)

#Write the output 
with open('Q3.out','w') as f:
    for eachedge in G.edges:
        f.write(' '.join(str(x) for x in eachedge) + '\n')

