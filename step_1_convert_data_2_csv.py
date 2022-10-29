import json
import pandas as pd
data_file = open(r"c:/Users/Yu/Desktop/cs410/final/yelp_academic_dataset_review.json", encoding = "utf8", errors ='replace')
data = []
for line in data_file:
    data.append(json.loads(line))
checkin_df = pd.DataFrame(data)
checkin_df.to_csv("c:/Users/Yu/Desktop/cs410/final/review.csv")
data_file.close()