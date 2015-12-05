from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os
outputFile = open("reports/testReport.html","w")
outputFile.write("<html>")
outputFile.write("<center>")
outputFile.write("<table border='1'  bordercolor='#FFFFFF'>")
outputFile.write("<tr>");
outputFile.write("<td bgcolor='#E0DFEE'><center><FONT SIZE='3'>Test</td>")
outputFile.write("<td bgcolor='#E0DFEE'><center><FONT SIZE='3'>Requirement</td>")
outputFile.write("<td bgcolor='#E0DFEE'><center><FONT SIZE='3'>Component</td>")
outputFile.write("<td bgcolor='#E0DFEE'><center><FONT SIZE='3'>Method</td>")
outputFile.write("<td bgcolor='#E0DFEE'><center><FONT SIZE='3'>Input parameters</td>")
outputFile.write("<td bgcolor='#E0DFEE'><center><FONT SIZE='3'>Actual output</td>")
outputFile.write("<td bgcolor='#E0DFEE'><center><FONT SIZE='3'>Expected output</td>")
outputFile.write("<td bgcolor='#E0DFEE'><center><FONT SIZE='3'>Result</td>")
for file in os.listdir("testCases"):
	f=open("testCases/"+file,"r")
	lines=f.readlines()
	outputFile.write("<tr>");
	outputFile.write("<td bgcolor='#E0DFEE'><center><FONT SIZE='3'> " + lines[0].rstrip() + "</td>")
	outputFile.write("<td bgcolor='#E0DFEE'><FONT SIZE='3'>" + lines[1].rstrip() + "</td>")
	outputFile.write("<td bgcolor='#E0DFEE'><center><FONT SIZE='3'>" + lines[2].rstrip() + "</td>")
	outputFile.write("<td bgcolor='#E0DFEE'><FONT SIZE='3'>" + lines[3].rstrip() + "</td>")
	input =lines[4].rstrip('\n').split("|")
	output = getattr(eval(lines[2]), lines[3].rstrip('\n'))(input[0].strip(), input[1].strip())
	#print lines[2], lines[3], lines[4], input[0], input[1]
	outputFile.write("<td bgcolor='#E0DFEE'><FONT SIZE='3'>" + input[0] + ", " + input[1] + "</td>")
	outputFile.write("<td bgcolor='#E0DFEE'><FONT SIZE='3'>" + str(output) + "</td>")
	outputFile.write("<td bgcolor='#E0DFEE'><FONT SIZE='3'>" + lines[5].rstrip() + "</td>")
	if str(output) == lines[5].rstrip():
		outputFile.write("<td bgcolor='#00FF00'><FONT SIZE='3'>")
		outputFile.write("PASSED")
	else:
		outputFile.write("<td bgcolor='#FF0000'><FONT SIZE='3'>")
		outputFile.write("FAILED")
	outputFile.write("</td>")
	outputFile.write("</tr>")
	f.close()
outputFile.write("</table>")
outputFile.write("</center>")
outputFile.write("</html>")
outputFile.close()

	
