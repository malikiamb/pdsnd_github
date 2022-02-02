import time
import pandas as pd
import numpy as np
import json
import datetime
import time
import calendar
#import math

#City_Data stores data csv's
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#List of Cities
CITIES = ['chicago', 'new york city', 'washington']

#List of Months
MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

#List of Days
DAYS = ['all', 'monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data together!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle     invalid inputs

    city = input("Choose a city (Chicago, New york city , Washington\n\n) :").lower()
    while city not in CITIES:
        print("Oops, Please enter a valid City from the list")
        city = input("Choose a city (Chicago, New york city , Washington\n\n) :").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Choose a month (All, January, February, March, April, May, June: ").lower()
    while month not in MONTHS:
        print("Oops, Please enter a valid month")
        month = input("Choose a month (All, January, February, March, April, May, June:").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Choose a day (All, Monday through Sunday\n\n :").lower()
    while day not in DAYS:
        print("Oops, Please enter a valid day")
        day = input("Choose a day (All or Monday through Sunday\n\n :").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load dat into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['start hour'] = df['Start Time'].dt.hour

    #filter for month to create new dataframe
    if month != 'all':
       months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month)
       df = df[df['month'] == month]

    #filter for day to create new dataframe
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is : {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('The most common day is : {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('The most common start hour is : {}'.format(df['start hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is : {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common end station is : {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip']=df['Start Station']+","+df['End Station']
    print('The most common trip is :{}'.format(df['trip'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time : ',(df['Trip Duration'].sum()).round())

    # TO DO: display mean travel time
    print('Average travel time : ',(df['Trip Duration'].mean()).round())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if 'Gender' in(df.columns):
        print(df['Gender'].value_counts())



    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in(df.columns):
        print('The earliest year of birth is : ',int(df['Birth Year'].min()))
        print('The most recent year of birth is : ',int(df['Birth Year'].max()))
        print('The most common year of birth is : ',int(df['Birth Year'].mode()[0]))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Ask user if they would like to see the unflitered data for the city they chose"""
    i = 0
    answer = input("Would you like to display the first 5 rows of data? (yes/no) :").lower()
    pd.set_option('display.max_columns',None)

    while True:
        if answer == 'no':
            break
        print(df[i:i+5])
        answer = input("Would you like to display the next 5 rows of data? (yes/no) :").lower()


        i += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
