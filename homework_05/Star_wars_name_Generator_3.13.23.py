#By Maya Oniciuc

# Star Wars Name Generator Algorithm
# SWFirstName SWLastName, Title of Origin
# SW First Name: First 3 letters of first name + First 2 letters of last name
# SW Last Name: First 2 letters of favorite food + First 3 letters of a city you would like to live in
# Title: Last 3 letters of last name reversed + first half of the car you want to drive
# Origin: Last 2 letters of first name + slice of your favorite movie:
    # first index: random number from 0 to 3 inclusive
    # second index: random number from 5 to 7 inclusive
# Maon Sadon

import random


# collect information from user
print("Hello! Are you ready to find out your star wars name???")
first_name = input("What is your first name? ").replace(" ", "")
last_name = input("What is your last name? ").replace(" ", "")
fav_food = input("What is your favorite food? ").replace(" ", "")
city = input("What is a city you would like to live in? ").replace(" ", "")
fav_movie = input("What is your favorite movie? ").replace(" ", "")
car = input("What Car would you like to drive?? ").replace(" ", "")


# Firstname Lastname, Title of Origin

# process the strings

# sw_first_name = first_name[0:3] + last_name[0:2]
sw_first_name = first_name[0].upper() + first_name[1:3].lower() + last_name[0:2].lower()
# sw_last_name = fav_food[0:3] + city[0:4]
sw_last_name = fav_food[0].upper() + fav_food[1:2].lower() + city[0:4].lower()
# title = last_name[len(last_name)-1] + last_name[len(last_name)-2] + last_name[len(last_name)-3] + car[0:len(car)//2]
title = last_name[len(last_name)-1].upper() + last_name[len(last_name)-2].lower() + last_name[len(last_name)-3].lower() + car[0:len(car)//2].lower()
# origin = first_name[len(first_name)-2:] +  fav_movie[:random.randint(0,3)] + fav_movie[:random.randint(5,7)]
origin = first_name[len(first_name)-2:len(first_name)-1].upper() + first_name[len(first_name)-1:].lower() +  fav_movie[:random.randint(0,3)].lower() + fav_movie[:random.randint(5,7)].lower()



# print the star wars name
print("Your Star Wars name is: " + sw_first_name + " " + sw_last_name + " " + title + "," + " of " + origin)
