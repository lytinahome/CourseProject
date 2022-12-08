# CourseProject -- BestDish

## (1) an overview of the project - An overview of the function of the code (i.e., what it does and what it can be used for):
+ Goal: an dish recommendation app based on jupyter notebook. 
+ By entering the name and zipcode of the restaurant (sometimes also address info if more than one restaurant can be found), the app will provide dish recommendation based on the review on yelp. The app is able to make personalized recommendation by specifying preferred food origin as well. 

## (2) team member contributions - Brief description of contribution of each team member in case of a multi-person team: 
team members: Yu Liu (yul10), Qinjingwen Cao (qcao11)

Both team members contribute equally.

## (3) related work and used libraries/models/previous projects, if any: 
depends on pandas and numpy library in python.

## (4) some sort of code structure or architecture diagram - Documentation of how the software is implemented with sufficient detail so that others can have a basic understanding of your code for future extension or any further improvement: 
Source code and links to datasets can be found in the folder `source code`.

+ step 1: convert the original database (https://www.yelp.com/dataset) from json to csv files
The unzipped Yelp database consists of several json files, for our analysis, we converted `yelp_academic_dataset_review.json` and `yelp_academic_dataset_business.json` to `review.csv` and `business.csv`, respectively. 
+ step 2: filter out the business associate with food, like "restaurant", "bar" and join the business table with review table

    In `review.csv` there is no business name, instead, a business_id was used which also appears in the `business.csv` that contains business name info and address info. This step is to filter restauratant related business entities and correlate review with business, since Yelp includes a variety of shops and services.  
+ step 3: create dish list for different countries and discover dish(es) mentioned in each review

    We collected dish names from different countries, and used them to check if a certain review has mentioned any dish(es). Then we exported the reviews where dish(es) are mentioned and the corresponding scores for this restaurant into file `merged_DishInText.csv` 
+ step 4: for each restaurant, caculated the score of each dish based on weighted average of the stars in reviews. Generated an off-line score table.
+ step 5: the UI of the app: two main functions. 1) `findRestaurant`: use name and zipcode as input and return business id. 2) `rankDish`: use business id as input and return recommended dish.
+ step 6: the personalization part: one main function: `rankDish_personalization`: use business id and food origin as input and return recommended dish.

## (5) detailed instructions for reviewers to set up and run code, including possible errors or blockers - Documentation of the usage of the software including either documentation of usages of APIs or detailed instructions on how to install and run a software, whichever is applicable:
go to the `scource code` folder and run the .ipynb file step by step.

the demo link can be found:
+ BestDish app v1.0 https://drive.google.com/file/d/1WVFKwPkJrjT4LpiaTcQBi_Y-l8FeSRT4/view?usp=sharing
+ BestDish app v2.0 https://drive.google.com/file/d/13ebIajsd_hdr8uqF449qHtzRt0laEfWD/view?usp=sharing



