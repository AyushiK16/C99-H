import os
import shutil
import time

folderPath = input('Enter the folder path: ')
listOfFiles = os.listdir(folderPath)

secondsInDay = 60*60*24
seconds_30 = secondsInDay*30


if os.path.exists(folderPath):
    for file in listOfFiles:
        ctime = os.stat(folderPath + '/' + file).st_ctime
        if ctime > seconds_30:
            print(ctime, seconds_30)
            #os.remove(folderPath + '/' + file)
            print(folderPath + '/' + file  + 'has been removed.')
        
        else:
            print(folderPath + '/' + file  + 'is still applicable.')



