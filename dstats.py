#Q1. Descriptive Stastistics
#Student Name: Changhong He
#Student ID: 215873201
from ast import Pass
import json
import argparse
import re


#use regular expression to restrict city
def my_regex_type_city(arg_value, pat = re.compile(r"^[a-zA-Z]*$")):
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError
    return arg_value
#use regular expression to restrict state, A-Z and 2
def my_regex_type_state(arg_value, pat = re.compile(r"^[A-Z]{2}$")):
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError
    return arg_value

#Record User's input: data file name, city, province
parser = argparse.ArgumentParser(description = 'Doing the Descriptive Statistic to the yelp_academic_dataset_business.json')
parser.add_argument('fileName', type = str, help = 'the Json file name with the path')
parser.add_argument('CT', type = my_regex_type_city, help = 'the city which you chosse from the dataset')
parser.add_argument('ST', type = my_regex_type_state, help = 'the state/province of the city (case-sensitive, 2-letter)')
args = parser.parse_args()

businessList = []
#Because this data file has more than one json object, then put them into a list
with open(args.fileName, encoding= "UTF-8") as f:
    for jsonObject in f:
        businessDict = json.loads(jsonObject)
        businessList.append(businessDict)



#Question 1.1 count the number   
def countnumberofbusiness(inputcity, inputstate):
    count = 0
    #if they match, then plus one
    for i in businessList:
        if i['city'] == inputcity and i['state'] == inputstate:
            count = count + 1
    return count 

#Question 1.2 calculate the avberage number of stars 
def averagestarofbusiness(inputcity, inputstate):
    totalstars = 0.0
    for i in businessList:
        #if they match, then find the star number and plus into total stars.
        if i['city'] == inputcity and i['state'] == inputstate:
            totalstars = totalstars + i['stars']
    
    res = totalstars / countnumberofbusiness(inputcity, inputstate)
    return round(res, 2)   

#Question 1.3 the number of restaurants in the city, state
def numberofrestaurants(inputcity, inputstate):
    count = 0
    #if they match, then plus into count
    for i in businessList:
        if i['city'] == inputcity and i['state'] == inputstate and 'Restaurants' in str(i['categories']):
            count = count + 1
            
    return count

#Question1.4 The average number of stars of restaurants in the city 
def averagestarofrestaurant(inputcity, inputstate):
    totalstars = 0.0
    #it they match, then record stars and add into total star, divde by total restaruants number
    for i in businessList:
        if i['city'] == inputcity and i['state'] == inputstate and 'Restaurants' in str(i['categories']):
                totalstars = totalstars + i['stars']
    res = totalstars / numberofrestaurants(inputcity, inputstate)
    return round(res, 2)

#Question1.5 The average number of reviews for all businesses in the city
def averagenumberofreviewbusiness(inputcity, inputstate):
    totalreview = 0.0
    for i in businessList:
        if i['city'] == inputcity and i['state'] == inputstate:
            totalreview = totalreview + i['review_count']
    averagereview = totalreview / countnumberofbusiness(inputcity, inputstate)
    res = round(averagereview, 2)
    return res

#Question1.6 The average number of Reviews for Restaurants in the city
def averagenumberofreviewrestaurants(inputcity, inputstate):
    totalreview = 0.0
    for i in businessList:
        if i['city'] == inputcity and i['state'] == inputstate and 'Restaurants' in str(i['categories']):
                totalreview = totalreview + i['review_count']
    averagereview = totalreview / numberofrestaurants(inputcity, inputstate)
    res = round(averagereview, 2)
    return res

#Output
if __name__ == "__main__":
    with open('Q1.out','w') as f:
        f.write(str(countnumberofbusiness(args.CT, args.ST)) + '\n')
        f.write(str(averagestarofbusiness(args.CT, args.ST)) + '\n')
        f.write(str(numberofrestaurants(args.CT, args.ST)) + '\n')
        f.write(str(averagestarofrestaurant(args.CT, args.ST)) + '\n')
        f.write(str(averagenumberofreviewbusiness(args.CT, args.ST)) + '\n')
        f.write(str(averagenumberofreviewrestaurants(args.CT, args.ST)) + '\n')