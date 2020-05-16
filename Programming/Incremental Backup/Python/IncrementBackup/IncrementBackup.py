import zipfile
import os
import fnmatch
# from numpy import array

# Different way to extract zip files
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


# URL TO CHECK
# https://docs.python.org/3/library/zipfile.html
# https://www.peterbe.com/plog/fastest-way-to-unzip-a-zip-file-in-python



def printFiles(folderpath, pattern):
    x = []
    listOfFiles = os.listdir(folderpath)
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            print (entry)
            x.append(entry)
    return x
    
def sort(x):
    fin = []
    i = 0
    while len(x) is not 0:
        min = x[0]
        minTime = min.split("-")
        for d in x:
            tx = d.split("-")
            print(tx)
            if tx[2] <= minTime[2]: # TX month is earlier or same as minimum
                if tx[0] <= minTime[0]: # TX month is earlier or same as minimum
                    if tx[1][-1:] < minTime[1][-1:]: # Tx day is earlier than minimum
                        min = d
                        print("made it here setting" + min + " as the smallest")
                        minTime = d.split("-")
        fin.append(min) # Put minimum into array
        x.remove(min) # Remove minimum 
    return fin

def main():
    filesList = printFiles('TestData', '*.zip') # Get valid zip files
    # Need to adjust for multiple states of files
    # Example Files.zip and Itunes.zip
    
    # Check get the compatable ones
    sets = sort(filesList)
    print("Sorted list")
    for d in sets:
        print(d)

    #dateIndex = day.rfind(" ")
    #fileName = day[:dateIndex]
    #dateTime = day[dateIndex + 1:-4]
    #print(dateTime)
    #y.append(dateTime.split("-"))


main()


# Get the folder of all the backups
# Organize and zip files extracted to folders 1 -10 accordingly
# Write the changes to be made file using code
# Adjust the following files with the changes in files IE deleting
    # Files that are written to can add extension .abby and .jacob
# Recompress the folders

# Write a decompression function and how that will change
