#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../Final Project/final_project_dataset_unix.pkl", "rb") )
data_dict.pop('TOTAL', 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for p in data_dict:
    try:
        if data_dict[p]['salary']>2.5e7:
            print(p, data_dict[p])
    except:
        pass
# Returns TOTAL

for p in data_dict:
    try:
        if (data_dict[p]['salary']>1e6 and data_dict[p]['bonus']>5e6):
            print(p)
    except:
        pass



for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


