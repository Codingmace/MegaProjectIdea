import zipfile
import os
import fnmatch
# from numpy import array

def f1(fn, dest):
    with open(fn, 'rb') as f:
        zf = zipfile.ZipFile(f)
        zf.extractall(dest)

    total = 0
    for root, dirs, files in os.walk(dest):
        for file_ in files:
            fn = os.path.join(root, file_)
            total += _count_file(fn)
    return total

def printFiles(folderpath, pattern):
    x = []
    listOfFiles = os.listdir(folderpath)
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            print (entry)
            x.append(entry)
    return x
    

# Get the folder of all the backups
# Organize and zip files extracted to folders 1 -10 accordingly
# Write the changes to be made file using code
# Adjust the following files with the changes in files IE deleting
    # Files that are written to can add extension .abby and .jacob
# Recompress the folders

# Write a decompression function and how that will change

# URL TO CHECK
# https://docs.python.org/3/library/zipfile.html
# https://www.peterbe.com/plog/fastest-way-to-unzip-a-zip-file-in-python


def main():
    filesList = printFiles('TestData', '*.zip') # Get valid zip files
    # Check get the compatable ones
    y = []
    filesList.sort()
    while len(filesList) is not 0:
        min = filesList.pop()
        for day in filesList:
            dateIndex = day.rfind(" ")
            fileName = day[:dateIndex]
            dateTime = day[dateIndex + 1:-4]
            print(dateTime)
            y.append(dateTime.split("-"))


main()