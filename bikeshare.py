import os
import sys
import time
import pandas as pd
import datetime
from IPython.display import display

# City dictionary with key: name and value: file directory
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

# Terminal controls(i.e. center prompts)
width = os.get_terminal_size().columns

# Function for entry greeting


def greeting():
    currentTime = datetime.datetime.now()
    currentTime.hour
    if currentTime.hour < 12:
        print('Good morning there !'.center(width))
    elif 12 <= currentTime.hour < 18:
        print('Good afternoon there !.'.center(width))
    else:
        print('Good evening there!'.center(width))


# Function to display all data (requires IPython module).
def RawData():
    try:
        pd.options.display.max_columns = None
        print('\nData for Chicago\n')
        chicago = pd.read_csv(CITY_DATA["chicago"])
        display(chicago)
        print('\nData for New York\n')
        new_york = pd.read_csv(CITY_DATA["chicago"])
        display(new_york)
        print('\nData for washington\n')
        washington = pd.read_csv(CITY_DATA["washington"])
        display(washington)
    except ModuleNotFoundError:
        print('Sorry, The module IPython is required to display data')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    """
    # get user input for city (chicago, new york city, washington).
    city = input(
        "Please enter a city name you would like to get the stats (Chicago, New York City, or Washington): ".center(width)).lower()
    while city not in ['chicago', 'new york city', 'washington']:
        print("Sorry, invalid input.".center(width))
        city = input(
            "Please enter a city name you would like to get the stats (Chicago, New York City, or Washington): ".center(width)).lower()

    # get user input for month (all, january, february, ... , june)
    month = input(
        "Please enter a month (January, February, March, April, May, June, or enter 'all'): ".center(width)).lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print("Sorry, invalid input.".center(width))
        month = input(
            "Please enter a month (January, February, March, April, May, June, or enter 'all'): ".center(width)).lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(
        "Please enter a day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or enter 'all'): ".center(width)).lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        print("Sorry, invalid input.".center(width))
        day = input(
            "Please enter a day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or enter 'all'): ".center(width))

    print('-' * 50)
    return city, month, day

# Function to load data as per the user selection of city, month and day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city, (str) month, (str) day 
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load intended file into data frame
    df = pd.read_csv(CITY_DATA[city])
    # pd.set_option("display.max_columns", 6)

    # convert columns od Start Time and End Time into date format yyyy-mm-dd
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month from Start Time into new column called month
    df['month'] = df['Start Time'].dt.month
    # extract day from Start Time into new column called month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # create a day mapper that maps day to corresponding day int(1st day start on sunday)
    day_mapper = {
        'sunday': 1,
        'monday': 2,
        'tuesday': 3,
        'wednesday': 4,
        'thursday': 5,
        'friday': 6,
        'saturday': 7
    }

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day_mapper[day]]

    return df

# This function maps the day number to corresponding date 
def map_day_to_text(day):
    """
    Method to help map each day in int to a corresponding day in string
    :param
     day(int): input the int day of week
    :return:
     string:  correct day of week in string(Week starts on sunday)
    """
    day_mapper = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }
    return day_mapper[day]

# This function maps month to its month number
def map_month_to_text(month):
    """
    Method to help map each month in int to a corresponding month in string
    :param
     day(int): input the int month
    :return:
     string:  correct month in string(Month always ends at june)
    """
    month_mapper = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June'
    }
    return month_mapper[month]


# Function to display the start for time

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    # Display the most common month

    try:
        df["month"] = df['Start Time'].dt.month
        print("Most common month is: ",
              map_month_to_text(df["month"].mode()[0]))
    except:
        print("\nTime stats:\nNo data available for this month.")

    #  Display the most common day of week
    try:
        df["day_of_week"] = df['Start Time'].dt.day_name()
        print("Most common day is: ", map_day_to_text(
            df["day_of_week"].mode()[0]))
    except:
        print("\nTime stats:\nNo data available for this week.")

    # Display the most common start hour
    try:
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['hour'] = df['Start Time'].dt.hour
        common_hour = df['hour'].mode()[0]
        print('Most comon Start Hour:', common_hour)
    except:
        print("\nTime stats:\nNo data available for this hour.")

    print('-'*50)

# Function to display stats for the stations of bike pickup


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    # TO DO: display most commonly used start station

    try:
        Start_Station = df['Start Station'].value_counts().idxmax()
        print('Most Commonly used start station:', Start_Station)
    except:
        print('\n Station Error:\n Values not available for station')
    # TO DO: display most commonly used end station
    try:
        End_Station = df['End Station'].value_counts().idxmax()
        print('\nMost Commonly used end station:', End_Station)
    except:
        print('\n Station Error:\n Values not available for station')

    # TO DO: display most frequent combination of start station and end station trip
    try:
        Combination_Station = df.groupby(
            ['Start Station', 'End Station']).count()
        print('\nMost Commonly used combination of start station and end station trip:',
              Start_Station, " & ", End_Station)
    except:
        print('\n Station Error:\n Values not available for station')

    print('-'*50)

# Function to get the trip duration in seconds


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    try:
        total_time = df["Trip Duration"].sum()
        print("Total trip duration is ", total_time/3600)
    except:
        print('\n Duration Error: Duration time not captured\n')

    # Display mean travel time
    try:
        avarage_time = df["Trip Duration"].mean()
        print("Avarage of trip duration is ", avarage_time/3600)
    except:
        print('\n Duration Error: Duration time not captured\n')

    print('-'*50)


# Function to display yser stats
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # Display counts of gender
    if 'Gender' in df.columns:
        user_gender = df['Gender'].value_counts()
        print(user_gender)
    else:
        print("No gender data available")

        # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year_of_birth = int(df['Birth Year'].min())
        most_recent_year_of_birth = int(df['Birth Year'].max())
        most_common_year_of_birth = int(
            df['Birth Year'].value_counts().idxmax())
        print("The earliest year of birth is:", earliest_year_of_birth,
              ", most recent one is:", most_recent_year_of_birth,
              "and the most common one is: ", most_common_year_of_birth)
    else:
        print("No birth year data available")

    print('-' * 50)

# Function to display extra 5 lines od specific data


def display_raw_data(df):
    """Displays raw data as per user input."""

    i = 0
    answer = input(
        "Would you like to display 5 lines of raw data? Enter yes or no.\n").lower()
    pd.set_option("display.max_columns", None)

    while True:
        if answer == "no":
            break
        print(df[i:i+5])
        answer = input(
            "Would you like to display another 5 lines of raw data? Enter yes or no.\n".center(width)).lower()
        i += 5


# To execute all functions
def all_functions():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input(
            '\nWould you like to restart? Enter yes or no.\n'.center(width))
        if restart.lower() != 'yes':
            break


def main():

    greeting()
    response = input(

        'Let\'s explore the US bikeshare data and do some analysis, you ready?'.center(width) + 'Yes: Let\'s go on!'.center(width) + 'No: Let me see the raw data first!'.center(width) + 'Press any key + enter to exit!'.center(width)).lower()
    if response == 'yes':
        all_functions()

    elif(response == 'no'):
        RawData()
        restart_2 = input(
            '\nWould you like to continue to analysis results? Enter yes or no.\n'.center(width))
        if restart_2.lower() == 'yes':
            all_functions()
    else:
        exit()


if __name__ == "__main__":
    # To handle exit
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
