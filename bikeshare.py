import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter the name of the city to analyze (Chicago, New York City or Washington): ').lower()
    
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Invalid city name. Please enter a valid city name (Chicago, New York City or Washington):').lower()
    
            
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter the month to analyze (January, February, March, April, May or June). Type "all" to apply no month filter: ').lower()

    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('Invalid month name. Please enter a valid month (January, February, March, April, May or June). Type "all" to apply no month filter: ').lower()
    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter the day of week to analyze (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday). Type "all" to apply no day filter: ').lower()

    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('Invalid day name. Please enter a valid day name (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday). Type "all" to apply no day     filter:').lower()

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
    
    # load data file into a dataframe
    df = pd.DataFrame(pd.read_csv(CITY_DATA[city]))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def raw_data(df):
    """
    Shows 5 rows of raw data until the user does not want to see more.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
        
    """
    
    # ask the user if wants to see 5 rows of raw data
    raw_data = input('\nDo you want to see 5 rows of raw data? (yes or no) ').lower()
    
    while raw_data not in ['yes', 'no']:
        raw_data = input('\nInvalid input. Please enter a valid input (yes or no):').lower()

    i = 0
    
    if raw_data == 'yes':
        while raw_data == 'yes':
            print('')
            print(df[i:(i+5)])
            i += 5
            raw_data = input('\nDo you want to see another 5 rows of raw data? (yes or no) ').lower()
            
            while raw_data not in ['yes', 'no']:
                raw_data = input('\nInvalid input. Please enter a valid input (yes or no):').lower()
    
    
    print('\nLet\'s see some statistics')
    print('-'*40)
            


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = int(df['month'].mode()[0])
    print('The most common month is: {}'.format(most_common_month))
    

    # TO DO: display the most common day of week
    most_common_weekday = df['day_of_week'].mode()[0]
    print('The most common day of week is: {}'.format(most_common_weekday))


    # TO DO: display the most common start hour
    most_common_start_hour = int(df['Start Time'].dt.hour.mode()[0])
    print('The most common start hour is: {}'.format(most_common_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: {}'.format(most_common_start_station))


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common end station is: {}'.format(most_common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    most_common_station_combination = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('The most common combination of start and end station is: {}'.format(most_common_station_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The the total travel time is: {} seconds'.format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The the mean travel time is: {} seconds'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types: ')
    print(user_types)
    print('')
    
    
    # TO DO: Display counts of gender
    try:
        user_genders = df['Gender'].value_counts()
        print('User genders: ')
        print(user_genders)
        print('')
    except:
        print('There is no gender information for this city.')
        print('')
    

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        user_min_birth_year = int(df['Birth Year'].min())
        user_max_birth_year = int(df['Birth Year'].max())
        user_mode_birth_year = int(df['Birth Year'].mode()[0])
        print('The earliest year of birth is: {}'.format(user_min_birth_year))
        print('The most recent year of birth is: {}'.format(user_max_birth_year))
        print('The most common year of birth is: {}'.format(user_mode_birth_year))
        print('')
    except:
        print('There is no year of birth information for this city.')
        print('')

        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
