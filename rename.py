import os
import re
def rename_list():
    #(1)get file names from a folder
    file_list = os.listdir(r"D:\Python3\test")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"D:\Python3\test")
    #(2)for each file ,rename filename
    for finame in file_list:
        os.rename(finame,re.sub('[0123456789]','',finame))
    file_list = os.listdir(r"D:\Python3\test")
    print(file_list)
rename_list()
