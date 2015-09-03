#!/bin/bash

#It takes default index and sends it to a temporary file
cat index.html > modified.html

#backup solution:
#echo -n "Type the command:  "
#read command

#It shows the result of ls command and sends it to the temp file
echo  `ls` >  temp.html

#It replaces the expression CofC for the content of temp
sed  "s/CofC/$(cat temp.html)/" modified.html > CSCI362.html

#It shows the result on the browser
echo  `gnome-open CSCI362.html`

