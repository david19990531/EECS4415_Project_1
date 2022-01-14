# EECS 4415 Assignment 1

**Data Analytics using Python (10%)**

**Start:** February 1, 2022, at 09:00 am EST   
**Due:** February 15, 2022, at 09:00 pm EST

## Objective

This assignment involves performing basic analytics on a large-scale dataset using Python. The dataset is a subset of Yelp's businesses, reviews, and user data. 
It was originally put together for the Yelp Dataset Challenge which is a chance for students to conduct research or analysis on Yelp's data and share their discoveries. The dataset consists of five JSON files, which contain information about businesses across 8 metropolitan areas in the USA and Canada.
The dataset can be found and downloaded [here](https://www.kaggle.com/yelp-dataset/yelp-dataset/version/3) (registration to Kaggle is required).

In this assignment, you will write four Python scripts/programs. The first program (`dstats.py`) performs descriptive analytics of the dataset. The second (`dist.py`) computes useful frequency distributions. The third (`network.py`) constructs a social network of Yelp friends. The fourth (`graph.py`) performs basic network analytics.

## Implementation
* Clone this repository and implement your solution in each corresponding file. 
* The three lines in the `info.txt` file include information about you (first name, last name, and 9-digit student ID). Please update the `info.txt` file accordingly.
* Output the dependencies of your solution into `requirements.txt` in requirements format (using the [`pip freeze`](https://pip.pypa.io/en/stable/cli/pip_freeze/) command).
* All scripts are to be written using Python >= 3.7.0.

Important notes:
* You should strictly follow the implementation instructions and the input/output format. Implementations that do not follow the correct format will be marked as 0.
* You may NOT change the file name of the Python scripts.
* To get full marks, your code must be well-commented.


## Submission
You need to zip the repository and submit one zip file with the name of `assignment1.zip` on eClass by the due date. The directory structure in `assignment1.zip` should look like this:

```
EECS4415_Assignment_1/
├─ dstats.py
├─ dist.py
├─ network.py
├─ graph.py
├─ requirements.txt
├─ info.txt
├─ README.md
```
You should strictly follow the directory structure. Implementations that do not follow the correct directory structure will be marked as 0.

## Evaluation
An automated judge will programmatically evaluate the majority part of your solution. TAs will assess the parts that cannot be programmatically judged (e.g., charts and code comments). Please refer to each question for the detailed breakdown of assignment marks.

