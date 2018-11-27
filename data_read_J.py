#Reading in data from data set
#userID's, movieID's, and movie_titles will be moved into arrays and saved in text files for use in other files
#the sparse user-item matrix will be created here and saved into a text file for use in other files

import os
import numpy

filepath = "C:\\CMSC471-Python\\ml-latest-small\\movies.csv"

file = open(filepath, "rt", encoding="utf8")

movie_ids = []
movie_titles = []


#first we read in from the file that holds all the movies in the dataset
i = 0
for line in file:
	if (i == 0):
		#will be skipping the first line since it just holds the column labels
		i = i+1
	else:
		movie_ids.append(line.split(',')[0])
		if(line.split(',')[1][0] == '\"'):
			#some of the movie names start in quotes because they have a comma in the title (comma is supposed to be the list item separator)
			#this if-block will get those movie titles, and the else will get all other regular movie titles without a comma
			
			first_quote = line.index('\"')
			second_quote = line.index('\"', first_quote+1)
			
			movie_titles.append(line[first_quote + 1:second_quote])#substring of line between the two quotation marks
		else:	
			movie_titles.append(line.split(',')[1])
			

filepath2 = "C:\\CMSC471-Python\\ml-latest-small\\ratings.csv"

file2 = open(filepath2, "rt", encoding="utf8")

user_ids = []

#then we read in from the file that holds all the ratings in the data set
#this file is the only one that has all user_ids, so we read from this one and skip duplicate id's from when a user has rated several movies
i=0
for line in file2:
	if (i == 0):
		#will be skipping the first line since it just holds the column labels
		i=i+1
	elif line.split(',')[0] not in user_ids:
		user_ids.append(line.split(',')[0])


rows = len(user_ids)
cols = len(movie_ids)

#if we want all empty spaces in matrix to be -1, use these lines
#a = numpy.ones(shape=(rows,cols))
#a = numpy.multiply(a, -1)
#if we want all empty spaces in matrix to be 0, use this line
a = numpy.zeros(shape=(rows,cols))

i=0

#here we reopen the ratings file to allow us to loop through it again
file2 = open(filepath2, "rt", encoding="utf8")

#here we actually add all of the ratings into our matrix, leaving many empty spaces as the matrix is sparse
for line in file2:
	if(i == 0):
		#will be skipping the first line since it just holds the column labels
		i=i+1
	else:
		linesplit = line.split(',')
		
		#first we find the index of the user id in the user_ids array
		curr_user = user_ids.index(linesplit[0])
		#then we find the index of the movie id in the movie_ids array
		curr_movie = movie_ids.index(linesplit[1])
		
		a[curr_user, curr_movie] = linesplit[2]

#this for loop is just a basic test
#for x in range(8500):
#	if(a[3,x] != -1):
#		print("User_ID: ", user_ids[3], " -- Movie_ID: ", movie_ids[x], " -- Rating: ", a[3,x])


#here we save all of the arrays and the matrix into text files so that we can access them more quickly in other files
numpy.savetxt("C:\\CMSC471-Python\\user_item_mat.txt", a, fmt='%1.1f', delimiter=",", newline="\n")
numpy.savetxt("C:\\CMSC471-Python\\user_ids_arr.txt", user_ids, fmt='%s', delimiter=",", newline="\n")
numpy.savetxt("C:\\CMSC471-Python\\movie_ids_arr.txt", movie_ids, fmt='%s', delimiter=",", newline="\n")
#NOTE: movie titles will have a delimiter of '@' instead of ',' because some of the titles have a comma, we will read it in with the delimiter as '@'
numpy.savetxt("C:\\CMSC471-Python\\movie_titles_arr.txt", movie_titles, fmt='%s', delimiter="@", newline="\n")
	
	