#utilizing the newly made user-item matrix to create a rating prediction matrix
#new matrix will be saved as text file for quick use in other files

import os
import numpy
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import svds, eigs

#we will first load our user-item matrix into data
data = numpy.loadtxt("/Users/Harrison Mann/Documents/CMSC_471_Project_Code/user_item_mat.txt", delimiter=",")
newUser = numpy.loadtxt("/Users/Harrison Mann/Documents/CMSC_471_Project_Code/newUser.txt",delimiter="," )


data = numpy.vstack([data, newUser])


#convert the data to a scipy sparse matrix
scipy_data = csc_matrix(data)

#perform scipy sparse svd on the matrix
#NOTE: we will need to determine a K parameter value
#Remember: 1 <= K < MIN(matrix.rows, matrix.columns)
#Professor Mittal recommended that we use 10-20 for k instead of worrying about optimizing the rank
#Basically, a higher K value will overfit our data to our training set, so this is the key component of our recommendation engine
U, S, Vt = svds(scipy_data, k=15)

#converts S from an list of values into a diagonal matrix
S = numpy.diag(S)

predicted_ratings = numpy.dot(numpy.dot(U, S), Vt)

#save the predicted_ratings matrix into a txt file so it can be utilized by other files
numpy.savetxt("/Users/Harrison Mann/Documents/CMSC_471_Project_Code/predictions_mat.txt", predicted_ratings, fmt='%1.3f', delimiter=",", newline="\n")