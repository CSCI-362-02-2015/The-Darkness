from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os
outputFile = open("../reports/testReport.html","w")
for file in os.listdir("../testCases"):
	f=open("../testCases/"+file,"r")
	lines=f.readlines()
	outputFile.write("<p>Test " + lines[0].rstrip() + "<br>")
	outputFile.write("Requirement: " + lines[1].rstrip() + "<br>")
	outputFile.write("Component: " + lines[2].rstrip() + "<br>")
	outputFile.write("Method: " + lines[3].rstrip() + "<br>")
	input =lines[4].rstrip().split("|")
	output = getattr(eval(lines[2]), lines[3].rstrip())(input[0], input[1])
	#print lines[2], lines[3], lines[4], input[0], input[1]
	outputFile.write("Input parameters: " + input[0] + ", " + input[1] + "<br>")
	outputFile.write("Actual output: " + str(output) + "<br>")
	outputFile.write("Expected output: " + lines[5].rstrip() + "<br>")
	if str(output) == lines[5].rstrip():
		outputFile.write("PASSED</p>")
	else:
		outputFile.write("FAILED</p>")


	