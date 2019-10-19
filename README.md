<p align="right">
<img src="https://github.com/mtamannaee/Vis-Trec/blob/master/Images/ls3lab_logo3.png" height="25%" width="25%">
</p>

# Vis-Trec
## Abstract 
<p align="left">
Vis-Trec, Visualization tool as the extension of Trec_eval tool to facilitate researchers in the IR task evaluation and visualization step.
In general Vis-Trec conducts 4 types of analysis and visualizations the analysis in order to avoid time-consuming repetitive task in IR domain for researchers. Plot type 1 i.e, Help-Hurt visualization of the analysis over baseline’s ranked and query percentiles for both ALL queries and defined Hard queries and plot type 2  i.e  visualization of the analysis over baseline’s ranked query percentiles for both ALL and HARD queries . Mor over, considering the user’s selected metric of measurement, the measured values for each retrieval gets inserted in a Latex table which code can easily get generated and printed within a text file in the specified directory by Vis-Trec. 
</p>

## Requirements and Experimental Setup
<p align="left"> 
This application is coded in python. Runs trec-eval() and gathers the results files. Calculate the results of the IR metrics. Plots the analysis and stores the figures within the created directory.
Eliminates the need of re-evaluating and re-calculating the results for further analysis 
Maintaining the run files and results within the desired directory chosen by the user.
The results of the runs get loaded to defined directory given by the user.
Result files remain safe in their own directory named after the timestamp the trec_eval results were generated for the sake of clear categorization.
</p>

## Plotting the IR system performance
### GUI
<p align="center">
<img src="https://github.com/mtamannaee/Vis-Trec/blob/master/Images/GUI%20windows.png" height="100%" width="100%">
 </p> 
### Evaluation and Visualizations:
#### Plot Type 1
Vis-Trec sorts the queries based on the measured metric e.g, map values and  draws barplots indicating the sorted queries measured values in order. This method provides the visualization of the system-method over all queries as they are  ordered by their measured metric values for convenient interpretation.  All the runs’ performance can be compared on each query separately to the given selected baseline as it is shown in Figure bellow:
<p align="center">
<img src="  https://github.com/mtamannaee/Vis-Trec/blob/master/Test-Files/output/Plots/All%20Queries%20Representation/run-bm25-ALL.png" height="50%" width="50%">
 </p>
#### Plot Type 2
Based on the given sequence of  percentages, the sorted queries get divided into groups. The series of the percentages get defined by the user. For each category, the average values get calculated for each percentile category  based on the measured metric values the sorted queries belonging to that percentile category. This feature provides a better insight on retrieval method performance inconsistency i.e, different retrieval method performance varies on different query difficulty range as it is shown in Figure bellow
<p align="center">
<img src="https://github.com/mtamannaee/Vis-Trec/blob/master/Test-Files/output/Plots/All%20Queries%20Representation/map-ALL%25.png" height="50%" width="50%">
</p>
#### Plot Type 3
 <p align="center">
<img src="https://github.com/mtamannaee/Vis-Trec/blob/master/Test-Files/output/Plots/Hard%20Queries%20Representation/run-ql-Hard.png" height="50%" width="50%">
</p>
#### Plot Type 4
<p align="center">
<img src="https://github.com/mtamannaee/Vis-Trec/blob/master/Test-Files/output/Plots/Hard%20Queries%20Representation/map-Hard%25.png" height="50%" width="50%">
</p>

## Table Generator in Latex
<p align="left">
Considering the fact that the results of analysis for the run files given by the user and the metric measured values derived from the trec_eval() function gets generated, compared, and further analysed by this application, the LaTeX code of a table including those results could be quite helpful for researchers to gather the results in a format that could be easily implanted into their documentation. Generating the laTeX code in same platform as the results are generated decreasea the chance of error caused by  human error in transferring numbers. To this aim, this option has been provided that  the final results get published in LaTex format printed as shown in Figure bellow:
</p> 

<p align="center">
<img src="https://github.com/mtamannaee/Vis-Trec/blob/master/Test-Files/output/Latex/LaTex%20Code%20%26%20Table.png" height="70%" width="70%">
</p>
  


