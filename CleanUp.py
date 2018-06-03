"""
Cleans up a directory

moves the files with the specified file extension to the specified target directory
Replace the source directory and target directory w/ intended direcort names

Author: Satish
"""
import os, re, shutil

#defining source and target
sourceDir = 'C:\\Users\\Satish Kumar Singh\\Desktop'
targetDir = 'C:\\Users\\Satish Kumar Singh\\Desktop\\images'

filesInDir = os.listdir(sourceDir)
countOfFiles=0
fileType = re.compile('.*\.JPEG')

for file in  filesInDir:
    if (fileType.match(file)):
        #print(file)
        countOfFiles += 1
        #create the target directory if not exists
        if not os.path.isdir(targetDir):
            os.mkdir(targetDir)
        shutil.move(sourceDir + "\\" + file, targetDir)
print("Total of", countOfFiles ,"files moved from", sourceDir, "to", targetDir)
