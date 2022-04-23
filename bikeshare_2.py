import time
import pandas as pd
import numpy as np

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('what city do you want to analyze: ').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('Enter a valid city')
        


    # get user input for month (all, january, february, ... , june)
    month_data = {'all':0, 'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}
    while True:
        month = input('which month?: ').lower()
        if month in month_data.keys():
            break
        else:
            print('Enter a valid month')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    week_data = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    while True:
        day = input('which day?: ').lower()
        if day in week_data:
            break
        else:
            print('Enter a valid day')


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
    # loading data
    df = pd.read_csv(CITY_DATA[city])

    # converting Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
                                  
    # extracting month, day and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    #filter by month if applicable
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
                  
                                                     

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month: {}' . format(common_month))
    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week: {}'.format(common_day_of_week))
    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('The most common start hour: {}'.format(common_start_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station= df['Start Station'].mode()[0]
    print('The most common start station: {}'.format(common_start_station))
    # TO DO: display most commonly used end station
    common_end_station= df['End Station'].mode()[0]
    print('The most common end station: {}'.format(common_end_station))
    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'])
    frequent_combination = df['Start To End'].mode()[0]
    print('most frequent combination of start to end station: {}'.format(frequent_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time:{}'.format(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean())
    print('mean travel time: {}'.format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('User Type: {}'.format(user_type))
         
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('gender : {}'.format(gender))
    except:
        print('There is no data for this city')  
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = int(df['Birth Year'].min())
        print('earliest birth year : {}'.format(earliest_birth_year))
    
        most_recent = int(df['Birth Year'].max())
        print('most recent year : {}'.format(most_recent))
    
        most_common = int(df['Birth Year'].mode()[0])
        print('most commom birth year: {}'.format(most_common))
    except:
        print('There is no data for this city')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    #To ask the user if he wants to view 5 rows of the data
    print('\nRaw data is available to see...\n')
    display_data = input('Would you like to display 5 rows of data?. Enter yes or no: ').lower()
    start_loc = 0
    while display_data == 'yes':
            print(df.iloc[start_loc:start_loc + 5])
            start_loc =+ 5
            display_data = input('Do you wish to continue?').lower()
    return display_data(df)
                               
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
