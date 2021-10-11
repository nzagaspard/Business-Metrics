import pandas as pd
from os import path
from numpy import random
from numpy.random import seed

def get_sample_data():
    survey_exists = path.exists('customers_survey.csv')
    if survey_exists:
        survey = pd.read_csv('customers_survey.csv')
    else:
        customer_id = random.randint(1001, 10001, 2500)
        rate = random.randint(0, 11, 2500)
        survey = pd.DataFrame({'CustId':customer_id, 'Response': rate})
        survey.to_csv('customers_survey.csv', index = False)
        survey = pd.read_csv('customers_survey.csv')

    return survey

def process_data(survey):
    survey['Category'] = survey['Response'].apply(lambda x: 'Detractors' if x <= 6 else 'Promoters' if x >= 9 else 'Passives')
    stats = pd.DataFrame(survey.Category.value_counts(normalize=True)*100)
    stats.columns = ['%']
    nps = float(stats.loc['Promoters']  - stats.loc['Detractors'])
    
    return survey, stats, nps

def read_file(file):
    file_extension = file.name.split('.')[-1]
    if file_extension in ['csv','txt']:
        data = pd.read_table(file, sep = ',', dtype = str)
    elif file_extension in ['xlsx', 'xls']:
        data = pd.read_excel(file, sep = ',', dtype = str)
    else:
        data = None
    
    if data is not None:
        number_of_columns = data.shape[1]
        if number_of_columns == 1:
            data.columns = ['Response']
        elif number_of_columns == 2:
            data.columns = ['CustId','Response']
            data = data.set_index('CustId')
    data['Response'] = data['Response'].astype(int)
    return data

def calculate_crr(bc, nc, ec):
    
    if int(ec) > (int(bc) + int(nc)): 
        return 'Not possible'
    
    else:
        crr = ((int(ec) - int(nc))/int(bc)) * 100
        return crr
 