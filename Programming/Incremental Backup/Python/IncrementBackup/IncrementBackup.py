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
    fileName = x[0].rfind(" ")
    while len(x) is not 0:
        min = x[0]
        minTime = min.split("-")
        for d in x:
            tx = d.split("-")
#            print(tx)

        # Can simplify by to say months and days
            if int(tx[2][:-4]) <= int(minTime[2][:-4]): # TX month is earlier or same as minimum
                if int(tx[0][fileName:]) <= int(minTime[0][fileName:]): # TX month is earlier or same as minimum
                    if int(tx[1]) < int(minTime[1]): # Tx day is earlier than minimum
                        min = d
#                        print("made it here setting" + min + " as the smallest")
                        minTime = d.split("-")
        fin.append(min) # Put minimum into array
        x.remove(min) # Remove minimum 
    return fin

def main():
    filesList = printFiles('TestData', '*.zip') # Get valid zip files
    # Need to adjust for multiple states of files
    # Example Files.zip and Itunes.zip
    
    # Check get the compatable ones
    sets = sort(filesList) # This sorting works
    print("Sorted list") 
    for d in sets:
        print(d)

    # Since they are zip have to extract them
    # Adjust later for temporary files
    for i in range(0, len(sets) -1 , 1):
        # Create target Directory if don't exist
        dirName = "Output\\" + str(i)
        if not os.path.exists(dirName):
            os.mkdir(dirName)
            print("Directory " , dirName ,  " Created ")
            if (i == 1):
                print("That is the file")
                zipfile.ZipFile(sets[i]).extractall(dirName)
#                f1(sets[i], dirName)
        else:
            print("Directory " , dirName ,  " already exists")
    
        



main()


# Get the folder of all the backups
# Organize and zip files extracted to folders 1 -10 accordingly
# Write the changes to be made file using code
# Adjust the following files with the changes in files IE deleting
    # Files that are written to can add extension .abby and .jacob
# Recompress the folders

# Write a decompression function and how that will change
