Fuzzywuzzy is a python open source string comparison project
Python 2.7 or later version must be installed in order for the project to run

Fuzzywuzzy must be installed, all the required files are in the project folder
To install, just run the command below from the project directory
	>sudo python setup.py install

The injected faults are highlight by comments, they involve changing return values and altering expressions to return faulty results. After the faults are injected, fuzzywuzzy must be reinstalled using the above command

After install, navigating to the scripts folder and typing
	>./scripts/runAllTests.sh
executes all test cases by parsing the text files located there and outputting them to an html file and then opening the file in a browser

