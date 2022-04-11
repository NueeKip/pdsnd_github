### Created on 11th April 2022

## Explore-US-Bikeshare-Data Analysis
This is a project facilitated by Udacity it contains data, which is a bike share system provider for many cities in the United States. The data files for all three cities contain columns and data to work on

## Description
This project contains the python script is written for Udacity's Data Analyst Nanodegree and is used to explore data related to bike share systems for Chicago, New York City, and Washington. It imports data from csv files and compute descriptive statistics from the data. It also takes in users' raw input to create an interactive experience in the terminal to present these statistics.

## How to run the script
You can run the script using a Python integrated development environment (IDE) such as Spyder. To install Spyder, you will need to [download the Anaconda installer](https://www.anaconda.com/download/). This script is written in Python 3, so you will need the Python 3.x version of the installer. After downloading and installing Anaconda, you will find the Spyder IDE by opening Anaconda Navigator.
### Dataset description (Columns)
Start Time
End Time
Trip Duration (in seconds)
Start Station
End Station
User Type (Subscriber or Customer)
The Chicago and New York City files also contain the following two columns:

Gender
Birth Year
## Files used
Python Script to Explore US Bikeshare Data <br>
./Bikeshare.py
###other required files (not in project)
new_york_city.csv <br>
chicago.csv <br>
washington.csv <br>

## Future scopes
In the future, more functions that compute statistics will be added to answer more questions about the data. The possibilities of improving the interactive experience (e.g turning this script into a web app) will also be explored.

## Credits and References
Resources referred to complete this project
Use parse_dates to recognize datetime columns:
https://stackoverflow.com/questions/21269399/datetime-dtypes-in-pandas-read-csv
https://stackoverflow.com/questions/17465045/can-pandas-automatically-recognize-dates
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
<br>
Assess datetime series:
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.dt.html
https://stackoverflow.com/questions/29366572/pandas-how-to-filter-most-frequent-datetime-objects
<br>
Filter date:
https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates
<br>
Check validity of date:
https://stackoverflow.com/questions/9987818/in-python-how-to-check-if-a-date-is-valid/9987935
<br>
Add a day to a date:
https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-dataframe-in-pandas-python
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.str.cat.html#pandas.Series.str.cat
<br>
Installing IPython
If you already have Python installed and are familiar with installing packages, you can get IPython with pip:
>pip install ipython

### Other pandas and numpy functions:

Lessons in the Introduction to Data Analysis section of Udacity's Data Aanalyst Nanodegree (DAND)


