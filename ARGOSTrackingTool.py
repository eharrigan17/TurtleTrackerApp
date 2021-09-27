#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2021
#--------------------------------------------------------------
#pretend we read one line of data from the file
lineString = '20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0'

#split the string into a list of data items
lineData = lineString.split()

#Extract items in list into variables
record_id = lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData[6]
obs_long = lineData[7]

#print location of sara the Turtle
print(f"Record {record_id} indicated Sara was seen at lat: {obs_lat}, lon:{obs_long} on {obs_date}")

#Task3
#Create a variable pointing ot the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name, 'r')

#read contents of file into a list
line_list = file_object.readlines()

#close the file
file_object.close()

#Pretend we read one line of data from the file
lineString = line_list[100]

#Split the string into a list of data items
lineData = lineString.split()

#Extract items in list into variables
record_id = lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData[6]
obs_lon = lineData[7]

#print the location of sara
print(f"Record {record_id} indicates Sara was seen at lat: {obs_lat}, lon:{obs_lon} on {obs_date}")

#Task 4
#Interate through all lines in the linelist using for loop
for lineString in line_list:
    if lineString[0] in ("#","u"): continue
                 
    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    #print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat: {obs_lat}, lon:{obs_lon} on {obs_date}")

#using while loop
#Read the first line in the file

lineString = file_object.readline()

#interate using a while loop
while lineString: 
    if lineString[0] in ("#","u"): 
        #read next line
        lineString = file_object.readline()
        continue
                 
    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    #print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat: {obs_lat}, lon:{obs_lon} on {obs_date}")
#Read the next line
    lineString = file_object.readline()
    
#close the file
file_object.close()



