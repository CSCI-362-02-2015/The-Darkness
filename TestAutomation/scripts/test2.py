from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os
outputFile = open("../reports/testReport.html","w")
outputFile.write("<html>")
outputFile.write("<center>")
outputFile.write("<table border='1'  bordercolor='#FFFFFF'>")
outputFile.write("<tr>");
outputFile.write("<td bgcolor='#E0DFEE'><center>Test</td>")
outputFile.write("<td bgcolor='#E0DFEE'><center>Requirement</td>")
outputFile.write("<td bgcolor='#E0DFEE'><center>Component</td>")
outputFile.write("<td bgcolor='#E0DFEE'><center>Method</td>")
outputFile.write("<td bgcolor='#E0DFEE'><center>Input parameters</td>")
outputFile.write("<td bgcolor='#E0DFEE'><center>Actual output</td>")
outputFile.write("<td bgcolor='#E0DFEE'><center>Expected output</td>")
outputFile.write("<td bgcolor='#E0DFEE'><center>Result</td>")
for file in os.listdir("../testCases"):
        f=open("../testCases/"+file,"r")
        lines=f.readlines()
        outputFile.write("<tr>");
        outputFile.write("<td bgcolor='#E0DFEE'><center>" + lines[0].rstrip() + "</td>")
        outputFile.write("<td bgcolor='#E0DFEE'>" + lines[1].rstrip() + "</td>")
        outputFile.write("<td bgcolor='#E0DFEE'><center>" + lines[2].rstrip() + "</td>")
        outputFile.write("<td bgcolor='#E0DFEE'>" + lines[3].rstrip() + "</td>")
        input =lines[4].rstrip().split("|")
        output = getattr(eval(lines[2]), lines[3].rstrip('\n'))(input[0], input[1])
        #print lines[2], lines[3], lines[4], input[0], input[1]
        outputFile.write("<td bgcolor='#E0DFEE'>" + input[0] + ", " + input[1] + "</td>")
        outputFile.write("<td bgcolor='#E0DFEE'>" + str(output) + "</td>")
        outputFile.write("<td bgcolor='#E0DFEE'>" + lines[5].rstrip() + "</td>")
        if str(output) == lines[5].rstrip():
		outputFile.write("<td bgcolor='#00FF00'>")
                outputFile.write("PASSED")
        else:
		outputFile.write("<td bgcolor='#FF0000'>")
                outputFile.write("FAILED")
        outputFile.write("</td>")
        outputFile.write("</tr>")
outputFile.write("</table>")
outputFile.write("</center>")
outputFile.write("</html>")
