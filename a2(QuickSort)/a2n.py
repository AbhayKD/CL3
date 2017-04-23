import  xml.etree.ElementTree as ET
from  threading import Thread,current_thread
import  threading
import  time

class Quicksort:
    value=0;
    def __init__(self,val):	 	#initializing data objects
        self.value=val

    def quickSort(self,alist):		#quicksort method
	self.sort(alist,0,len(alist)-1)

    def sort(self,alist,first,last):     	#method for sorting concurrently
        if first<last:
	    splitpoint = self.partition(alist,first,last)
	    #creating threads
	    t1=threading.Thread(target=self.sort, name="thread1", args=(alist,first,splitpoint-1))
	    t2=threading.Thread(target=self.sort, name="thread2", args=(alist,splitpoint+1,last))
            #starting threads
	    t1.start()
	    t2.start()
	    #waiting all threads to complete
	    t1.join()
	    t2.join()

    def partition(self,alist,first,last):		#function for dividing data
	print "Thread", current_thread().getName(), "handling with Pivot", alist[first], "\n"
	pivotvalue = alist[first]
        leftmark = first+1
	rightmark = last
	done = False
	while not done:		#quicksort algoritm
	    while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
	        leftmark = leftmark + 1

	    while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
		rightmark = rightmark -1

	    if rightmark < leftmark:
		done = True
	    else:
		temp = alist[leftmark]
		alist[leftmark] = alist[rightmark]
		alist[rightmark] = temp

	temp = alist[first]
	alist[first] = alist[rightmark]
	alist[rightmark] = temp
	return rightmark


#Declaration
datalist = []
tempObj = Quicksort
intlist = []
sortedData = []

fname=raw_input("Enter the XML file name : ")
tree = ET.parse(fname);			#taking input from XML file
root = tree.getroot()

for num in root.findall("number"):		#moving input from file to list
    tempObj = Quicksort(int(num.find('value').text))
    datalist.append(tempObj);

for obj in datalist:			#copying data to another list to sort
    intlist.append(obj.value)
					#sorting integer data
tempObj = Quicksort(0) 			#Constructor initialization
tempObj.quickSort(intlist)
					#sorting remaining data
for val in intlist:
    for obj in datalist:
	if obj.value==val:
	    sortedData.append(obj)

print "Sorted List"			#printing sorted data
for obj in sortedData:
    print str(obj.value)
