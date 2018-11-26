#utilizing the newly made user-item matrix to create a rating prediction matrix
#new matrix will be saved as text file for quick use in other files

import os
import numpy
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import svds, eigs

#we will first load our user-item matrix into data
data = numpy.loadtxt("/Users/Harrison Mann/Documents/CMSC_471_Project_Code/user_item_mat.txt", delimiter=",")


#convert the data to a scipy sparse matrix
scipy_data = csc_matrix(data)

#perform scipy sparse svd on the matrix
#NOTE: we will need to determine a K parameter value
#To do this:
#1. Run our algorithm without a low K value on training set
#2. Then run on validation set and compute Root Mean Square Error
#3. Repeats steps 1 and 2, increasing K, and find the K value that minimizes the Root Mean Square Error
#Remember: 1 <= K < MIN(matrix.rows, matrix.columns)

#Basically, a higher K value will overfit our data to our training set, so this is the key component of our recommendation engine
#For movies, lower rank matricies with 20 <= k <= 100 has been shown to be a good range for accurate predictions
U, S, Vt = svds(scipy_data, k=50)

#converts S from an list of values into a diagonal matrix
S = numpy.diag(S)

predicted_ratings = numpy.dot(numpy.dot(U, S), Vt)

#save the predicted_ratings matrix into a txt file so it can be utilized by other files
numpy.savetxt("/Users/Harrison Mann/Documents/CMSC_471_Project_Code/predictions_mat.txt", predicted_ratings, fmt='%1.3f', delimiter=",", newline="\n")