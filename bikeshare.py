import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

monthdata = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

daydata = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs




    while True:
      city = input("\n choose one of folowing cities (new york city , washington or chicago) that you want to analyze\n")
      if city.lower() not in CITY_DATA[city.lower()]:
        print("it's wrong ,Please try again to enter one of folowing cities new york city , washington or chicago\n")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\n Enter the name of the month that you want to analyze (choose 'all' or from january to june \n")
      if month not in monthdata:
        print("it is wrong ,Please enter either 'all' or choose one of the months from january to june \n")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\n Enter the name of the day that you want to analyze (choose 'all' or from monday to sunday \n")
      if day not in daydata:
        print("it's wrong ,Please enter either 'all' or choose one of the Days from monday to sunday \n")
        continue
      else:
        break

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
    df = pd.read_csv(CITY_DATA[city.lower()])

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

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


       # TO DO: display the most common month

    common_month = df['month'].mode()[0]
    print('The Most Common Month:', common_month)


    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('The Most Common day:', common_day)



        # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The Most Common Hour:', common_hour)



    print("\nThis took %s Sec." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

 # TO DO: display most commonly used start station

    commonStartStation = df['Start Station'].mode()[0]
    print('the most Start Station:\t', commonStartStation)


    # TO DO: display most commonly used end station

    commonEndStation = df['End Station'].mode()[0]
    print('the most end Station:\t', commonEndStation)


    # TO DO: display most frequent combination of start station and end station trip

    groupField=df.groupby(['Start Station','End Station'])

    frequentCombination = groupField.size().sort_values(ascending=False).head(1)
    print('The Most Commonly combination of Start Station and End Station trip:\t', frequentCombination)

    print("\nThis took %s Sec." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")


    # TO DO: display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Min")


    print("\nThis took %s Sec." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)


    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s Sec." % (time.time() - start_time))
    print('-'*40)

def displayRawData(df):

    print(df.head())
    next = 0
    while True:
        DisplYRawData = input('\n if you would like to see the first 5 row of data row?\n \tEnter yes or no\t ')
        if DisplYRawData.lower() == 'yes':
            print(df.iloc[next:next+5])
            next = next + 5
        elif DisplYRawData.lower() == 'no':
            break
        else:
            print('it is wrong answer or there is no avalible data to view  ')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            DisplyRawData = input('\n if you would like to see the first 5 row of data row?\n \tEnter yes or no\t ')
            if DisplyRawData.lower() != 'yes' :
                break
            displayRawData(df)
            break



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
