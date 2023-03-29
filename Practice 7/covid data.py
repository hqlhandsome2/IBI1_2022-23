import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# change path to where "full_data.csv" is downloaded
os.chdir("/Users/yaokaiwen/IBI1_2022-23/Practical7")
# import data from a CSV file
covid_data=pd.read_csv ("full_data.csv")
# print the first five lines of file. For code"head(x)", x means the total number of lines.
print(covid_data.head(2))
#  the name of each column, the number of non-null entries, the data type, and other summary information about the DataFrame are printed.
covid_data.info()

# --------------------------------------------------------------------------------------------------------------

# show the second column from every 100th row from the first 1000 rows
print(covid_data.iloc[0:1001:100,1])
# 0       Afghanistan
# 100         Albania
# 200         Andorra
# 300         Armenia
# 400       Australia
# 500         Austria
# 600      Azerbaijan
# 700         Bahrain
# 800         Belarus
# 900         Belgium
# 1000        Bolivia

# ------------------------------------------------------------------------------------------------------------

# The appropriate Boolean array member is True if a value equals "Afghanistan," otherwise False. By providing covid data['afghanistan'] with this Boolean array
covid_data['afghanistan'] = (covid_data['location'] == 'Afghanistan')
# Filter out the rows where the 'afghanistan' column equals True, and then print the 'total_cases' column of the filtered row.
print(covid_data.loc[covid_data['afghanistan'] == True,"total_cases"])
# 0       0
# 1       0
# 2       0
# 3       0
# 4       0
#      ...
# 77     75
# 78     91
# 79    106
# 80    114
# 81    141

# ------------------------------------------------------------------------------------------------------------

# The appropriate Boolean array member is True if a value equals "2020-03-31", otherwise False. By providing covid data['20200331'] with this Boolean array
covid_data['20200331'] = (covid_data['date'] == '2020-03-31')
# create a new_data to store only the data on new cases and deaths for 31 March.
new_data = covid_data.loc[covid_data['20200331'] == True,["new_cases","new_deaths"]]
# use np to calculate the mean of "new_cases" and "new_deaths"
mean_new_cases=np.mean(new_data["new_cases"])
mean_new_deaths=np.mean(new_data["new_deaths"])
print("Mean New Cases:", mean_new_cases)
print("Mean New Deaths:", mean_new_deaths)
# Mean New Cases: 640.4615384615385
# Mean New Deaths: 37.92820512820513

# --------------------------------------------------------------------------------------------------------------

# draw two separate box plots.

labels = 'new_cases'
# create a "new_cases_data" to store the data of "new_cases" in "new_data"
new_cases_data = new_data["new_cases"]
# draw a figure
plt.boxplot(new_cases_data)
# put a title
plt.title('new cases')
plt.show()

labels = 'new_deaths'
# create a "new_deaths_data" to store the data of "new_deaths" in "new_data"
new_deaths_data = new_data["new_deaths"]
# draw a figure
plt.boxplot(new_deaths_data)
# put a title
plt.title('new deaths')
plt.show()

# ----------------------------------------------------------------------------------------------
# draw the change of new cases and new deaths worldwide over time.
# create a "world_dates" to store the data of "date" in "covid_data"
world_dates=covid_data["date"]
# create a "world_new_cases" to store the data of "new_data" in "covid_data"
world_new_cases=covid_data["new_cases"]
# use world_dates as x axis and world_new_cases as y axis and color of curve is blue
plt.plot (world_dates, world_new_cases,"b+",label='New Cases')
# set font size and adjust x-tick value
plt.xticks (world_dates.iloc[0:len (world_dates) :4],fontsize=4,rotation=-90)
# create a "world_new_deaths" to store the data of "new_deaths" in "covid_data"
world_new_deaths=covid_data["new_deaths"]
# use world_dates as x axis and world_new_deaths as y axis and color of curve is red
plt.plot (world_dates, world_new_deaths,"r+",label='New Deaths')
# set font size and adjust x-tick value
plt.xticks (world_dates.iloc[0:len (world_dates) :4],fontsize=4,rotation=-90)
# put a title
plt.title('world deaths and new cases over time')
# put a legend on upper left
plt.legend(loc='upper left')
plt.show()


# --------------------------------------------------------------------------------------------------------

# How have new cases and total cases developed over time in the UK?

# The appropriate Boolean array member is True if a value equals "United Kingdom," otherwise False. By providing covid data['UK'] with this Boolean array
covid_data['UK'] = (covid_data['location'] == 'United Kingdom')
# Filter out the rows where the 'UK' column equals True, and then print the 'total_cases','date' and 'new_cases' column of the filtered row.
UK_data=covid_data.loc[covid_data['UK'] == True,["date","new_cases","total_cases"]]
# create a "new_cases_UK_data" to store the data of "new_cases" in "covid_data"
new_cases_UK_data=UK_data["new_cases"]
# create a "total_cases_UK_data" to store the data of "total_cases" in "covid_data"
total_cases_UK_data=UK_data["total_cases"]
# create a "tUK_dates" to store the data of "date" in "covid_data"
UK_dates=UK_data["date"]
# use UK_dates as x axis and new_cases_UK_data as y axis and color of curve is blue
plt.plot (UK_dates,new_cases_UK_data,'b+',label='New Cases')
# set font size and adjust x-tick value
plt.xticks (UK_dates.iloc[0:len (UK_dates) :4],fontsize=6,rotation=-90)
# use UK_dates as x axis and total_cases_UK_data as y axis and color of curve is red
plt.plot (UK_dates,total_cases_UK_data,'r+',label='Total Cases')
# set font size and adjust x-tick value
plt.xticks (UK_dates.iloc[0:len (UK_dates) :4],fontsize=6,rotation=-90)
# put a title
plt.title('the tend of new cases and total cases in UK')
# put a legend on upper left
plt.legend(loc='upper left')
plt.show()
