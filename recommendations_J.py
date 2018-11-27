#utilizes rating prediction matrix from text file in order to actually recommend movies

#first we will load in our predicted rating matrix 
ratings = numpy.loadtxt("C:\\CMSC471-Python\\predictions_mat.txt", delimiter=",")

#then we will load our reference arrays into their respective variables
user_ids = numpy.loadtxt("C:\\CMSC471-Python\\user_ids_arr.txt", delimiter=",")
movie_ids = numpy.loadtxt("C:\\CMSC471-Python\\movie_ids_arr.txt", delimiter=",")
movie_titles = numpy.loadtxt("C:\\CMSC471-Python\\movie_titles_arr.txt", dtype = numpy.str, delimiter="@")
#NOTE: some of the items in movie_titles have foreign letters in their strings, and as such may not print properly
#if you attempt to print a movie_title and get an unexpected error on the print statement, this should be the first thing you check...

