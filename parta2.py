## Part A Task 2 
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# call 2 args from command line

img1 = ""
img2 = ""
if len(sys.argv) > 2:
    img1 = sys.argv[1]
    img2 = sys.argv[2]
else:
    print("[-] Not enough arguments provided")


df = pd.read_csv("owid-covid-data.csv")

year_filter = df['date'] < '2021-01-01'

# sort values based on location 

year_2020 = df.loc[year_filter].sort_values('location')
fatality_rate = year_2020['total_deaths']/year_2020['total_cases']
new_cases = year_2020['new_cases']

# scatter plot a

plt.scatter(new_cases, fatality_rate)
plt.title("Fatality Case Rate vs Confirmed New Cases 2020")
plt.xlabel("new_cases")
plt.ylabel("case_fatality_rate")
plt.savefig('scatter-a.png')


# scatter plot b

plt.scatter(new_cases, fatality_rate)
plt.title("Fatality Case Rate vs Confirmed New Cases 2020 (log)")
plt.xlabel("new_cases (log-scale)")
plt.ylabel("case_fatality_rate")
plt.xscale("log")
plt.savefig('scatter-b.png')
