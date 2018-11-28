#utilizes rating prediction matrix from text file in order to actually recommend movies

import numpy

#first we will load in our predicted rating matrix 
ratings = numpy.loadtxt("/Users/Harrison Mann/Documents/CMSC_471_Project_Code/predictions_mat.txt", delimiter=",")

#then we will load our reference arrays into their respective variables
user_ids = numpy.loadtxt("/Users/Harrison Mann/Documents/CMSC_471_Project_Code/user_ids_arr.txt", delimiter=",")
movie_ids = numpy.loadtxt("/Users/Harrison Mann/Documents/CMSC_471_Project_Code/movie_ids_arr.txt", delimiter=",")
movie_titles = numpy.loadtxt("/Users/Harrison Mann/Documents/CMSC_471_Project_Code/movie_titles_arr.txt", dtype = numpy.str, delimiter="@")
#NOTE: some of the items in movie_titles have foreign letters in their strings, and as such may not print properly
#if you attempt to print a movie_title and get an unexpected error on the print statement, this should be the first thing you check...


row_count = numpy.size(ratings,0)
col_count = numpy.size(ratings,1)

sorted_ratings = ratings[row_count - 1] #should now hold the final row of the matrix
sorted_ids = movie_ids.copy() #should now hold the movie ids in original order

#insertion sort
#inefficient sorting algorithm but it will be easy to maintain the sorted_ids array while sorting the values into the sorted_ratings array
#goal here is to sort the predicted user ratings into descended order
#we also have to sort the movie_ids array in the same order so that we can determine what the ratings are for
for i in range(1, col_count):
	j = i-1
	next = sorted_ratings[i]
	next_id = sorted_ids[i]
	while(sorted_ratings[j] < next) and (j >= 0):
		sorted_ratings[j+1] = sorted_ratings[j]
		sorted_ids[j+1] = sorted_ids[j]
		j = j - 1
	sorted_ratings[j+1] = next
	sorted_ids[j+1] = next_id


print(sorted_ratings)	