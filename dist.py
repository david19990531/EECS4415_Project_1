#Q2. Distribution Statistics
#Student Name: Changhong He
#Student ID: 215873201
import json
import argparse
import re
from matplotlib import pyplot as plt
import numpy as np

#use regular expression to restrict city
def my_regex_type_city(arg_value, pat = re.compile(r"^[a-zA-Z]*$")):
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError
    return arg_value

#use regular expression to restrict state
def my_regex_type_state(arg_value, pat = re.compile(r"^[A-Z]{2}$")):
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError
    return arg_value

#Record User's input: data file name, city, province
parser = argparse.ArgumentParser(description = 'Doing the Distribution Statistic to the yelp_academic_dataset_business.json')
parser.add_argument('fileName', type = str, help = 'the Json file name with the path')
parser.add_argument('CT', type = my_regex_type_city, help = 'the city which you chosse from the dataset')
parser.add_argument('ST', type = my_regex_type_state, help = 'the state/province of the city (case-sensitive, 2-letter)')
args = parser.parse_args()

businessList = []
'''
for i in businessList:
    categories_str = i['categories']
    if categories_str is not None:
        categories_list = [i.strip() for i in categories_str.split(',')]
        if categories_str and 'Restaurants' in categories_str:
            for categories_object in categories_list:
                if categories_object not in single_categories:
                    single_categories.append(categories_object)
                else:
                    pass
 
for items in single_categories:
    print(items, end = '\n') 


Using above code to find all the categories with restaurants, and hand-picked all the geographical categories
'''
categories_geographical_restaurants = ['American (Traditional)', 'Thai', 'American (New)', 'Italian', 'Mediterranean', 'Greek', 'Mexican', 'Indian', 'Chinese', 'Kosher', 'Caribbean', 'Puerto Rican', 'Taiwanese', 'Vietnamese', 'Korean', 'Japanese', 'Canadian (New)', 'Brazilian', 'Cuban', 'German', 'African', 'Southern', 'Asian Fusion', 'French', 'Middle Eastern', 'Persian\/Iranian', 'Latin American', 'Filipino', 'Cajun\/Creole', 'Himalayan\/Nepalese', 'Turkish', 'Modern European', 'Austrian', 'Hawaiian', 'Irish', 'Irish Pub', 'Lebanese', 'Pakistani', 'Peruvian', 'Russian', 'Colombian', 'Portuguese', 'Venezuelan', 'Ethiopian', 'Malaysian', 'Tuscan', 'Hungarian', 'Donairs', 'British', 'Salvadoran', 'Cantonese', 'Acai Bowls', 'Spanish', 'Somali', 'Argentine', 'Dominican', 'Jewish', 'Cambodian', 'Singaporean', 'Pan Asian', 'Szechuan', 'Haitian', 'New Mexican Cuisine', 'Basque', 'Indonesian', 'Laotian', 'Mongolian', 'Moroccan', 'Burmese', 'Guamanian', 'Honduran', 'Arabian', 'Belgian', 'Afghan', 'South African', 'Polish', 'Eritrean', 'Trinidadian', 'Egyptian', 'Georgian', 'Senegalese', 'Ukrainian', 'Armenian', 'Shanghainese', 'Oaxacan', 'Scottish', 'Hong Kong Style Cafe', 'Australian', 'Scandinavian', 'Sicilian', 'Uzbek', 'Bulgarian', 'Bangladeshi', 'Swiss Food', 'Syrian', 'Sri Lankan', 'Swiss Food', 'Syrian', 'Sri Lankan', 'French Southwest', 'Czech', 'Czech\/Slovakian', 'Calabrian', 'Nicaraguan', 'Catalan', 'Sardinian', 'Mauritius', 'Iberian', 'Polynesian', 'Pueblan', 'Oriental']
#Because this data file has more than one json object, then put them into a list
with open(args.fileName, encoding= "UTF-8") as f:
    for jsonObject in f:
        businessDict = json.loads(jsonObject)
        businessList.append(businessDict)


def numofcountryforrestaurants(inputcity, inputstate):
    #Create the result of count_categories_dict
    count_categories_dict = {}                                   
    for i in businessList:
        #Find the "city" & "State" exist in the dataset
        if i['city'] == inputcity and i['state'] == inputstate:
            #get their categories information
            categories_str = str(i['categories'])
            if 'Restaurants' in categories_str:
                categories_list = [i.strip() for i in categories_str.split(',')]
                for eachitem in categories_list:
                    #Because I already get the all the geographical categories, then just compare, 
                    # if not exist then add into count_categories_dict. else find the value and + 1
                    if eachitem in categories_geographical_restaurants:
                        if eachitem not in count_categories_dict.keys():
                            count_categories_dict[eachitem] = 1
                        else:
                            count_categories_dict[eachitem] = count_categories_dict[eachitem] + 1
    count_list = [(count_categories_dict[i],i) for i in count_categories_dict]
    count_list_sort = sorted(count_list, reverse=True)
    #write them into Q2_part1.put
    with open('Q2_part1.out','w') as f:
        for i,value in enumerate(count_list_sort):
            if i < 10:
                f.write(value[1] + ':' + str(value[0]) + '\n')

def averageofreviewcountrestaurants(inputcity, inputstate):

    count_categories_dict = {}
    review_count_categories_dict = {}                                   
    for i in businessList:
        #Find the "city" & "State" exist in the dataset
        if i['city'] == inputcity and i['state'] == inputstate:
            #get their categories information
            categories_str = str(i['categories'])
            if 'Restaurants' in categories_str:
                categories_list = [i.strip() for i in categories_str.split(',')]
                for eachitem in categories_list:
                    #Because I already get the all the geographical categories, then just compare, 
                    # if not exist then add into count_categories_dict. else find the value and + 1
                    if eachitem in categories_geographical_restaurants:
                        if eachitem not in count_categories_dict.keys():
                            #if it is not in the dict before, then set it to be 1, record review count
                            count_categories_dict[eachitem] = 1
                            review_count_categories_dict[eachitem] = i['review_count']
                        else:
                            #if it is in the dict before, then let it plus one, and plus review count
                            count_categories_dict[eachitem] = count_categories_dict[eachitem] + 1
                            review_count_categories_dict[eachitem] = review_count_categories_dict[eachitem] + i['review_count']
    count_list = [(review_count_categories_dict[i],i) for i in review_count_categories_dict]
    count_list_sort = sorted(count_list, reverse=True)    
    #output
    with open('Q2_part2.out','w') as f:
        for i,value in enumerate(count_list_sort):
            if i < 10:
                f.write(value[1] + ':' + str(value[0]) + ':' + str(round(value[0] / count_categories_dict[value[1]] ,2)) + '\n')

def barcharttopfive(inputcity, inputstate):
    #Create the result of count_categories_dict
    topfivelist_x = []
    topfivelist_y = []
    count_categories_dict = {}                                   
    for i in businessList:
        #Find the "city" & "State" exist in the dataset
        if i['city'] == inputcity and i['state'] == inputstate:
            #get their categories information
            categories_str = str(i['categories'])
            if 'Restaurants' in categories_str:
                categories_list = [i.strip() for i in categories_str.split(',')]
                for eachitem in categories_list:
                    #Because I already get the all the geographical categories, then just compare, 
                    # if not exist then add into count_categories_dict. else find the value and + 1
                    if eachitem in categories_geographical_restaurants:
                        if eachitem not in count_categories_dict.keys():
                            count_categories_dict[eachitem] = 1
                        else:
                            count_categories_dict[eachitem] = count_categories_dict[eachitem] + 1
    count_list = [(count_categories_dict[i],i) for i in count_categories_dict]
    count_list_sort = sorted(count_list, reverse=True)
    #Top 5, append them into 2 list
    y = 0
    for x in count_list_sort:
        if y < 5:
            topfivelist_x.append((x[1]))
            topfivelist_y.append(x[0])
            y = y + 1

    #creat bar
    new_position_x = np.arange(len(topfivelist_x))
    #set size to 10 inch * 10 inch
    plt.figure(figsize = (10, 10))
    plt.xticks(new_position_x, topfivelist_x)
    plt.bar(new_position_x, topfivelist_y, color = '#e5ae38')
    plt.title("The top-5 restaurants categories")
    plt.xlabel("x- restaurant category")
    plt.ylabel("y- frequency of the Restaurants(#restaurants)") 
    plt.savefig("Q2_part3.pdf", dpi =200)

#Output
if __name__ == "__main__":
    #Output Q2_part1
    numofcountryforrestaurants(args.CT, args.ST)
    #Output Q2_part2
    averageofreviewcountrestaurants(args.CT, args.ST)
    #Output Q2_part3
    barcharttopfive(args.CT, args.ST)