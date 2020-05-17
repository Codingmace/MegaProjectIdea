import zipfile
import os
import fnmatch
import hashlib
import sys
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

def md5_a_file(filePath, block_size=128 * 16):
    md5 = hashlib.md5()
    f = open(filePath, "rb")
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    
    return md5.hexdigest()

def printFiles(folderpath, pattern):
    x = []
    listOfFiles = os.listdir(folderpath)
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
            x.append(entry)
    return x
    
def sortDates(x):
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
#                        print("made it here setting" + min + " as the
#                        smallest")
                        minTime = d.split("-")
        fin.append(min) # Put minimum into array
        x.remove(min) # Remove minimum
    return fin


def selectionSort(array1, array2): # Filename, Hashname
    A = [64, 25, 12, 22, 11] 
    # Traverse through all array elements 
    for i in range(len(A)): 
        # Find the minimum element in remaining unsorted array 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
        # Swap the found minimum element with the first element		 
        A[i], A[min_idx] = A[min_idx], A[i] 
    return A




def main():
    workspace = "TestData"
    # os.chdir(workspace) # Created issues
    filesList = printFiles('TestData', '*.zip') # Get valid zip files
    # Need to adjust for multiple states of files
                                                   # Example Files.zip and Itunes.zip
    
    # Check get the compatable ones
    sets = sortDates(filesList) # This sorting works
    print("Sorted list") 
    for d in sets:
        print(d)

    # Since they are zip have to extract them
    # Adjust later for temporary files
    for i in range(0, len(sets) , 1):
        # Create target Directory if don't exist
        dirName = "Output\\" + str(i)
        if not os.path.exists(dirName):
            os.mkdir(dirName)
            print("Directory " , dirName ,  " Created ")
        else:
            print("Directory " , dirName ,  " already exists")
        zipfile.ZipFile(workspace + "\\" + sets[i]).extractall(dirName)
                
    # Compare all of them to the folder 0
    # First need md5 of all the files
    os.chdir("Output\\0")
    baseFiles = printFiles(".", "*") # What comparing everything to
    baseHash = []
    print(os.path.abspath(baseFiles[0]))
    for b in baseFiles: # For directory 0
        baseHash.append(md5_a_file(b))
        print(md5_a_file(b))

    for i in range(1, len(sets) , 1):
        os.chdir("..\\" + str(i))
        changeFiles = printFiles(".", "*")
        changeHash = []
        for c in changeFiles: # The new directory
            changeHash.append(md5_a_file(c))
            print(md5_a_file(c))
        A = selectionSort(changeFiles, changeHash)
        print ("Sorted array") 
        for i in range(len(A)): 
            print("%d" %A[i])


main()


# Write the changes to be made file using code
# Adjust the following files with the changes in files IE deleting
# Files that are written to can add extension .abby and .jacob
# Recompress the folders

# Write a decompression function and how that will change
