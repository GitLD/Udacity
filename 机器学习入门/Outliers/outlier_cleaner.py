#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    res = [abs(prediction - net_worth) for (prediction, net_worth) in zip(predictions, net_worths)]
    res_sort = res.copy()
    res_sort.sort()
    del_num = int(0.1*len(res))
    for i in range(len(res)):
        if res[i] not in res_sort[-del_num:]:
            cleaned_data.append((ages[i], net_worths[i], res[i]))
    return cleaned_data

