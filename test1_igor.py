#Reading in data from data set
#userID's and movieID's will be moved into a dictionary matching them to indices which will be used for the matrix

import os

filepath = "/Users/roboriot/OneDrive/UMBC/CLASSES/Junior_FirstSemester/CMSC471/ml-latest/movies.csv"

file = open(filepath, "rt", encoding="utf8")

movie_ids = []
movie_titles = []

i = 0
for line in file:
	if (i == 0):
		#will be skipping the first line since it just holds the column labels
		i = i+1
	else:
		movie_ids.append(line.split(',')[0])
		movie_titles.append(line.split(',')[1])


#print (movie_ids[34])
#print (movie_ids[112])
#print (len(movie_ids))


filepath2 = "/Users/roboriot/OneDrive/UMBC/CLASSES/Junior_FirstSemester/CMSC471/ml-latest/ratings.csv"

file2 = open(filepath, "rt", encoding="utf8")

user_ids = []

i=0
for line in file2:
	if (i == 0):
		#will be skipping the first line since it just holds the column labels
		i=i+1
	elif line.split(',')[0] not in user_ids:
		user_ids.append(line.split(',')[0])

#print (user_ids[0])
#print (user_ids[1])
#print (user_ids[4])
