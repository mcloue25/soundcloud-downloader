import glob, os.path, shutil


def getListOfFiles(dirName):
    # The path to the folder where you want the files to be stored
    newLoaction = 'C:/Users/Eoin/Documents/Soulseek Downloads/Tracks Folder/Runway Techno'
    
    listOfFiles = os.listdir(dirName)
    # Iterate over all the entries
    for entry in listOfFiles:
            # Create full path
        fullPath = os.path.join(dirName, entry)
            # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            print(fullPath)
            getListOfFiles(fullPath)
        else:
            if fullPath.endswith(".mp3") or fullPath.endswith(".wav"):
                shutil.move(fullPath, newLoaction)
                

#Wherever the Soulseek Downloads/complete folder is 
dirName = 'C:/Users/Eoin/Documents/Soulseek Downloads/complete'
listOfFiles = getListOfFiles(dirName)

#To run it cd into wherever you downloaded this file to. 
#Eg I stored it in the Soulseek Downloads folder so from Users 
#1: >cd Eoin 
#2: >cd Documents 
#3: >cd Soulseek Downloads 

#Then type python fileFinder.py
#Make sure youve python added to your path or youll get an error
'''