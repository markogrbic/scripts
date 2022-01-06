# This script renames specifically named files and chanegs the date time format in the name.
# The files have the following name structure "NAME_DATE(MMDDYY)_TIME(HHMMSS).extension".
# The script modifies it to the following structure "NAME_YYYY_MM_DD_HHMMSS.jpg".

import os, os.path, datetime, re

# Set directory path.
# Example path: "/Users/<user>/Desktop/temp"
path = input('Enter directory path: ')
dirs = os.listdir(path)

for file in dirs:
    print(f"Before Renaming: {file}")

    string_list = re.split('; |, |\_|\.', file)
    file_date_time = string_list[1] + " " + string_list[2]
    #print("file parsed time: " + file_date_time)

    date_time = datetime.datetime.strptime(file_date_time, "%m%d%y %H%M%S")
    #print(date_time)

    new_date_time_format = date_time.strftime("_%Y_%m_%d_%H%M%S")
    #print(new_date_time_format)

    new_name = string_list[0] + new_date_time_format + ".jpg"
    print(f"After Renaming: {new_name}")

    os.rename((path + "/" + file), (path+ "/" + new_name))
