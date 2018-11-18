#utilizing the newly made user-item matrix

import os
import numpy

data = numpy.loadtxt("/Users/Harrison Mann/Documents/CMSC_471_Project_Code/user_item_mat.txt", delimiter=",")

#data is now our user-item matrix

user_ids = numpy.loadtxt("/Users/Harrison Mann/Documents/CMSC_471_Project_Code/user_ids_arr.txt", delimiter=",")
movie_ids = numpy.loadtxt("/Users/Harrison Mann/Documents/CMSC_471_Project_Code/movie_ids_arr.txt", delimiter=",")


#this file is mostly useless, was just using it to mess around with reading back in the data and ensuring proper formats
