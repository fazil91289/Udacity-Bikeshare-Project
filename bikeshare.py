import pandas as pd
from datetime import datetime
from datetime import timedelta
import time
import datetime


city = ''
while city.lower() not in ['chicago', 'new york', 'washington']:
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or'
                     ' Washington?\n')
    if city.lower() == 'chicago':
        df = pd.read_csv('chicago.csv')
    elif city.lower() == 'new york':
        df = pd.read_csv('new_york_city.csv')
    elif city.lower() == 'washington':
        df = pd.read_csv('washington.csv')
    else:
        print('Sorry, I do not understand your input. Please input either '
                  'Chicago, New York, or Washington.')

time_period = ''
while time_period.lower() not in ['month', 'day', 'none']:
    time_period = input('\nWould you like to filter the data by month, day,'
                            ' or not at all? Type "none" for no time filter.\n')
    if time_period.lower() not in ['month', 'day', 'none']:
        print('Sorry, I do not understand your input.')


if time_period == 'month' or time_period == 'day':
    month_input = ''
    day_input = ''
    months_list = ['1','2','3','4','5','6']
    day_list = ['0','1','2','3','4','5','6']
    if time_period == 'month':
        while month_input.lower() not in months_list:
            month_input = input('Please enter month in numbers (1 to 6),'
                            '1 being January and 6 being June\n')
            if month_input.lower() not in months_list:
                print('Sorry, I do not understand your input. Please type in a '
                      'month between January and June')
    elif time_period == 'day':
        while month_input.lower() not in months_list:
            month_input = input('Please enter month in numbers (1 to 6),'
                            '1 being January and 6 being June\n')
            if month_input.lower() not in months_list:
                print('Sorry, I do not understand your input. Please type in a '
                      'month between January and June')
        while day_input.lower() not in day_list:
            day_input = input('Please enter day in numbers (0 to 6),'
                            '0 being Monday and 6 being Sunday\n')
            if day_input.lower() not in day_list:
                print('Sorry, I do not understand your input. Please type in a '
                      'month between January and June')
    elif time_period == 'none':
        pass








#Dropping NA values in the DataFrame

df.fillna("0", inplace = True)

#creating month column

df['month'] = pd.DatetimeIndex(df['Start Time']).month

#Creating weekday column

df['weekday'] = pd.DatetimeIndex(df['Start Time']).weekday

#Creating Hour column

df['hour'] = pd.DatetimeIndex(df['Start Time']).hour

#Creating duration_min Column

df['duration_min'] = pd.to_datetime(df['Trip Duration'], unit = 's')

#Creating delimiter column

df['delimiter'] = "To"

#Creating start_station_delimiter column

df['start_station_delimiter'] = df['Start Station'] + df['delimiter']

#Creating pop trip column

df['pop trip'] = df['start_station_delimiter'] + df['End Station']

#Creating age column


if city == 'washington':
    df['Birth Year'] = 2019
    df['age'] = df['Birth Year'] - 2019
    df['age'] = df['age'].abs()
elif city == 'chicago' or city == 'new york':
    df['Birth Year'] = df['Birth Year'].astype('int')
    df['age'] = df['Birth Year'] - 2019
    df['age'] = df['age'].abs()
    df.loc[:, 'age'].replace([2019], [0], inplace=True)


if time_period == 'month' or time_period == 'day':
    if month_input == '1':
        df = df[df['month']==1]
    elif month_input == '2':
        df = df[df['month']==2]
    elif month_input == '3':
        df = df[df['month']==3]
    elif month_input == '4':
        df = df[df['month']==4]
    elif month_input == '5':
        df = df[df['month']==5]
    elif month_input == '6':
        df = df[df['month']==6]
    elif month_input == '7':
        df = df[df['month']==7]
    else:
        pass
elif time_period == 'none':
    pass



if time_period == 'month' or time_period == 'day':
    if day_input == '0':
        df = df[df['weekday']==0]
    elif day_input == '1':
        df = df[df['weekday']==1]
    elif day_input == '2':
        df = df[df['weekday']==2]
    elif day_input == '3':
        df = df[df['weekday']==3]
    elif day_input == '4':
        df = df[df['weekday']==4]
    elif day_input == '5':
        df = df[df['weekday']==5]
    elif day_input == '6':
        df = df[df['weekday']==6]
    else:
        pass
elif time_period == 'none':
    pass


def popular_month(df):

    most_pop_month = int(df['month'].mode())
    to_check_month = str(most_pop_month)

    if most_pop_month == 1:
        print("Most popular month is January")
    elif most_pop_month == 2:
        print("Most popular month is February")
    elif most_pop_month == 3:
        print("Most popular month is March")
    elif most_pop_month == 4:
        print("Most popular month is April")
    elif most_pop_month == 5:
        print("Most popular month is May")
    elif most_pop_month == 6:
        print("Most popular month is June")
    elif most_pop_month == 7:
        print("Most popular month is July")
    else:
        print("I donno ask your Mom")



def popular_day(df):

    most_pop_weekday = int(df['weekday'].mode())
    #to_check_weekday = str(most_pop_weekday)
    if most_pop_weekday == 0:
        print("Most popular weekday is Monday")
    elif most_pop_weekday == 1:
        print("Most popular weekday is Tuesday")
    elif most_pop_weekday == 2:
        print("Most popular weekday is Wednesday")
    elif most_pop_weekday == 3:
        print("Most popular weekday is Thurday")
    elif most_pop_weekday == 4:
        print("Most popular weekday is Friday")
    elif most_pop_weekday == 5:
        print("Most popular weekday is Saturday")
    elif most_pop_weekday == 6:
        print("Most popular weekday is Sunday")
    else:
        print("I donno ask your Mom")


def popular_hour(df):


    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
    most_pop_hour = int(df['hour'].mode())

    if most_pop_hour == 0:
        print("Most popular hour is 12 AM")
    elif most_pop_hour == 1:
        print("Most popular hour is 1 AM")
    elif most_pop_hour == 2:
        print("Most popular hour is 2 AM")
    elif most_pop_hour == 3:
        print("Most popular hour is 3 AM")
    elif most_pop_hour == 4:
        print("Most popular hour is 4 AM")
    elif most_pop_hour == 5:
        print("Most popular hour is 5 AM")
    elif most_pop_hour == 6:
        print("Most popular hour is 6 AM")
    elif most_pop_hour == 7:
        print("Most popular hour is 7 AM")
    elif most_pop_hour == 8:
        print("Most popular hour is 8 AM")
    elif most_pop_hour == 9:
        print("Most popular hour is 9 AM")
    elif most_pop_hour == 10:
        print("Most popular hour is 10 AM")
    elif most_pop_hour == 11:
        print("Most popular hour is 11 AM")
    elif most_pop_hour == 12:
        print("Most popular hour is 12 PM")
    elif most_pop_hour == 13:
        print("Most popular hour is 1 PM")
    elif most_pop_hour == 14:
        print("Most popular hour is 2 PM")
    elif most_pop_hour == 15:
        print("Most popular hour is 3 PM")
    elif most_pop_hour == 16:
        print("Most popular hour is 4 PM")
    elif most_pop_hour == 17:
        print("Most popular hour is 5 PM")
    elif most_pop_hour == 18:
        print("Most popular hour is 6 PM")
    elif most_pop_hour == 19:
        print("Most popular hour is 7 PM")
    elif most_pop_hour == 20:
        print("Most popular hour is 8 PM")
    elif most_pop_hour == 21:
        print("Most popular hour is 9 PM")
    elif most_pop_hour == 22:
        print("Most popular hour is 10 PM")
    elif most_pop_hour == 23:
        print("Most popular hour is 11 PM")
    else:
        print("I donno ask your Mom")


def trip_duration(df):

    average_trip_duration = df['Trip Duration'].mean()
    average_trip_duration = int(average_trip_duration)
    average_trip_duration = datetime.timedelta(seconds=average_trip_duration)
    print('Average trip duration is :', average_trip_duration)
    total_trip_duration = df['Trip Duration'].sum()
    total_trip_duration = int(total_trip_duration)
    total_trip_duration_seconds = df['Trip Duration'].sum()
    total_trip_duration = datetime.timedelta(seconds=total_trip_duration)
    print('Total trip duration is :', total_trip_duration_seconds, 'seconds','i.e.', total_trip_duration, 'hours')


def popular_stations(df):
    most_popular_start_station = df['Start Station'].mode()
    most_popular_start_station = str(most_popular_start_station)
    most_popular_start_station = most_popular_start_station[1 : : ]
    print('Most popular start station is : ' , most_popular_start_station)
    most_popular_end_station = df['End Station'].mode()
    most_popular_end_station = str(most_popular_end_station)
    most_popular_end_station = most_popular_end_station[1 : : ]
    print('Most popular end station is : ' , most_popular_end_station)


def popular_trip(df):
    most_pop_trip = df['pop trip'].mode()
    most_pop_trip = str(most_pop_trip)
    #removes the 0 at the beggining
    most_pop_trip = most_pop_trip[1 : : ]
    #splits from to
    most_pop_trip = most_pop_trip.split("To")
    #joins the strings
    most_pop_trip = str(([most_pop_trip[0], 'to', most_pop_trip[-1] ] ))
    #replacing quotes
    most_pop_trip = most_pop_trip.replace(',', '')
    most_pop_trip = most_pop_trip.replace("'", '')
    print('The most popular trip is : ', most_pop_trip)



def users(df):
    count_of_subscribers = df.loc[df['User Type'] == 'Subscriber', 'User Type'].count()
    count_of_customers = df.loc[df['User Type'] == 'Customer', 'User Type'].count()
    print('Total Number of Subscribers are :', count_of_subscribers)
    print('Total Number of Customers are :', count_of_customers)


def gender(df):
    count_of_female = df.loc[df['Gender'] == 'Female', 'Gender'].count()
    count_of_male = df.loc[df['Gender'] == 'Male', 'Gender'].count()
    print('Total Number of Females are :', count_of_female)
    print('Total Number of Males are :', count_of_male)


def birth_years(df):
    youngest = df[df['age'] > 0]['age'].min(axis=0)
    old_year = df[df['Birth Year'] > 0]['Birth Year'].min(axis=0)
    young_year = df['Birth Year'].max()
    oldest = df['age'].max()
    most_pop_birth_year = df[df['Birth Year'] > 0]['Birth Year'].mode()
    most_pop_birth_year = str(most_pop_birth_year)
    most_pop_birth_year = most_pop_birth_year[1 : : ]
    print("The Youngest person is", youngest, "years old, born in", young_year)
    print("The oldest person is", oldest, "years old, born in", old_year)
    print("The most popular birth year is :", most_pop_birth_year.lstrip())


def display_5lines():

    if city == 'chicago':
        df2 = pd.read_csv('chicago.csv')
        print(df2.head())
    elif city == 'washington':
        df2 = pd.read_csv('chicago.csv')
        print(df2.head())
    elif city == 'new york':
        df2 = pd.read_csv('chicago.csv')
        print(df2.head())



popular_month(df)
popular_day(df)
popular_hour(df)
trip_duration(df)
popular_stations(df)
popular_trip(df)
users(df)
if city == 'chicago' or city == 'new york':
    # What are the counts of gender?
    gender(df)
    # What are the earliest (i.e. oldest user), most recent (i.e. youngest
    # user), and most popular birth years?
    birth_years(df)


validation = input('Do you want to see 5 lines of individual data?')

if validation.lower() == 'yes':
    display_5lines()
elif validation.lower() == 'no':
    pass
else:
    print("I don't Understand, please type yes or no")
