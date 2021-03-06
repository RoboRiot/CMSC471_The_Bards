# This loads data from a save file in the ".npy" format

import os
import numpy


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
a = numpy.ones(shape=(rows,cols))
a = numpy.multiply(a, -1)



a = numpy.load("C:\\CMSC471-Python\\user_item_mat.npy")

for x in range(8500):
	if(a[3,x] != -1):
		print("User_ID: ", user_ids[3], " -- Movie_ID: ", movie_ids[x], " -- Rating: ", a[3,x])


