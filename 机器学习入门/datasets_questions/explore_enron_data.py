#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../Final Project/final_project_dataset_unix.pkl", "rb"))

print('Size of dataset: ', len(enron_data))
print('Features of data: ', len(enron_data["SKILLING JEFFREY K"]))

poi_num = 0
for person in enron_data.keys():
	if enron_data[person]['poi'] == 1:
		poi_num += 1
print("In the dataset, there are %d POI." % poi_num)

with open(r"../Final Project/poi_names.txt",'r') as f:
	poi_total = len(f.readlines())-2
print("Total POI number is %d." % poi_total)

print('Total Stock Value of James Prentice are %.2f' % enron_data['PRENTICE JAMES']['total_stock_value'])

print('Message from Wesley Colwell to POIs are %d' % enron_data['COLWELL WESLEY']['from_this_person_to_poi']) 

print('Exercised Stock Options are %.2f' % enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

print('Total payments of Lay, Skilling and  Fastow are %.2f, %.2f, %.2f' % 
	(enron_data['LAY KENNETH L']['total_payments'], 
	enron_data['SKILLING JEFFREY K']['total_payments'], 
	enron_data['FASTOW ANDREW S']['total_payments'])
)

#print(enron_data.values())
have_salary = 0
have_email = 0
for person in enron_data.keys():
	if enron_data[person]['salary'] != 'NaN':
		have_salary += 1
	if enron_data[person]['email_address'] != 'NaN':
		have_email += 1
print("%d people have quantified salary.\n%d people have known email address." % (have_salary, have_email))

nan_total_payments = 0
for person in enron_data.keys():
	if enron_data[person]['total_payments'] == 'NaN':
		nan_total_payments += 1
print("%d people have NaN total payments. And its percentage is about %.2f%%." % (nan_total_payments, nan_total_payments/len(enron_data.keys())*100))

poi_nan_total_payments = 0
for person in enron_data.keys():
	if ((enron_data[person]['total_payments'] == 'NaN') and (enron_data[person]['poi']==True)):
		poi_nan_total_payments += 1
print("%d POI people have NaN total payments. And its percentage is about %.2f%%." % (poi_nan_total_payments, poi_nan_total_payments/poi_num*100))
