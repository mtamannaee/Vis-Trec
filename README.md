<p align="right">
<img src="https://github.com/mtamannaee/Vis-Trec/blob/master/Images/ls3lab_logo3.png" height="25%" width="25%">
</p>

# Vis-Trec
<p align="left">
Vis-Trec, Visualization tool as the extension of Trec_eval tool to facilitate researchers in the IR task evaluation and visualization step.
In general Vis-Trec conducts 4 types of analysis and visualizations the analysis in order to avoid time-consuming repetitive task in IR domain for researchers. Plot type 1 i.e, Help-Hurt visualization of the analysis over baseline’s ranked and query percentiles for both ALL queries and defined Hard queries and plot type 2  i.e  visualization of the analysis over baseline’s ranked query percentiles for both ALL and HARD queries . Mor over, considering the user’s selected metric of measurement, the measured values for each retrieval gets inserted in a Latex table which code can easily get generated and printed within a text file in the specified directory by Vis-Trec. 
</p>

<p align="left">
Requirements and Experimental Setup 
This application is coded in python. Runs trec-eval() and gathers the results files. Calculate the results of the IR metrics. Plots the analysis and stores the figures within the created directory.
Eliminates the need of re-evaluating and re-calculating the results for further analysis 
Maintaining the run files and results within the desired directory chosen by the user.
The results of the runs get loaded to defined directory given by the user.
Result files remain safe in their own directory named after the timestamp the trec_eval results were generated for the sake of clear categorization.
</p>

<p align="center">
<img src="https://github.com/mtamannaee/Vis-Trec/blob/master/Images/GUI%20windows.png" height="100%" width="100%">
<img src="  https://github.com/mtamannaee/Vis-Trec/blob/master/Test-Files/output/Plots/All%20Queries%20Representation/run-bm25-ALL.png" height="50%" width="50%">
<img src="https://github.com/mtamannaee/Vis-Trec/blob/master/Test-Files/output/Plots/All%20Queries%20Representation/map-ALL%25.png" height="50%" width="50%">
<img src="https://github.com/mtamannaee/Vis-Trec/blob/master/Test-Files/output/Plots/Hard%20Queries%20Representation/map-Hard%25.png" height="50%" width="50%">
<img src="https://github.com/mtamannaee/Vis-Trec/blob/master/Test-Files/output/Plots/Hard%20Queries%20Representation/run-ql-Hard.png" height="50%" width="50%">
<img src="https://github.com/mtamannaee/Vis-Trec/blob/master/Test-Files/output/Latex/LaTex%20Code%20%26%20Table.png" height="50%" width="50%">
  
</p>

