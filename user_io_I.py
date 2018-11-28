import os
import numpy

compareList = numpy.loadtxt("/Users/roboriot/OneDrive/UMBC/CLASSES/Junior_FirstSemester/CMSC471/movie_ids_arr.txt", delimiter=",")

newUser = [0] * len(compareList)
pos = 0
rating = 0

while pos!=-1 and rating != -1:

    pos = int(input("Which movie would you like to rate (1-9,000). (type -1 to exit): "))

    while(pos < -1 or pos > 9000):
        print("Incorrect input: please enter valid movie number:")
        pos = int(input("Which movie would you like to rate (1-9,000). (type -1 to exit): "))

    if(pos!= -1):
        rating = float(input("Rate this film: (.5-5.0)"))

        while(rating < .5 or rating > 5 ):
            print("Incorrect input, please enter valid rating:")
            rating = float(input("Rate this film: (.5-5.0)"))

        newUser[pos] = rating


#print(newUser)
numpy.savetxt("/Users/roboriot/OneDrive/UMBC/CLASSES/Junior_FirstSemester/CMSC471/newUser.txt", newUser, fmt='%1.1f', delimiter=",", newline="\n")
