#Reading in data from data set
#userID's and movieID's will be moved into a dictionary matching them to indices which will be used for the matrix

import os
import numpy
from sklearn.preprocessing import normalize


filepath = "C:\\CMSC471-Python\\ml-latest-small\\movies.csv"
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


filepath2 = "C:\\CMSC471-Python\\ml-latest-small\\ratings.csv"
file2 = open(filepath2, "rt", encoding="utf8")
user_ids = []

i=0
for line in file2:
	if (i == 0):
		#will be skipping the first line since it just holds the column labels
		i=i+1
	elif line.split(',')[0] not in user_ids:
		user_ids.append(line.split(',')[0])


rows = len(user_ids)
cols = len(movie_ids)


a = numpy.zeros(shape=(rows,cols))

file2 = open(filepath2, "rt", encoding="utf8")

i=0
for line in file2:
	if(i == 0):
		#will be skipping the first line since it just holds the column labels
		i=i+1
	#elif (user_ids.index(line.split(',')[0]) < 100): THIS LINE WAS FOR WHEN WE WERE USING THE LARGE SET AND LIMITING THE NUMBER OF USERS
	else:
		linesplit = line.split(',')
		
		#first we find the index of the user id in the user_ids array
		curr_user = user_ids.index(linesplit[0])
		#then we find the index of the movie id in the movie_ids array
		curr_movie = movie_ids.index(linesplit[1])
		
		a[curr_user, curr_movie] = linesplit[2]

#for x in range(8500):
#	if(a[3,x] != -1):
#		print("User_ID: ", user_ids[3], " -- Movie_ID: ", movie_ids[x], " -- Rating: ", a[3,x])

numpy.savetxt("C:\\CMSC471-Python\\user_item_mat.txt", a, fmt='%1.1f', delimiter=",", newline="\n")
numpy.save("C:\\CMSC471-Python\\user_item_mat.npy", a)

	
normed_matrix = normalize(a, axis=1, norm="l1")

print ("Original matrix:")
for i in range(10):
	print ("\nLine ", i, ": ", end=" ")
	for j in range(10):
		print (a.item((i, j)), end=" ")

print ("Normalized matrix:")
for i in range(10):
	print ("\nLine ", i, ": ", end=" ")
	for j in range(10):
		print (normed_matrix.item((i, j)), end=" ") 



