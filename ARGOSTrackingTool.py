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