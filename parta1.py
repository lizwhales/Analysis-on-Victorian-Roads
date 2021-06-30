## Part A Task 1
import pandas as pd
import argparse

covid_data = pd.read_csv('owid-covid-data.csv', parse_dates=['date'])

covid_data['month'] = covid_data['date'].dt.strftime('%m')

covid_data = covid_data[covid_data['date'].dt.year == 2020]

covid_data = covid_data.sort_values(['location','month'], ascending=True)

covid_data= covid_data.groupby(['location', 'month']).aggregate({
    'total_cases' : 'sum',
    'new_cases' : 'sum',
    'total_deaths': 'sum',
    'new_deaths' : 'sum'
})

# remove those with no entries for certain combinations
covid_data = covid_data.dropna(subset=['total_cases','total_deaths','new_deaths'])


# returning the aggregated values of four variables
covid_data

fatality_list = []

for i, value in enumerate(covid_data['total_cases']):
    if value:
        case_fatality_val = covid_data['total_deaths'][i]/covid_data['total_cases'][i]
        fatality_list.append(case_fatality_val)
    else:
        fatality_list.append(0)
        
covid_data.insert(0, 'case_fatality_rate', fatality_list, True)

covid_data


covid_data.head(5).to_csv('\owid-covid-data-2020-monthly.csv', index = False)
