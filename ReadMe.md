<p align="right">
<img src="https://github.com/mtamannaee/Vis-Trec/blob/master/Images/ls3lab_logo3.png" height="25%" width="25%">
</p>

# Vis-Trec READ-ME
# What is Vis-Trec?
Vis-Trec, Visualization tool as the extension of Trec_eval tool to facilitate researchers in the IR task evaluation and visualization step.
In general Vis-Trec conducts 4 types of analysis and visualizations the analysis.
__Help-Hurt visualization__ of the analysis over baseline’s ranked and query percentiles for both __ALL__ queries and defined __Hard__ queries.
__Visualization__ of the analysis over baseline’s ranked query __percentiles__ for both __ALL__ and __HARD__ queries. 
Moreover, considering the user’s selected metric of measurement, the measured values for each retrieval gets inserted in a __LaTEX table__ which code can easily get generated and printed within a text file in the specified directory by Vis-Trec. 

# How To Start?
## Setup Check-List
1. This application works on __Python 3.6__ . This version has a builtin graphical library Tkinter. 
2. If you are using Unix, you have to forward the application via SSH X11 forwarding. 
3. There are  libraries that you need to download and import :  __numpy__, __matplotlib__, and __tabulate__
#### What is Vis-Trec? Where can I get it? How to set up?
Full youtube tutorial on how to use this application on this link :
https://youtu.be/OVJiRS8t9jQ

## Vis-Trec Application Steps
### Step 1 : trec_eval Compilation 
####  Window A  : trec_eval() Compilation
### Step 2 : All Queries Plots + LaTex + All Systems Plots 
####  Window B  : All Queries Help Hurt Plots + LaTex
####  Window C  : Query Percentiles on All systems
### Step 3 : Hard Queries ID + HQ Help-Hurt Plots + Latex + HQ All Systems
####  Window D  : Hard Queries Identification
####  Window E  : Hard Queries Help Hurt Plots + Latex
####  Window F  : Hard Query Percentiles on All systems


# FAQ
### 1. The GUI looks too small/large.
#### Why is that happening?
In case you are useing Desplying Server (eg. X11 forwarding using Xming) , the render size of  fonts on Windows is different from the render size on a Linux ; which may compress or enlarge the fonts on client application (your Computer). remote client applications rendered by Xming may display with smaller or larger fonts than you expect. 
For more details please refer to th efollowing link: http://www.straightrunning.com/XmingNotes/fonts.php 
#### How can I fix it? 
You can adjust the fonts and their sizes on the client application by configuration on the remote host to fix a problem on the local display. You can adjust the fonts and the sizes the way you wish useing the python template file provided on this link : 
http://www.straightrunning.com/XmingNotes/mkfontalias.py

### 2. When I try to run trec_eval() on server , I get __"permission denied"__ command-line error.
#### Why is that happening?
Since this application will run the trec_eval.c code, you need to make sure have the c compiler and the "execution permission" if you are running it on the server UNIX based environment.
#### How can I fix it?
To give execution permission in UNIX you can use this command ___“chmod +x filename”___.

### 3. I use Python 3.7, when I try to run Vis-Trec, It gives me error.
#### Why is that happening?
This program is written with Python 3.6 verion.  The error hapends because the Python3.7 is has its own version of Tcl and Tk.
when we run the pyhton file a test on the path of the Tcl and Tk library will fail and causes errors.
#### How can I fix it?
Update to Python 3.6. Some usefull links of updating to Python 3.6 :
* __Ubuntu :__ http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/
* __Windows :__ Go to Python Official Page(https://www.python.org/downloads/), download and install the exe file.
* __Mac OS X :__ Go to Python Official Page(https://www.python.org/downloads/), download Mac OS X and install it.

