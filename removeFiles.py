import os
import shutil
import time

folderPath = input('Enter the folder path: ')
listOfFiles = os.listdir(folderPath)

secondsInDay = 60*60*24
#seconds_30 = secondsInDay*30
seconds_30 = 30
currentTime = time.time()


if os.path.exists(folderPath):
    #os.walk(folderPath)
    for root,folders,files in os.walk(folderPath):
        ctime = os.stat(folderPath).st_ctime
        if ctime <currentTime - seconds_30:
            shutil.rmtree(folderPath)
    
        else:
            for file in files:
                ctime = os.stat(folderPath + '/' + file).st_ctime
                print(ctime, currentTime - seconds_30)

                if ctime < currentTime - seconds_30:
                    #print(ctime, seconds_30)
                    os.remove(folderPath + '/' + file)
                    print(folderPath + '/' + file  + ' has been removed.')
                else:
                    print(folderPath + '/' + file  + ' is still applicable.')

            for folder in folders:
                ctime = os.stat(folderPath + '/' + folder).st_ctime

                if ctime < currentTime - seconds_30:
                    #print(ctime, seconds_30)
                    shutil.rmtree(folderPath + '/' + folder)
                    print(folderPath + '/' + folder  + ' has been removed.')
                else:
                    print(folderPath + '/' + folder  + ' is still applicable.')



                #for folders





'''
os.walk(folderPath) - root, folders, files
for root,folders,files in os.walk(folderPath):
    - sep gives you all
    check time for root folder, 
        if true, delete the folder
    shutil.rmtree(folderPath) => to delete a folder

    else:
        - check the folders 
        - write the time condition for each folder
        then shutil.rmtree(folderPath)

        - check the files
        - check for the condition, then os.remove (for files)       

'''

