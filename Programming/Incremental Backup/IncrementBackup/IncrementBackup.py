import zipfile
import os
import fnmatch
import hashlib
import sys
# from os import listdir
# from os.path import isfile, join

# MD5 a file based on chunks
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
			x.append(entry)
	return x

# Sorts files based on the date instead of names (2-1-20 is before 2-10-20)
def sortDates(x): 
	fin = []
	i = 0
	fileName = x[0].rfind(" ")
	while len(x) != 0:
		min = x[0]
		minTime = min[fileName:].split("-")
		for d in x:
			tx = d[fileName:].split("-")

		# Can simplify by to say months and days
			if int(tx[2][:-4]) <= int(minTime[2][:-4]): # TX month is earlier or same as minimum
				if int(tx[0]) <= int(minTime[0]): # TX month is earlier or same as minimum
					if int(tx[1]) < int(minTime[1]): # Tx day is earlier than minimum
						min = d
						minTime = d[fileName:].split("-")
		fin.append(min) # Put minimum into array
		x.remove(min) # Remove minimum
	return fin

# Sorting the array1 based on the numbers in array2
def selectionSort(array1, array2): # Filename, Hashname
	# Traverse through all array elements 
	for i in range(len(array2)): 
		# Find the minimum element in remaining unsorted array 
		min_idx = i
		for j in range(i+1, len(array2)): 
			if array2[min_idx] > array2[j]: 
				min_idx = j
		# Swap the found minimum element with the first element		 
		array1[i], array1[min_idx] = array1[min_idx], array1[i] 
		array2[i], array2[min_idx] = array2[min_idx], array2[i] 
	return array1, array2


def getFiles(fp): # Files Path
	x = []
	y = os.listdir()
	while len(y) > 0:
		cur = y[0]
		print(cur)
		print(y)
		if os.path.isdir(cur):
			tmp = os.listdir(cur)
			for t in tmp:
				y.append(t)
#			y.append(os.listdir(cur))
		elif os.path.isfile(cur):
			x.append(cur)
		y.remove(cur)
#	print(y[0])
#	print("I GOT FILES")
	return x

def main():
	workspace = "TestData"
	# os.chdir(workspace) # Created issues
	filesList = printFiles('TestData', '*.zip') # Get valid zip files
	# Need to adjust for multiple states of files
												   # Example Files.zip and Itunes.zip
	
	# Check get the compatable ones
	sets = sortDates(filesList) # This sorting works


	# Since they are zip have to extract them
	# Adjust later for temporary files
	for i in range(0, len(sets) , 1):
		# Create target Directory if don't exist
		dirName = "Output\\" + str(i)
		if not os.path.exists(dirName):
			os.mkdir(dirName)
			print("Directory " , dirName ,  " Created ")
			zipfile.ZipFile(workspace + "\\" + sets[i]).extractall(dirName)
		else:
			print("Directory " , dirName ,  " already exists")
#		zipfile.ZipFile(workspace + "\\" + sets[i]).extractall(dirName)
				
	# Compare all of them to the folder 0
	# First need md5 of all the files
	os.chdir("Output\\0")
	baseFiles = getFiles("..") # What comparing everything to
	baseHash = []
#    print(os.path.abspath(baseFiles[0]))
	for b in baseFiles: # For directory 0
		baseHash.append(md5_a_file(b))

	for i in range(1, len(sets) , 1):
		os.chdir("..\\" + str(i))
		changeFiles = printFiles(".", "*")
		changeHash = []
		for c in changeFiles: # The new directory
			changeHash.append(md5_a_file(c))
		A,B = selectionSort(changeFiles, changeHash)
		for i in range(len(A)):
#            print(A[i]) # Filename
#            print(B[i]) # Hashnames
			if B[i] in baseHash: # Hash Exist
				print(os.path.abspath(A[i]))
				xp = A[i]
				print(os.path.abspath(A[i]) + " is the same as \n" + os.path.abspath(baseFiles[baseHash.index(B[i])]))
#				print(baseHash.index(B[i]) + " Is the same as " + B[i])
#                print(A[i] + " Already has been found")
			else: # Writes file because unique
#				print(A[i] + " is a new file")
				baseFiles.append(A[i])
				baseHash.append(B[i])

	print("Total Files")
	for i in range(len(baseFiles)):
		print(baseFiles[i])

main()


# Write the changes to be made file using code
# Adjust the following files with the changes in files IE deleting
# Files that are written to can add extension .abby and .jacob
# Recompress the folders

# Write a decompression function and how that will change
