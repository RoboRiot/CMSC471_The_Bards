CMSC471 -- The Bards -- 11/30/2018
Michael Unuigbe
Joseph Koffman
Igor Savchenko
Harrison Mann


Ensure that your machine is running Python 3.6 (Errors have occurred while testing in older versions)

File setup:
In order to run the movie recommendation engine, you will first need to ensure that your files are in the correct directory format to work together.  Create the following path from your C: drive:

C:/movie_recs/

All of the files submitted should be put into this folder, this includes:

1. read_data.py
2. get_ratings.py
3. svd.py
4. results.py
5. driver.py
6. Movie_List.txt
7. ml-latest-small (folder)
	a. links.csv
	b. movies.csv
	c. ratings.csv
	d. tags.csv

Now, run your command prompt in administrator mode.  Several python libraries will need to be installed before the system can be run.  Install these libraries with the following commands, run one after the other in the command prompt (run everything INSIDE the quotation marks):

1. "python -m pip install numpy"
2. "python -m pip install scikit-learn"
3. "python -m pip install scipy"

Once these commands have been successfully run, it's now time to run the program!

Inside your command prompt (admin mode no longer required):

1. Navigate to the directory containing the python files (C:/movie_recs/)
2. Print the contents of the directory to ensure that all six files and the folder "ml-latest-small" are present
3. Run the command "python driver.py"
	a. The program will begin to run here, but it will take a few moments before you are prompted further
4. Once the program asks you which movie you would like to rate, open up the file "Movie_List.txt"
	a. This file is a list of movies, numbered 1-9742
	b. In the command prompt, type in the number preceding the movie that you want to rate
5. Once you've selected a movie to rate, enter the rating you wish to give the movie
	a. the rating can be from 0.5 - 5.0 in increments of 0.5
6. Continue to repeat steps 4 and 5 until you are done rating movies, then type "-1" when prompted which movie to rate
7. Now the program will begin to run again, and after a few moments, a list of 15 movie recommendations will appear
8. To run the program again, simply repeat the steps of this list