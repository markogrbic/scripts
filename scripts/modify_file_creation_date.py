# This script modifies the creation date of all the files in a folder.
# The files have the following name structure "NAME_DATE(MMDDYY)_TIME.extension"
# The Date and Time are extracted out of the name and assigned as the new Creation Date for the file.

import os, os.path, sys, time, datetime, re
from subprocess import call

# Set directory path.
# Example path: "/Users/<user>/Desktop/temp/"
path = input('Enter directory path: ')
dirs = os.listdir(path)

# Iterate over all the files in the directory.
for file in dirs:

    ## Skip .DS_Store files.
    if(file == ".DS_Store"):
        continue

    print(file)

    complete_path = path + file

    creationTime = time.ctime(os.path.getctime(complete_path))
    lastModifiedTime = time.ctime(os.path.getmtime(complete_path))

    print("ORIGINAL TIME:")
    print("created: %s" % creationTime)
    print("last modified: %s" % lastModifiedTime)
    print()

    # https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
    stringList = re.split('; |, |\_|\.', file)

    #print(stringList[1])
    #print(stringList[2])
    dtString = stringList[1] + " " + stringList[2] 
    print("file parsed time: " + dtString)
    print()

    # https://docs.python.org/3/library/datetime.html
    print("NEW TIME")
    dt = datetime.datetime.strptime(dtString, "%m%d%y %H%M%S")
    print(dt)
    print()

    newDate = dt.strftime("%m/%d/%Y")
    newTime = dt.strftime("%H:%M:%S")
    newDT = "\"" + newDate + " " + newTime + "\" "
    print("New date: " + newDate)
    print("New time: " + newTime)
    print(newDT)
    print()

    # https://stackoverflow.com/questions/56008797/how-to-change-the-creation-date-of-file-using-python-on-a-mac
    # https://gmelikov.com/2016/12/19/change-a-files-last-modified-and-creation-dates-on-mac-os-x-and-linux/
    command = 'SetFile -d ' + newDT + complete_path
    call(command, shell=True)
    print(command)
    print()

    creationTime2 = time.ctime(os.path.getctime(complete_path))
    lastModifiedTime2 = time.ctime(os.path.getmtime(complete_path))

    print("NEW TIME SET:")
    print("created: %s" % creationTime2)
    print("last modified: %s" % lastModifiedTime2)
    print()

    print("############################################")

print("DONE")
