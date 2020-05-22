import zipfile
import os
import fnmatch
import hashlib
import sys

# Class for the nodes
class ListNode:
    def __init__(self, data, path):
        self.data = data # Set Data
        self.next = None # Set Reference (Following Node)
        self.path = path # Sets the path

    def set_hash(self, value): # Sets the hash data
        self.hash = value

    def get_hash(self): # Returns hash
        return self.hash

    def has_value(self, value): # Compares the value with node value
        return self.data == value

# The linked list
class SingleLinkedList:
    def __init__(self): 
        self.head = None # Making a null first pointer
        self.tail = None

    def add_list_item(self, item): # Adds item to the end of the list
        if not isinstance(item, ListNode):
            item = ListNode(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def list_length(self): # Returns size of list
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count

    def printList(self): # Prints Node values
        current_node = self.head        
        while current_node is not None:
            print(current_node.data + " " + current_node.path)
            current_node = current_node.next

    def unordered_search (self, value): # Searches List for Node with data equal to value        
        # define current_node
        current_node = self.head
        # define position
        node_id = 1
        # define list of results
        results = []
        while current_node is not None:
            if current_node.has_value(value):
                return node_id
#                results.append(node_id)
            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1
        return -1
#        return results

    def remove_list_item_by_id(self, item_id): # Remove node with id for data
        current_id = 1
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_id == item_id:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    # we don't have to look any further
                    return
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1
        return

def exampleLinkedList():
	# create four single nodes
	node1 = ListNode(15)
	node2 = ListNode(8.2)
	item3 = "Berlin"
	node4 = ListNode(15)

	track = SingleLinkedList()
	print("track length: %i" % track.list_length())

	for current_item in [node1, node2, item3, node4]:
		track.add_list_item(current_item)
		print("track length: %i" % track.list_length())
		track.printList()


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
		for j in range(i + 1, len(array2)): 
			if array2[min_idx] > array2[j]: 
				min_idx = j
		# Swap the found minimum element with the first element
		array1[i], array1[min_idx] = array1[min_idx], array1[i] 
		array2[i], array2[min_idx] = array2[min_idx], array2[i] 
	return array1, array2

# Gets if a value is found in the list. If it is returns which index
def linkedFind(lists, value):
	count = 0
	for a in lists:
		if a== None:
			return -1
		c = a.unordered_search(value)
		if c >= 0: # element exist
			return count
		else:
			count+=1
	return -1 # It was not found

def printGrid(grid):
	for u in grid:
		u.printList()
		print("")

def getFiles(fp): # Files Path
	x = []
	y = os.listdir()
	while len(y) > 0:
		cur = y[0]
#		print(cur)
#		print(y)
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
	grid = []
#	grid.append(None)
#	maping = SingleLinkedList()
	# Compare all of them to the folder 0
	# First need md5 of all the files
	os.chdir("Output\\0")
	for i in range(0, len(sets) , 1):
		os.chdir("..\\" + str(i))
		baseFiles = getFiles(".") # What comparing everything to
		baseHash = []
	#    print(os.path.abspath(baseFiles[0]))
		for b in baseFiles: # For directory 0
			data = md5_a_file(b)
			path = os.path.abspath(b)
#			print(path)
			print(data + " " + path)
			q = ListNode(data, path)
			itemIndex = linkedFind(grid, data)
			if linkedFind(grid,data) >= 0: # It was found
				grid[itemIndex].add_list_item(q)
			else: # Adds the new item
				qs = SingleLinkedList()
				qs.add_list_item(q)
				grid.append(qs)
#				grid.append((SingleLinkedList().add_list_item(q)))
#				grid[len(grid)-1].add_list_item(q)
#				printGrid(grid)
				# Traverse Back so that we can find the node
	#		baseHash.append(md5_a_file(b))
	printGrid(grid)
#	for u in grid:
#		u.printList()

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
#				print(os.path.abspath(A[i]))
				xp = A[i]
				print(os.path.abspath(A[i]) + " is the same as " + os.path.abspath(baseFiles[baseHash.index(B[i])]))
#				print(baseHash.index(B[i]) + " Is the same as " + B[i])
#                print(A[i] + " Already has been found")
			else: # Writes file because unique
#				print(A[i] + " is a new file")
				baseFiles.append(A[i])
				baseHash.append(B[i])
				
	print("Total Files")
	for i in range(len(baseFiles)):
		print(baseFiles[i])

#	exampleLinkedList()
main()



# ADJUSTMENT
# Write the changes to be made file using code
# Adjust the following files with the changes in files IE deleting
# Files that are written to can add extension .abby and .jacob
# Recompress the folders

# Write a decompression function and how that will change
