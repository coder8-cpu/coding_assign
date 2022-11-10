The following files responsible for ,
featch_data.py -- > its call the api endpoint and featch the data and store it to user_data.csv

main.py -- > is responsible for perform a sorting technique 
and sort the user_data.csv data as order username and name
and save it to sorted_user_data

it is also responsible for return the user data when input user id or username from the sorted_user_data.csv

sorted_user_data.csv -- > where all the sorted data are stored

user_data.csv -- > where all the featched data store and return as call 

-- for featch_data.py -- 

first i make a get request to AN API in an interval of 1 sec
then i open the user_data.csv in write mode and write the featched data
to user_data.csv

-- for main.py --
here i opened the user_data.csv in read mode
then i take the date of every user data and rearrange the dates in assending to decending order and save it to a varible

then i compare the list of dates with my user_sorted data
whem its matched its write the line in a new file named sorted_user_data in a manner such that the dates are in assending to decending order. 

-- for search_data.py -- 
here i take a input as username and open the sorted_csv file and perform a 
for loop to determine wheather it is match the username with any line or not
if yes then its return the line from sorted_user_data.csv

Thank You
Debashish Sarkar
