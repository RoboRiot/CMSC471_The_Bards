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
new_user = numpy.loadtxt("/Users/Harrison Mann/Documents/CMSC_471_Project_Code/newUser.txt",delimiter="," )

row_count = numpy.size(ratings,0)
col_count = numpy.size(ratings,1)

sorted_ratings = ratings[row_count - 1] #should now hold the final row of the matrix, the predicted new user's ratings
sorted_ids = movie_ids.copy() #should now hold the movie ids in original order

#insertion sort
#inefficient sorting algorithm but it will be easy to maintain the sorted_ids array while sorting the values into the sorted_ratings array
#goal here is to sort the predicted user ratings into descended order
#we also have to sort the movie_ids array in the same order so that we can determine what each of the sorted ratings are in reference to
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


#print(sorted_ratings)	

#Now we will run through the sorted ratings list in descending order (highest to lowest).
#Each item that WASNT initially rated by the new user but has a high predicted rating will be printed out.
#This will continue until 15 movies have been recommended (printed out), then the loop will exit

rec_count = 0
print("-------------------- Recommendations --------------------\n")

for i in range(0, col_count):
	#find the id of the movie at index i in sorted_ratings
	id = sorted_ids[i]
	
	#then find the index of that movie_id in the id array pre-sorting
	initial_index = movie_ids.tolist().index(id)
	
	#if the user did not rate this movie
	if(new_user[initial_index] == 0):
		rec_count = rec_count + 1
		print(rec_count, "- ", movie_titles[initial_index], "\n")
		
		#if this was the 15th recommendation, break out of loop to finish
		if(rec_count == 15):
			break
			
	#THIS ELSE BLOCK IS ONLY FOR TESTING, JUST CURIOUS TO SEE HOW MANY OF THE INITIALLY RATED MOVIES ARE AT THE TOP OF THE LIST OF RECOMMENDATIONS		
	#else:
		#print(movie_titles[initial_index], "\n")
		
print("---------------------------------------------------------\n")

#this is basically just a garbage file that we create here after the recommendations are given
#this allows the driver to know when all other files are done being used, so it can delete them safely in order to allow the program to run again
numpy.savetxt("/Users/Harrison Mann/Documents/CMSC_471_Project_Code/completion_indicator.txt", sorted_ratings, fmt='%1.3f', delimiter=",", newline="\n")