# CourseProject -- BestDish

## (1) an overview of the project - An overview of the function of the code (i.e., what it does and what it can be used for):
+ Goal: an dish recommendation app based on jupyter notebook. 
+ BestDish app v1.0 (use case 1): the app is able to provide **dish recommendation** based on the review on yelp. User just need to input restaurant name and zipcode (sometimes also address info if more than one restaurant can be found).
+ BestDish app v2.0 (use case 2): The app is able to make **personalized dish recommendation** when user specifies preferred food origin after inputting restaurant name and zipcode. 

## (2) team member contributions - Brief description of contribution of each team member in case of a multi-person team: 
team members: Yu Liu (yul10), Qinjingwen Cao (qcao11)

Both team members contribute equally. We collaborated together throughout this project, including collecting raw data, writing code, analyzing data, finalizing the project dcumentation, etc. 

## (3) related work and used libraries/models/previous projects, if any: 
Our project depends on pandas and numpy library in python.

## (4) some sort of code structure or architecture diagram - Documentation of how the software is implemented with sufficient detail so that others can have a basic understanding of your code for future extension or any further improvement: 
Source code and links to datasets can be found in the folder `source code`.
![CS410 team project diagram](https://user-images.githubusercontent.com/43865938/206522980-36005e44-2290-4de1-8f33-b939369d4525.jpg)

+ step 1: convert the original database (https://www.yelp.com/dataset) from json to csv files

    The unzipped Yelp database consists of several json files, for our analysis, we converted `yelp_academic_dataset_review.json` and `yelp_academic_dataset_business.json` to `review.csv` and `business.csv`, respectively. 
+ step 2: filter out the business associate with food, like "restaurant", "bar" and join the business table with review table

    In `review.csv` there is no business name, instead, a business_id was used which also appears in the `business.csv` that contains business name info and address info. This step is to filter restauratant related business entities and correlate review with business, since Yelp includes a variety of shops and services.  
+ step 3: create dish list for different countries and discover dish(es) mentioned in each review

    We collected dish names from different countries, and combined them together into `all_dish.csv`. We then found out the dish(es) mentioned in each review. Then we exported the reviews where dish(es) are mentioned and the corresponding scores for this restaurant into file `merged_DishInText.csv` 
+ step 4: for each restaurant, caculated the score of each dish based on weighted average of the stars in reviews. Generated an off-line score table `score_table_mean.csv`.
+ step 5: the UI of the app: two main functions. 1) `findRestaurant`: use name and zipcode as input and return business id. 2) `rankDish`: use business id as input and return recommended dish.
+ step 6: the personalization part: one main function: `rankDish_personalization`: use business id and food origin as input and return recommended dish.

## (5) detailed instructions for reviewers to set up and run code, including possible errors or blockers - Documentation of the usage of the software including either documentation of usages of APIs or detailed instructions on how to install and run a software, whichever is applicable:
Users can refer to the `source code` folder and run the two .ipynb files: `step5_UI.ipynb` for **dish recommendation**, `step6_personalization.ipynb` for **personalized dish recommendation**. Make sure pandas and numpy have been installed on Python 3, and the three required data files (`business.csv`, `score_table_mean.csv`, `all_dish.csv`) have been downloaded and put in the same folder of the Jupyter Notebook files.

Two files are for dish recommendation and included in the demo videos below. `step5_UI.ipynb` is for user inputting a restaurant (name and zipcode) and retrieving **dish recommendation**. `step6_personalization.ipynb` is for user inputting a restaurant (name and zipcode), user's food preference and retrieving **personalized dish recommendation**.

the demo link can be found:
+ BestDish app v1.0 (`step5_UI.ipynb`) https://drive.google.com/file/d/1WVFKwPkJrjT4LpiaTcQBi_Y-l8FeSRT4/view?usp=sharing
+ BestDish app v2.0 (`step6_personalization.ipynb`) https://drive.google.com/file/d/13ebIajsd_hdr8uqF449qHtzRt0laEfWD/view?usp=sharing



