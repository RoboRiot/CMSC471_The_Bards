
import os.path
import time


filepath1 = "C:\\Users\\Harrison Mann\\Documents\\CMSC_471_Project_Code\\movie_titles_arr.txt"
filepath2 = "C:\\Users\\Harrison Mann\\Documents\\CMSC_471_Project_Code\\newUser.txt"
filepath3 = "C:\\Users\\Harrison Mann\\Documents\\CMSC_471_Project_Code\\predictions_mat.txt"



#first we run data_read_H.py
import data_read_H

#at the very end of data_read_H, we create the document at filepath1
#so we want to wait until this document is created before running the next file
while not os.path.exists(filepath1):
	time.sleep(1)
	

#after the file is known to exist, we will wait 5 seconds to ensure it has been completed
time.sleep(5)

#then we run user_io.py
import user_io

#at the very end of user_io, we create the document at filepath2
#so we want to wait until this document is created before running the next file
while not os.path.exists(filepath2):
	time.sleep(1)
	

#after the file is known to exist, we will wait 5 seconds to ensure it has been completed
time.sleep(5)

#then we run run_svd.py
import run_svd

#at the very end of run_svd, we create the document at filepath3
#so we want to wait until this document is created before running the next file
while not os.path.exists(filepath3):
	time.sleep(1)
	

#after the file is known to exist, we will wait 5 seconds to ensure it has been completed
time.sleep(5)

#now we can safely run the last file which prints the recommendations
import recommendations
