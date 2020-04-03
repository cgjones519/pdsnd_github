import time
import pandas as pd
import numpy as np

city_data = { "chicago": "chicago.csv", "new york city": "new_york_city.csv", "washington": "washington.csv" }
print("\nHello! Let\'s explore some US bikeshare data!")
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    filters = []
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:   
        city = str(input("\nWhat city would you like to analyze data for: Chicago, New York City or Washington? ", ))
        try:
            if city.strip().lower() not in city_data.keys():
                print("\nSorry, {} is not a valid city. Please type again by entering either Chicago, New York City or Washington".format(city)) #                 
            else:    
                print("\nYou have selected {}.".format(city.title()))
                filters.append(city.strip().lower())   
                break  
        except (ValueError, TypeError, KeyboardInterrupt):
            print()
    # TO DO: get user input for month (all, january, february, ... , june)                
    while True:                
        month = str(input("\nWhat month would you like to analyze data for: January, February, March, April, May, June or All? ", ))           
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        try:
            if month.strip().lower() not in months:           
                print("\nSorry, {} is not a valid month selection. Please try again by entering January, February, March, April, May or June or All.".format(month))  
            else:
                print("\nYou have selected {}.".format(month.title()))
                filters.append(month.strip().lower())
                break    
        except (ValueError, TypeError, KeyboardInterrupt):    
            print()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)                
    while True:
        day = str(input("\nWhat day of the week would you like to analyze data for: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All? ", ))
        day_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'] 
        try:       
            if day.strip().lower() not in day_of_week:
                print("\nSorry, {} is not a valid day of the week selection. Please type again by entering either Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday or All.".format(day))     
            else: 
                print("\nYou have selected {}.".format(day.title()))
                filters.append(day.strip().lower())     
                break
        except (ValueError, TypeError, KeyboardInterrupt):
           print()
    city, month, day = filters
    print("\nNow analyzing data for...\n \nCity: {} \nMonth: {} \nDay of the Week: {}.".format(city.title(), month.title(), day.title()))
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by one of the following month and day of the week options:
        1) All months and All days of the week
        2) All months and a specific day of the week
        3) A specific month and All days of the week
        4) A specifc month and a specific day of the week
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(city_data[city], index_col=[0])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    
    df['Month Index'] = df['Start Time'].dt.month
    df['Month Title'] = df['Start Time'].dt.month_name()
    df['Day of Week Index'] = df['Start Time'].dt.dayofweek
    df['Day of Week Title'] = df['Start Time'].dt.weekday_name


   
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    day_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] 

   
    if month != 'all' and day == 'all':
        month = months.index(month) + 1
        df = df[df['Month Index'] == month] 
     
        
    if day != 'all' and month == 'all': 
        day = day_of_week.index(day)
        df = df[df['Day of Week Index'] == day]
 
        
    if month != 'all' and day != 'all':  
        month = months.index(month) + 1
        day = day_of_week.index(day)
        df = df[(df['Month Index'] == month) & (df['Day of Week Index'] == day)]
   
    return df   

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month 
    common_month = df['Month Title'].mode()[0] 
    print("\nThe most common month is {}, for the most frequent times of travel.".format(common_month))

    # TO DO: display the most common day of week
    common_dow = df['Day of Week Title'].mode()[0]
    print("\nThe most common day of the week is {}, for the most frequent times of travel.".format(common_dow))
                                        
    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour                                   
    common_hour = df['Hour'].mode()[0]
    print("\nThe most common hour is {}:00, for the most frequent times of travel.".format(common_hour))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("\n{} is the most common start station.".format(common_start_station))
    

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("\n{} is the most common end station.".format(common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    freq_start_stop = (df['Start Station'] + df['End Station']).mode()[0] 
    print("\n{} and {} is the most frequent route combination of all start and end stations.".format(common_start_station, common_end_station))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_total = df['Trip Duration'].sum()
    print("\nThe total travel time for all trips was: {}".format(travel_total))

    # TO DO: display mean travel time
    travel_mean = df['Trip Duration'].mean()
    print("\nThe mean travel time for all trips was: {}".format(travel_mean))   

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
                                        
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nThe counts of user types are as follows:\n\n{}".format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns: 
        gender_count = df['Gender'].value_counts()
        print("\nThe counts of gender are as follows:\n\n{}".format(gender_count))
    else:
        print("\nThere is no available data for gender")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_dob = df['Birth Year'].min().astype('int64')
        print("\nThe earliest reported year of birth is {}.".format(earliest_dob))
        recent_dob = df['Birth Year'].max().astype('int64')
        print("\nThe most recent year of birth is {}.".format(recent_dob))
        common_dob = df['Birth Year'].mode().astype('int64')[0]
        print("\nThe most common year of birth is {}.".format(common_dob))
    else: 
        print("There is no available data for year of birth")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter Yes or No.\n')
        if restart.strip().lower() != 'yes':
            break


if __name__ == "__main__":
    main()