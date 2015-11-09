#!/usr/bin/python
import os
import argparse
def rename_files():
    parser=argparse.ArgumentParser()
    parser.add_argument('-fp','--folderpath',help="Specify path of folder to rename files")
    args=parser.parse_args()
    #Check for valid folderpath
    if args.folderpath :
        #Get files in particular folder
        file_list=os.listdir(args.folderpath)
        print(file_list)
        os.chdir(args.folderpath)
        if len(file_list) > 0:
            for file_name in file_list:
                #string fun translate removes second parameter ele from string
                new_name=file_name.translate(None,"0123456789")
                #Finally to rename files in folder os.rename
                os.rename(file_name,new_name)
        else:
            print("Folder is empty")
    else :
        print("Specify Folder Name in cmd")
        
rename_files()

#Exception Conditione
#1.renaming file that does not exist
#2.renaming a file name to name that already exist in folder.
