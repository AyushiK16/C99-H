import os
import shutil
import time

folderPath = input('Enter the folder path: ')
listOfFiles = os.listdir(folderPath)

secondsInDay = 60*60*24
seconds_30 = secondsInDay*30
currentTime = time.time()


if os.path.exists(folderPath):
    os.walk(folderPath)
    for root,folders,files in os.walk(folderPath):
        ctime = os.stat(folderPath).st_ctime
        if ctime <currentTime - seconds_30:
            shutil.rmtree(folderPath)
    
        else:
            for file in listOfFiles:
                ctime = os.stat(folderPath + '/' + file).st_ctime
                print(ctime, currentTime - seconds_30)

                if ctime < currentTime - seconds_30:
                    #print(ctime, seconds_30)
                    #os.remove(folderPath + '/' + file)
                    print(folderPath + '/' + file  + ' has been removed.')
                else:
                    print(folderPath + '/' + file  + ' is still applicable.')


''' OLD CODE
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
'''


