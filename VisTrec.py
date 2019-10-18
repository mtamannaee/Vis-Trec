import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import math
import operator
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog
import os
import shutil
from tabulate import tabulate
from datetime import datetime
import pyperclip
from sys import platform


# ____________________________________________________________________________________________________________________ #

app = tk.Tk()

#  TREC FILE VECTORS & VARIABLES   #
runfilenames = []
numberRunfiles = tk.IntVar(app, tk.NONE)
dirRel = tk.StringVar(app, tk.NONE)
relfilename = tk.StringVar(app, tk.NONE)
trecDir = tk.StringVar(app, tk.NONE)
trecDir = os.getcwd()
plotDir = tk.StringVar(app, tk.NONE)
plotHardDir = tk.StringVar(app, tk.NONE)
plotAllDir = tk.StringVar(app, tk.NONE)
latexDir = tk.StringVar(app, tk.NONE)
runTime = tk.StringVar(app, tk.NONE)
resultDir = tk.StringVar(app, tk.NONE)
resultfilenames = []
commandTemp = tk.StringVar(app, tk.NONE)

BBLnames_initOptions=("TREC Files", '--------------------')      #   Tab1    and     Tab2     : initial options for best and base baselines Optionmenu  #
BBLnames_TRECfilesOptions=()

bestBLfilename_P1 = tk.StringVar(app, tk.NONE)                  #   Tab 1    :   Plot Type 1   best baseline  #         GLOBAL
meas_P1 = tk.StringVar(app, tk.NONE)                            #   Tab 1    :   Plot Type 1                  #         GLOBAL
baseBLfilename_P1 = tk.StringVar(app, tk.NONE)                  #   Tab 1    :   Plot Type 2   base baseline #
Pcent_seq = tk.StringVar(app, tk.NONE)                          #   Tab 1    :   Plot Type 2                 #
allQ_ranked=[]                                                  #   Tab 1    :   Plot Type 2   :   ranked queries based on IR MEAS value of baseBL     #         GLOBAL V      #

bestBLfilename_P2 = tk.StringVar(app, tk.NONE)                  #   Tab 2    :   Plot Type 1    #         GLOBAL        #
baseBLfilename_P2 = tk.StringVar(app, tk.NONE)                  #   Tab 2    :   Plot Type 1    #         GLOBAL
meas_P2 = tk.StringVar(app, tk.NONE)                            #   Tab 2    :   Plot Type 1    #
hardRange = tk.StringVar(app, tk.NONE)
hardQ = []
hardQ_ranked=[]
Pcent_seq_P2 = tk.StringVar(app, tk.NONE)                       #   Tab 2    :   Plot Type 2    #

logo = tk.PhotoImage(file='ls3lab_logo3.png')
logo= logo.subsample(12, 14)



#       Functions         #       #       Functions         #       #       Functions         #       #       Functions         #       #       Functions         #       #       Functions         #       #       Functions         #       #       Functions         #       #       Functions         #
# ____________________________________________________________________________________________________________________ #
def bestMenu_P1(value):
    global bestBLfilename_P1
    bestBLfilename_P1= bestBLfilename_P11.get()
    bestBLmenu_P1.configure(fg="blue", width=8)
    plotTypeOneButton.configure(state="active")
# ____________________________________________________________________________________________________________________ #
def baseMenu_P1(value):
    global baseBLfilename_P1
    baseBLfilename_P1=baseBLfilename_P11.get()
    baseBLmenu_p1.configure(fg="blue", width=8)
    plot2.configure(state="active")
# ____________________________________________________________________________________________________________________ #
def bestMenu_P2(value):
    global bestBLfilename_P2
    bestBLfilename_P2=bestBLfilename_P22.get()
    bestBLmenu_P2.configure(fg="blue", width=8)
    plot3.configure(state="active")
    #print(bestBLfilename_P2)

# ____________________________________________________________________________________________________________________ #
def baseMenu_P2(value):
    global baseBLfilename_P2
    baseBLfilename_P2=baseBLfilename_P22.get()
    baseBLmenu_p2.configure(fg="blue", width=8)
    plot4.configure(state="active")
# ____________________________________________________________________________________________________________________ #
def showmeas1():
    with open("majorMeas.txt", "r") as f:
        new1 = tk.Tk()
        tk.Label(new1, text=f.read()).pack()
        new1.mainloop()

# ____________________________________________________________________________________________________________________ #
def runfileUpload():
    global numberRunfiles
    global trecDir
    global resultfilenames
    global runfilenames

    srcDir = filedialog.askdirectory()
    dirFiles = os.listdir(srcDir)

    for file_name in dirFiles:
        full_file_name = os.path.join(srcDir, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, trecDir)

    for i in range(dirFiles.__len__()):
        runfilenames.append(dirFiles[i])
        resultfilenames.append(dirFiles[i].split("."+dirFiles[i].split(".")[-1])[0] + "-TREC.txt")

    numberRunfiles = runfilenames.__len__()
    textString = ""
    textString001= ""
    half1 = []
    half2 = []
    split_point = int
    if (numberRunfiles % 2) == 0:
        split_point = int(numberRunfiles/2)
        half1, half2 = runfilenames[:split_point], runfilenames[split_point:]
    else:
        split_point = int((numberRunfiles+1)/2)
        half1, half2 = runfilenames[:split_point], runfilenames[split_point:]

    for i in range(len(half1)):
        textString = textString + "{}\n".format(runfilenames[i])
    for i in range(len(half2)):
        textString001 = textString001 + "{}\n".format(runfilenames[i])

    fileBrifLable.config(text=textString)
    fileBrifLable2.config(text=textString001)
    plot1BLabel.configure(text="                                              ")

# ____________________________________________________________________________________________________________________ #
def relfileUpload():                            #   TREC    #
    global trecDir
    global dirRel
    global relfilename
    dirRel = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=( ("all files", "*.*"),("adhoc files", "*.ahdoc"),("text files", "*.txt")))
    relfilename = str(dirRel).split("/")[-1]
    shutil.copy(r'{}'.format(dirRel), trecDir)
    print("{} is seleceted to be uploaded.".format(relfilename))
    relBrifLable.config(text=relfilename)
    runTrecButton.config(state="active")

# ____________________________________________________________________________________________________________________ #
def runTrec():                                  #   TREC    #

    print("Trec is running")
    global numberRunfiles
    global resultfilenames
    global runfilenames
    global relfilename
    global runTime
    global trecDir
    global plotDir
    global resultDir
    global latexDir
    global plotAllDir
    global plotHardDir
    global commandTemp

    # PART A : OS PLATFORM TYPE DETECTION  ___________________________________________________________________________ #
    platformList = []
    platformList.append(str(platform))
    p_FL = platformList[0][0]
    commandTemp = ""
    if platform == "linux" or platform == "Linux" or platform == "Linux" or platform == "Linux2" or p_FL == "l" or p_FL == "L":  # linux
        commandTemp = './trec_eval -q  {} {} >> {}'
        print(str(platform))
    elif platform == "darwin" or platform == "Darwin" or p_FL == "d" or p_FL == "D":  # OS X
        commandTemp = './trec_eval -q  {} {} >> {}'
        print(str(platform))
    elif platform == "win32" or platform == "cygwin" or p_FL == "w" or p_FL == "W" or p_FL == "C" or p_FL == "c":  # Windows
        commandTemp = './trec_eval.exe -q  {} {} >> {}'
        print(str(platform))

    # PART B : RUNNING THE TREC EVAL .C CODE _________________________________________________________________________ #

    commandlist = []
    #commandTemp = './trec_eval.exe -q  {} {} >> {}' #CYGWIN
    #commandTemp = './trec_eval -q  {} {} >> {}' #SERVER


    for x in range(numberRunfiles):
        commandlist.append(commandTemp.format(relfilename, runfilenames[x], resultfilenames[x]))

    for y in range(numberRunfiles):
        os.system(commandlist[y])

    textString2 = ""
    textString002 = ""
    if (numberRunfiles % 2) == 0:
        split_point = int(numberRunfiles / 2)
        half1, half2 = resultfilenames[:split_point], resultfilenames[split_point:]
    else:
        split_point = int((numberRunfiles + 1) / 2)
        half1, half2 = resultfilenames[:split_point], resultfilenames[split_point:]

    for i in range(len(half1)):
        textString2 = textString2 + "{}\n".format(resultfilenames[i])
    for i in range(len(half2)):
        textString002 = textString002 + "{}\n".format(resultfilenames[i])

    # PART C : DIRECTORY : Moving files to another directory named based on time stamp _______________________________ #

    runTime = str(datetime.now()).split(" ")[0] + '-' + (str(datetime.now()).split(" ")[1]).split(":")[0] + '-' + \
              (str(datetime.now()).split(" ")[1]).split(":")[1]

    resultDir = str(os.getcwd()) + "/" + runTime            # Directory Definition for trec_eval Result Files #
    latexDir = resultDir + "/Latex"                         # Directory Definition for Code of Latex Table #
    plotDir = resultDir + "/Plots"                          # Directory Definition for Plots #
    plotAllDir = plotDir + "/All Queries Representation"    # Directory Definition for ALL-QUERIES Help&Hurt Plots #
    plotHardDir = plotDir + "/Hard Queries Representation"  # Directory Definition for HARD-QUERIES Help&Hurt Plots #

    if not os.path.exists(resultDir):                       # Directory Creation for trec_eval Result Files #
        os.makedirs(resultDir)

    if not os.path.exists(latexDir):                        # Directory Creation for Code of Latex Table #
        os.makedirs(latexDir)

    if not os.path.exists(plotDir):                         # Directory Creation for Plots #
        os.makedirs(plotDir)

    if not os.path.exists(plotAllDir):                      # Directory Creation for ALL-QUERIES Help&Hurt Plots #
        os.makedirs(plotAllDir)

    if not os.path.exists(plotHardDir):                     # Directory Creation for HARD-QUERIES Help&Hurt Plots #
        os.makedirs(plotHardDir)

    for file_name in runfilenames:                          # Moving Retreval's Run Files to trec_eval directory #
        full_file_name = os.path.join(trecDir, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, resultDir)
            os.remove(file_name)

    for file_name in resultfilenames:                       # Moving trec_eval Result Files to Specified Directory #
        full_file_name = os.path.join(trecDir, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, resultDir)
            os.remove(file_name)

    if (os.path.isfile(os.path.join(trecDir, relfilename))):
        shutil.copy(os.path.join(trecDir, relfilename), resultDir)
        os.remove(relfilename)

    os.chdir(resultDir)
    os.getcwd()

    # PART D : GUI CONFIGURATION ______________________________________________________________________________________#

    resultBrifLable.config(text=textString2)
    resultBrifLable2.config(text=textString002)

    measMenu_P2.config(state="active")
    measMenu_P1.config(state="active")

    global BBLnames_TRECfilesOptions
    BBLnames_TRECfilesOptions = tuple(resultfilenames)

    bestBLmenu_P1['menu'].delete(2, 'end')
    bestBLmenu_P1.configure(state="active")

    baseBLmenu_p1['menu'].delete(2, 'end')
    baseBLmenu_p1.configure(state="active")

    bestBLmenu_P2['menu'].delete(2, 'end')
    bestBLmenu_P2.configure(state="active")

    baseBLmenu_p2['menu'].delete(2, 'end')
    baseBLmenu_p2.configure(state="active")


    for choice in BBLnames_TRECfilesOptions:
        bestBLmenu_P1['menu'].add_command(label=choice, command=tk._setit(bestBLfilename_P11, choice, bestMenu_P1))
        baseBLmenu_p1['menu'].add_command(label=choice, command=tk._setit(baseBLfilename_P11, choice, baseMenu_P1))
        bestBLmenu_P2['menu'].add_command(label=choice, command=tk._setit(bestBLfilename_P22, choice, bestMenu_P2))
        baseBLmenu_p2['menu'].add_command(label=choice, command=tk._setit(baseBLfilename_P22, choice, baseMenu_P2))
    print("Trec is done")
    runTrecLabel.configure(text="                   Trec is done        ")
# ____________________________________________________________________________________________________________________ #
def irMeas_P1(value):                               #   Tab 1    :   Plot Type 1    #
    global meas_P1
    meas_P1 = measVar1.get()    #print(meas_P1)
    measMenu_P1.configure(fg="blue")

    plotTypeOneButton.config(state="active")
    plot2.configure(state="active")

# ____________________________________________________________________________________________________________________ #
def irMeas_P2(value):                               #   Tab 2    :   Plot Type 2    #
    global meas_P2
    meas_P2 = measVar2.get()    #print(meas_P2)
    measMenu_P2.configure(fg="blue")
    plot4.configure(state="active")
    plot3.configure(state="active")
# ____________________________________________________________________________________________________________________ #
#   ***************************************----  PLOTS FunctionS  ----*********************************************    #
#   *****************************************    PLOT 1 Function    ***********************************************    #

def plot1():                # pictures of the graphs : {}-PlotALL.png #
    print("plot type1")
    global bestBLfilename_P1
    global numberRunfiles   # from TREC #
    global resultfilenames  # from TREC #
    global meas_P1
    global resultDir
    global plotAllDir


    bLines = []
    bqueries = []
    TICK_PLT = 3

    with open(str(bestBLfilename_P1), "r") as bf:
        ballLines = bf.readlines()
        for bl in ballLines:
            if bl.split()[1] != "all" and bl.split()[0] == meas_P1:
                bqueries.append(bl.split()[1])
                bLines.append([bl.split()[1], bl.split()[2]])  #
                # print(bqueries)
    for x in range(numberRunfiles):
        if str(resultfilenames[x]) != bestBLfilename_P1:
            with open(str(resultfilenames[x]), "r") as rf:
                diflines = []
                allLines = rf.readlines()
                for l in allLines:
                    if l.split()[1] != "all" and l.split()[0] == meas_P1 and l.split()[1] in bqueries:
                        bindex = bqueries.index(l.split()[1])
                        diffrance = float(bLines[bindex][1]) - float(l.split()[2])
                        diflines.append([l.split()[1], diffrance])
                print(str(resultfilenames[x]))
                yz_setlistdict = dict(diflines)
                sorteddict_yz = OrderedDict(
                    sorted(list(yz_setlistdict.items()), key=operator.itemgetter(1), reverse=True))

                xLabels_plt = list(sorteddict_yz.keys())
                xL_plt = list(range(len(xLabels_plt)))
                xL_plt_2 = []
                xL_plt_2 = xL_plt[1:]

                fig = plt.figure(figsize=(10, 7))
                plt.title("All Queries Representation \n")

                plt.grid(axis='y', linestyle='--', linewidth=0.4, color='black')
                plt.bar(list(range(len(list(sorteddict_yz.keys())))), list(sorteddict_yz.values()), width=1,
                        color='black', align='center', edgecolor='black')
                plt.xticks(xL_plt[::TICK_PLT], xL_plt_2[::TICK_PLT])
                plt.xlim(-0.5, len(xLabels_plt) - 0.5)
                plt.margins(tight="true")
                plt.xlabel("{}".format(resultfilenames[x]), horizontalalignment='center')
                plt.ylabel(r'$\Delta$' + meas_P1 + "\n", horizontalalignment='center')


                graph_name = "{}-ALL.png".format(resultfilenames[x].split("-"+resultfilenames[x].split("-")[-1])[0])
                os.chdir(plotAllDir)
                fig.savefig(graph_name, pad_inches=0.5)
                os.chdir(resultDir)
                print("PLOT TYPE 1 :  {}".format(graph_name))


            rf.close()
    latexBut1.config(state="active")

#   *****************************************    PLOT 2 Function   ************************************************    #

def Plot2():    # pictures of the graphs : {}-ALL%.png #
    print("plot 2 - All Queries %")
    global allQ_ranked
    global baseBLfilename_P1
    global meas_P1
    global resultfilenames
    global Pcent_seq
    global numberRunfiles
    global allQ_ranked
    global resultDir
    global plotAllDir

    Pcent_seq=Pcent_seq_l.get()

    with open('{}'.format(baseBLfilename_P1), "r")as fBase:
        yz_rankBaseBB = []
        baseBLlines = fBase.readlines()
        sorteddict = OrderedDict()
        for l in baseBLlines:
            if l.split()[0] == meas_P1 and l.split()[1] != 'all':
                yz_rankBaseBB.append((l.split()[1], l.split()[2]))
        sorteddict = OrderedDict(sorted(list(dict((list(set(yz_rankBaseBB)))).items()), key=operator.itemgetter(1),
                                        reverse=True))  # print(sorteddict)
        allQ_ranked = list(sorteddict)  # print(allQ_ranked)
    fBase.close()

    percentTest = []
    p = Pcent_seq.split(',')
    percentages = []
    for i in range(p.__len__()):
        if i == 0:
            percentages.append(int(p[i]))
            percentTest.append(int(p[i]))
        else:
            percentages.append(int(p[i]) - int(p[i - 1]))
            percentTest.append(int(p[i]))

    Pack_C = percentages.__len__()
    totalQueryCount = allQ_ranked.__len__()

    packQueryCountList = []
    indxList = []

    counter = percentages.__len__()
    for i in percentages:
        factor = float(i) / 100.00
        packQueryCountList.append((percentages.__len__() - counter, int(totalQueryCount * factor)))
        counter -= 1
    # print(("Packs : {}".format(packQueryCountList)))
    # print("Total Number of Queris : {}".format(totalQueryCount))

    tuple_c = packQueryCountList.__len__() - 1
    # indxList = []
    indxList.append(0)

    for item in packQueryCountList:

        if int(item[0]) == 0:
            indxList.append(item[1])

        elif int(item[0]) == tuple_c:
            indxList.append(totalQueryCount)

        elif 0 <= int(item[0]) or int(item[0]) <= tuple_c:
            indx1 = item[0]
            l2 = []
            l2_values = ()
            for x in range(int(item[0]) + 1):
                l2.append(packQueryCountList[x])

            l2_values = list(zip(*l2))[1]  # print (l2_values) : (15,) and (15, 15)
            sum = 0
            for i in l2_values:
                sum = sum + int(i)
            indxList.append(sum)  # print(("Indexes :{}".format(indxList)))

    rankQpacksList = []  # [[int, [..]],[int,[]],..] : [[int,[indexes]],[int,[querynumber]]]   :   [[0, [...]], [1, [...]], [2, [...]], [3, [...]]]
    rankQPack2 = []  # [[],[],..]  :[[packnumber, querynumber],[],..]  :   [[0, '108'], [0, '142'], ..., [1, '117'], [1, '141'], .., [2, '119'], [2, '118'], .., [3, '110'], [3, '122'],..]
    for i in range(indxList.__len__() - 1):
        first_q_index = indxList[i]  # print(start_indx)
        last_q_index = indxList[i + 1]  # print(end_index)
        rankQPack = []
        for l_indx in range(first_q_index, last_q_index):
            rankQPack.append(allQ_ranked[l_indx])
            rankQPack2.append([i, allQ_ranked[l_indx]])  # print(rankQPack)
        rankQpacksList.append(rankQPack)

    packsAvrgList = []
    for pack in rankQpacksList:
        packNum = rankQpacksList.index(pack)
        for i in range(numberRunfiles):
            with open("{}".format(resultfilenames[i]), 'r') as rf:
                lines = rf.readlines()
                sum_val = 0.0000
                avg_val = 0.0000
                count = 0
                for q in pack:
                    for l in lines:
                        if l.split()[1] == str(q) and l.split()[0] == meas_P1 and l.split()[1] != "all":
                            sum_val = math.fsum([float(sum_val), float(l.split()[2])])
                            count = count + 1
                avg_val = sum_val / count

                packsAvrgList.append([packNum, resultfilenames[i], avg_val])
        packsAvrgList.append([packNum, " ", 0.0])

    sorteeed = sorted(packsAvrgList, key=operator.itemgetter(0))
    op_av = [(x[1], float(x[2])) for x in sorteeed]

    fig = plt.figure(figsize=(10, 7))
    plt.title("All Queries Representation % \n")

    labels, ys = list(zip(*op_av))
    labels_plt = []
    xs = np.arange(len(labels))

    plt.grid(axis='y', linestyle='--', linewidth=0.4, color='black', zorder=0)
    bars = plt.bar(xs, ys, width=1, align='center', edgecolor='black', color='w', zorder=3)

    #plt.xlim(-0.5, len(bars) - 0.5)  --> to remove the margins in xaxis
    #plt.margins(tight="true")        -->             //

    patterns = ["///", "\\\\", "||||", "xx", "oo", "OO", "\\\\\\\\\\", "----", "+++", ".", "..."]
    patterns_2 = []
    for j in range(percentTest.__len__()):
        for i in patterns[0:numberRunfiles]:
            patterns_2.append(i)
            labels_plt.append(str(percentTest[j])+"%")
        patterns_2.append("")
        labels_plt.append("")

    for bar, pattern in zip(bars, patterns_2):
        bar.set_hatch(pattern)

    middle = int
    if numberRunfiles % 2 == 0:
        middle = numberRunfiles / 2
    if numberRunfiles % 2 != 0:
        middle = (numberRunfiles + 1) / 2

    plt.xticks(xs[int(middle)::numberRunfiles + 1], labels_plt[int(middle)::numberRunfiles + 1], fontsize=7)
    plt.ylabel(meas_P1 + "\n", horizontalalignment='center')
    plt.xlabel("\n Percentiles \n", horizontalalignment='center')
    plt.legend(bars[0:numberRunfiles:], labels[0:numberRunfiles], loc=0, shadow=True, fancybox=True, title="Legend", ncol=1)

    graph_name = '{}-ALL%.png'.format(meas_P1)
    os.chdir(plotAllDir)
    plt.savefig(graph_name, pad_inches=0.5)
    os.chdir(resultDir)

    print("PLOT TYPE 2 :  {}".format(graph_name))


#   *****************************************    PLOT 3 Function    ***********************************************    #

def plot3():    # pictures of the graphs : {}-Hard.png #
    global hardQ
    global hardQ_ranked
    global resultfilenames
    global runfilenames
    global numberRunfiles
    global hardRangeuperbound
    global bestBLfilename_P2
    global baseBLfilename_P2
    global meas_P2
    global resultDir
    global plotHardDir

    hardRangeuperbound = hardRRange.get()
    hardQ_val = []
    TICK_PLT = 3

    #  finding hard queries based on selected  output
    with open("{}".format(baseBLfilename_P2), "r")as f:
        lines = f.readlines()
        with open('S-HQ{}.txt'.format(meas_P2), "w") as HQ:
            HardQ_counter = 0
            for l in lines:
                if l.split()[1] != 'all' and str(l.split()[0]) == meas_P2 and float(l.split()[2]) <= float(
                        hardRangeuperbound):
                    HQ.writelines("{}                   	{}\n".format('HQ-baseline:{}'.format(baseBLfilename_P2),
                                                                         l.split()[1]))
                    hardQ.append(l.split()[1])
                    hardQ_val.append((l.split()[1], float(l.split()[2])))

        HQ.close()
    f.close()

    sorteddict1 = OrderedDict(
        sorted(list(dict((list(set(hardQ_val)))).items()), key=operator.itemgetter(1),
               reverse=False))  # print(sorteddict)
    hardQ_ranked = list(sorteddict1)  # print(HARDQ_ranked)

    print("the function of Hard Queries values of All Runs vs Best is running ")
    lineTemp1 = '{}                   	{}	{}\n'
    lineTemp0 = '{}                   	{}\n'

    with open("{}".format(bestBLfilename_P2), "r")as fBestH:
        with open('S-HQ{}.txt'.format(meas_P2), "r") as HQ:
            with open('BHQ-{}.txt'.format(meas_P2), "w") as BHQ:
                Blines = fBestH.readlines()
                HQlines = HQ.readlines()

                for Bline in Blines:
                    for HQline in HQlines:
                        if Bline.split()[1] != "all" and Bline.split()[0] == meas_P2 and Bline.split()[1] == \
                                HQline.split()[1]:
                            BHQ.writelines(lineTemp0.format(HQline.split()[1], float(Bline.split()[2])))
            BHQ.close()
        HQ.close()
    fBestH.close()
    with open('BHQ-{}.txt'.format(meas_P2), "r") as BHQ:
        BHQlines = BHQ.readlines()
        for x in range(numberRunfiles):
            if bestBLfilename_P2 != resultfilenames[x]:
                with open('{}'.format(resultfilenames[x]), "r") as fx:
                    with open('H-{}-output{}'.format(meas_P2, x), "w") as fOutHQx:
                        fxlines = fx.readlines()
                        for fxline in fxlines:
                            for BHQline in BHQlines:
                                if fxline.split()[1] != 'all' and fxline.split()[0] == meas_P2 and fxline.split()[1] == \
                                        BHQline.split()[0]:
                                    hard_val_diff = str(float(BHQline.split()[1]) - float(fxline.split()[2]))
                                    fOutHQx.writelines(
                                        lineTemp1.format(BHQline.split()[0], fxline.split()[2], hard_val_diff))
                    fOutHQx.close()
                fx.close()
        BHQ.close()

    for x in range(numberRunfiles):
        if resultfilenames[x] != bestBLfilename_P2:
            with open('H-{}-output{}'.format(meas_P2, x), "r") as fHard:
                hqd = []
                fHardlines = fHard.readlines()
                for fhline in fHardlines:
                    hqd.append((fhline.split()[0], float(fhline.split()[2])))

                hqd_dict = dict(list(set(hqd)))
                sorteddict_hqd = OrderedDict(sorted(list(hqd_dict.items()), key=operator.itemgetter(1), reverse=True))

                fig1 = plt.figure(figsize=(10, 7))
                plt.title("Hard Queries Representation \n")

                xLabels_plt = list(sorteddict_hqd.keys())
                xL_plt = list(range(len(xLabels_plt)))
                xL_plt_2 = []
                xL_plt_2 = xL_plt[1:]

                plt.grid(axis='y', linestyle='--', linewidth=0.4, color='black')
                plt.bar(list(range(len(list(sorteddict_hqd.keys())))), list(sorteddict_hqd.values()), width=1,
                        align='center', color='black', edgecolor='black')

                plt.xlim(-0.5, len(xLabels_plt) - 0.5)
                plt.margins(tight="true")

                # plt.xticks(xL_plt[::TICK_PLT], xL_plt_2[::TICK_PLT])
                plt.xlabel("{}".format(resultfilenames[x]), horizontalalignment='center')
                plt.ylabel(r'$\Delta$' + meas_P2, horizontalalignment='center')


                graph_name = '{}-Hard.png'.format(resultfilenames[x].split("-"+resultfilenames[x].split("-")[-1])[0])
                os.chdir(plotHardDir)
                plt.savefig(graph_name, pad_inches=0.5)
                os.chdir(resultDir)

                print("PLOT TYPE 3 :  {}".format(graph_name))
                
            fHard.close()
    latexBut2.config(state="active")

#   *****************************************    PLOT 4 Function    ***********************************************    #

def plot4():    # pictures of the graphs : {}-Hard%.png #
    global hardQ
    global hardQ_ranked
    global resultfilenames
    global runfilenames
    global numberRunfiles
    global hardRangeuperbound
    global bestBLfilename_P2
    global baseBLfilename_P2
    global meas_P2
    global Pcent_seq_P2
    global resultDir
    global plotHardDir


    Pcent_seq_P2=Pcent_seq_l2.get()
    hardQ_val = []
    TICK_PLT = 3
    hardRangeuperbound = hardRRange.get()

    #  finding hard queries based on selected  output
    with open("{}".format(baseBLfilename_P2), "r")as f:
        lines = f.readlines()
        with open('S-HQ{}.txt'.format(meas_P2), "w") as HQ:
            HardQ_counter = 0
            for l in lines:
                if l.split()[1] != 'all' and str(l.split()[0]) == meas_P2 and float(l.split()[2]) <= float(
                        hardRangeuperbound):
                    HQ.writelines("{}                   	{}\n".format('HQ-baseline:{}'.format(baseBLfilename_P2),
                                                                         l.split()[1]))
                    hardQ.append(l.split()[1])
                    hardQ_val.append((l.split()[1], float(l.split()[2])))

        HQ.close()
    f.close()

    sorteddict1 = OrderedDict(
        sorted(list(dict((list(set(hardQ_val)))).items()), key=operator.itemgetter(1),
               reverse=True))  # print(sorteddict)
    hardQ_ranked = list(sorteddict1)  # print(HARDQ_ranked)

    p = Pcent_seq_P2.split(',')
    percentTest = []
    percentages = []
    for i in range(p.__len__()):
        if i == 0:
            percentages.append(int(p[i]))
            percentTest.append(int(p[i]))
        else:
            percentages.append(int(p[i]) - int(p[i - 1]))
            percentTest.append(int(p[i]))

    Pack_C = percentages.__len__()
    totalQueryCount = hardQ_ranked.__len__()

    packQueryCountList = []
    indxList = []

    counter = percentages.__len__()
    for i in percentages:
        factor = float(i) / 100.00
        packQueryCountList.append((percentages.__len__() - counter, int(totalQueryCount * factor)))
        counter -= 1
    # print(("Packs : {}".format(packQueryCountList)))
    print("Total Number of Queris : {}".format(totalQueryCount))

    tuple_c = packQueryCountList.__len__() - 1  # print(tuple_c) : 3
    # indxList = []
    indxList.append(0)

    for item in packQueryCountList:

        if int(item[0]) == 0:
            indxList.append(item[1])  # print item[0] : 0

        elif int(item[0]) == tuple_c:
            indxList.append(totalQueryCount)  # print item[0] : 3

        elif 0 <= int(item[0]) or int(item[0]) <= tuple_c:
            indx1 = item[0]  # print indx1 : 1, 2
            l2 = []

            for x in range(int(item[0]) + 1):
                l2.append(packQueryCountList[x])

            l2_values = list(zip(*l2))[1]  # print (l2_values) : (15,) and (15, 15)
            sum = 0
            for i in l2_values:
                sum = sum + int(i)
            indxList.append(sum)

    rankQpacksList = []  # [[int, [..]],[int,[]],..] : [[int,[indexes]],[int,[querynumber]]]   :   [[0, [...]], [1, [...]], [2, [...]], [3, [...]]]
    rankQPack2 = []  # [[],[],..]  :[[packnumber, querynumber],[],..]  :   [[0, '108'], [0, '142'], ..., [1, '117'], [1, '141'], .., [2, '119'], [2, '118'], .., [3, '110'], [3, '122'],..]
    for i in range(indxList.__len__() - 1):
        first_q_index = indxList[i]  # print(start_indx)
        last_q_index = indxList[i + 1]  # print(end_index)
        rankQPack = []
        for l_indx in range(first_q_index, last_q_index):
            rankQPack.append(hardQ_ranked[l_indx])
            rankQPack2.append([i, hardQ_ranked[l_indx]])
        # print(rankQPack)
        rankQpacksList.append(rankQPack)

    packsAvrgList = []
    for pack in rankQpacksList:
        packNum = rankQpacksList.index(pack)
        for i in range(numberRunfiles):
            with open("{}".format(resultfilenames[i]), 'r') as rf:
                lines = rf.readlines()
                sum_val = 0.0000
                avg_val = 0.0000
                count = 0
                for q in pack:
                    for l in lines:
                        if l.split()[1] == str(q) and l.split()[0] == meas_P2 and l.split()[1] != "all":
                            sum_val = math.fsum([float(sum_val), float(l.split()[2])])
                            count = count + 1
                avg_val = sum_val / count

                packsAvrgList.append([packNum, resultfilenames[i], avg_val])
        packsAvrgList.append([packNum, " ", 0.0])

    sorteeed = sorted(packsAvrgList, key=operator.itemgetter(0))
    op_av = [(x[1], float(x[2])) for x in sorteeed]

    fig = plt.figure(figsize=(10, 7))
    plt.title("Hard Queries Representation % \n")

    labels, ys = list(zip(*op_av))
    labels_plt = []
    xs = np.arange(len(labels))

    plt.grid(axis='y', linestyle='--', linewidth=0.4, color='black', zorder=0)
    bars = plt.bar(xs, ys, width=1, align='center', edgecolor='black', color='w', zorder=3)

    #plt.xlim(-0.5, len(bars) - 0.5) --> removes the margin on xaxis
    #plt.margins(tight="true")       -->            //

    patterns = ["///", "\\\\", "||||", "xx", "oo", "OO", "\\\\\\\\\\", "----", "+++", ".", "..."]
    patterns_2 = []
    for j in range(percentTest.__len__()):
        for i in patterns[0:numberRunfiles]:
            patterns_2.append(i)
            labels_plt.append(str(percentTest[j])+"%")
        patterns_2.append("")
        labels_plt.append("")

    for bar, pattern in zip(bars, patterns_2):
        bar.set_hatch(pattern)

    middle = int
    if numberRunfiles % 2 == 0:
        middle = numberRunfiles / 2
    if numberRunfiles % 2 != 0:
        middle = (numberRunfiles + 1) / 2

    plt.xticks(xs[int(middle)::numberRunfiles + 1], labels_plt[int(middle)::numberRunfiles + 1], fontsize=7)
    plt.ylabel("\n"+ meas_P2 + "\n", horizontalalignment='center')
    plt.xlabel("\n Percentiles \n", horizontalalignment='center')
    plt.legend(bars[0:numberRunfiles:], labels[0:numberRunfiles], loc=0, shadow=True, fancybox=True, title="Legend",
               ncol=1)

    graph_name = '{}-Hard%.png'.format(meas_P2)
    os.chdir(plotHardDir)
    plt.savefig(graph_name, pad_inches=0.5)
    os.chdir(resultDir)
    print("PLOT TYPE 4 : {}".format(graph_name))

# ____________________________________________________________________________________________________________________ #
#   ***************************************----  LaTex FunctionS  ----*********************************************    #
# LATEX   FUNCTIONS : { latex1, latex2 }
def latex1():
    global resultfilenames  # from TREC #
    global meas_P1
    global numberRunfiles
    global runfilenames
    global resultDir
    global latexDir

    print("latex1 is Running")
    fname_avg = []
    for i in range(numberRunfiles):
        with open("{}".format(resultfilenames[i]), "r")as f:
            lines = f.readlines()
            values = []
            for l in lines:
                if l.split()[0] == meas_P1 and l.split()[1] != "all":
                    values.append(float(l.split()[2]))
            suM = sum(values)
            avG = suM / values.__len__()
            fname_avg.append((resultfilenames[i], avG))
        f.close()

    h = []
    h.append("      ")
    h.append("All Queries ({})".format(meas_P1))

    allLAX = tabulate(fname_avg, headers=h, tablefmt='latex')
    app.clipboard_clear()
    app.clipboard_append(allLAX)
    print(allLAX)

    os.chdir(latexDir)
    with open("LATEX_ALL.txt", "w") as latexFile:
        latexFile.writelines(allLAX)
        latexFile.close()
    os.chdir(resultDir)

    print("latex1 is Done")


def latex2():
    global resultfilenames  # from TREC #
    global meas_P2
    global numberRunfiles
    global runfilenames
    global hardQ
    global resultDir
    global latexDir

    print("latex2 is Running")
    fname_avg = []
    for i in range(numberRunfiles):
        with open("{}".format(resultfilenames[i]), "r")as f:
            lines = f.readlines()
            values = []
            for l in lines:
                if l.split()[0] == meas_P2 and l.split()[1] != "all" and l.split()[1] in hardQ:
                    values.append(float(l.split()[2]))
            suM = sum(values)
            avG = suM / values.__len__()
            fname_avg.append((runfilenames[i], avG))
        f.close()

    print(fname_avg)
    h = []
    h.append("      ")
    h.append("Hard Queries ({})".format(meas_P2))

    hardLAX = tabulate(fname_avg, headers=h, tablefmt='latex')
    app.clipboard_clear()
    app.clipboard_append(hardLAX)

    os.chdir(latexDir)
    with open("LATEX_Hard.txt", "w") as latexFile:
        latexFile.writelines(hardLAX)
        latexFile.close()
    os.chdir(resultDir)

    print("latex2 is Done")
# ____________________________________________________________________________________________________________________ #
#         END   Functions         #       #       END   Functions         #       #       END   Functions         #       #       END   Functions         #       #       END   Functions         #       #       END   Functions         #



#       GUI         #       #       GUI         #       #       GUI         #       #       GUI         #       #       GUI         #       #       GUI         #       #       GUI         #       #       GUI         #       #       GUI         #

#   Main Window of GUI  #
app.geometry('815x740')
mainFrame = tk.Frame(app, bd=5, padx=1, pady=1, relief="ridge")
mainFrame.grid(row=1, column=0, padx=1, pady=1, ipadx=1, ipady=1, sticky="nwes")

#   Main Frame          #
#   Frame (mainFrame) : {Label(x1), topFrame, botFrame, latexFrame}  #
tk.Label(mainFrame, text="   Vis-Trec Application", font=(None, 14, "bold"), fg="maroon").grid(row=0, column=0, sticky="nws")
tk.Label(mainFrame,  image=logo).grid(row=0, column=1,sticky="ne")

topFrame = tk.Frame(mainFrame, bd=2, padx=5, pady=3, relief="sunken")
topFrame.grid(row=1, column=0, columnspan=2, padx=5, pady=3, ipadx=1, ipady=1, sticky="nwes")
botFrame = tk.Frame(mainFrame, bd=2, padx=5, pady=3, relief="sunken")
botFrame.grid(row=2, column=0, columnspan=2, padx=5, pady=3, ipadx=1, ipady=1, sticky="nwes")

# ____________________________________________________________________________________________________________________ #
# ******************************  GUI :  Top Frame : trec_eval Farme    ***********************************************#
# ____________________________________________________________________________________________________________________ #

#   Frame (topFrame) :  {leftTopFrame}  #
leftTopFrame = tk.Frame(topFrame, bd=1, padx=1, pady=1)
leftTopFrame.grid(row=0, padx=1,columnspan=2 , pady=1, ipadx=1, ipady=1, sticky="nwes")

#   Frame (leftTopFrame) :  Trec :{ ..}    #
tk.Label(leftTopFrame, text="Step 1 : Trec Evaluation ", bd=1, padx=1, pady=1, font=(None, 10), fg="maroon").grid(row=0,column=0, padx=1,pady=1,ipadx=1, ipady=1, sticky="w")
tk.Label(leftTopFrame, text=" List Retreival's Run Files:", bd=1, padx=1, pady=1, font=(None, 8), fg="blue").grid(row=0,column=2, padx=1,pady=1,ipadx=1, ipady=1, sticky="w")
tk.Label(leftTopFrame, text="Retreival's Run Folder :", bd=2, padx=1, pady=1, font=(None, 8)).grid(row=1, column=0, padx=1,  pady=1, ipadx=1, ipady=1, sticky="w")
tk.Label(leftTopFrame, text="Trec Relevance File :", bd=2,padx=1, pady=1, font=(None, 8)).grid(row=2, column=0, padx=1, pady=1, ipadx=1, ipady=1, sticky="w")

uploadRunButton = tk.Button(leftTopFrame, text="Upload ", command=runfileUpload,font=(None, 8), width=13)
uploadRunButton.grid(row=1, column=1, padx=1, pady=1, ipadx=1, ipady=1)

fileBrifLable = tk.Label(leftTopFrame, text="      ", fg="blue", font=(None, 8))
fileBrifLable.grid(row=1, column=2, padx=1, pady=1, ipadx=1, ipady=1)

fileBrifLable2 = tk.Label(leftTopFrame, text="     ", fg="blue", font=(None, 8))
fileBrifLable2.grid(row=1, column=3, padx=1, pady=1, ipadx=1, ipady=1)


uploadRelButton = tk.Button(leftTopFrame, text="Upload ", command=relfileUpload, font=(None, 8),width=13)
uploadRelButton.grid(row=2, column=1, padx=1, pady=1, ipadx=1, ipady=1)
relBrifLable = tk.Label(leftTopFrame, text="", fg="blue", font=(None, 8))
relBrifLable.grid(row=2, column=2, padx=1, pady=1,ipadx=1, ipady=1)

runTrecButton = tk.Button(leftTopFrame, text="Run trec_eval", fg="black", command=runTrec, font=(None, 8), state="disabled", width=13)
runTrecButton.grid(row=3, column=2, padx=1, pady=1,ipadx=1, ipady=1, sticky='w')

runTrecLabel = tk.Label(leftTopFrame, text="                         ", bd=2, padx=1,pady=1, font=(None, 9), fg="steel blue")
runTrecLabel.grid(row=3,column=3,padx=1,pady=1,sticky="w")

tk.Label(leftTopFrame, text="List of TREC Result Files :", bd=2, padx=1, pady=1, font=(None, 8), fg="steel blue").grid(row=0, column=4, padx=1,pady=1,sticky="w")

resultBrifLable = tk.Label(leftTopFrame, text="      ", fg="steel blue", font=(None, 8))
resultBrifLable.grid(row=1, column=4,columnspan=2,rowspan=2, padx=1, pady=1,ipadx=1,ipady=1,sticky='Nw')

resultBrifLable2 = tk.Label(leftTopFrame, text="       ", fg="steel blue", font=(None, 8))
resultBrifLable2.grid(row=1, column=5,columnspan=2,rowspan=2, padx=1, pady=1, ipadx=1, ipady=1, sticky='N')

# ***************************** GUI :  End of Top Frame : trec_eval    ************************************************#
# ____________________________________________________________________________________________________________________ #
# ***************************** GUI :  Begining  of Lower Frame : Plots    ********************************************#
# ____________________________________________________________________________________________________________________ #

#   Frame (botFrame) : {Label(x1), Notebook (tabControl)   }  #
tk.Label(botFrame, text="Step 2 : Analysis and Visualization", font=(None, 10), fg="maroon").grid(row=0,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")
tabControl = ttk.Notebook(botFrame, padding='0.02i')


#   Notebook (tabControl) : {tab1, tab2}  #
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='  All Queries  ')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='  Hard Queries  ')


#   Frame(tab1) : {tab1TopFrame,tab1ButFrame}  #
tab1TopFrame = tk.Frame(tab1, bd=2, padx=1, pady=1, relief="sunken")
tab1TopFrame.grid(row=1, column=0, padx=1, pady=1, ipadx=1, ipady=1,sticky="nwes")
tab1ButFrame = tk.Frame(tab1, bd=2, padx=1, pady=1, relief="sunken")
tab1ButFrame.grid(row=2, column=0, padx=1, pady=1, ipadx=1, ipady=1,sticky="nwes")

# ********************************* GUI :  End   of Lower Frame : Plots    ********************************************#
# ____________________________________________________________________________________________________________________ #
# ********************** GUI :  Plot TYPE 1 : Help & Hurt Over ALL Baseline's Ranked Queries    ***********************#
# ____________________________________________________________________________________________________________________ #

#   Frame(tab1TopFrame) : {...}  #
tk.Label(tab1, text="All Queries Relative Representation ", font=(None, 9),fg="maroon").grid(row=0,column=0,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")
tk.Label(tab1TopFrame, text="Plot Type 1 :  Plotting the improvement of selected IR measurement value of all queries over the best baseline ranked queries.", font=(None, 9),fg="IndianRed3").grid(row=0,column=0,columnspan=4,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")
tk.Label(tab1TopFrame, text="IR Measurement : ", font=(None, 8)).grid(row=1,column=0,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

optionList = ("map" ,"gm_ap" ,"R-prec" ,"recip_rank" ,"ircl_prn.0.00","ircl_prn.0.10","ircl_prn.0.20","ircl_prn.0.30",
              "ircl_prn.0.40","ircl_prn.0.50","ircl_prn.0.60","ircl_prn.0.70", "ircl_prn.0.80","ircl_prn.0.90",
              "ircl_prn.1.00","P5","P10","P15","P20", "P30", "P100", "P200", "P500", "P1000")
measVar1 = tk.StringVar()
measVar1.set("Choose")
measMenu_P1 = tk.OptionMenu(tab1TopFrame, measVar1, *optionList, command=irMeas_P1)
measMenu_P1.config(width=9,font=(None, 8), state="disabled")
measMenu_P1.grid(row=1,column=1,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

tk.Label(tab1TopFrame, text="Best Baseline Result File : ", font=(None, 8)).grid(row=3,column=0,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

bestBLfilename_P11=tk.StringVar(app,tk.NONE)
bestBLfilename_P11.set(BBLnames_initOptions[0])
bestBLmenu_P1= tk.OptionMenu(tab1TopFrame,bestBLfilename_P11,*BBLnames_initOptions, command= bestMenu_P1)
bestBLmenu_P1.config(state= tk.DISABLED, width=9,font=(None, 8))
bestBLmenu_P1.grid(row=3,column=1,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

plot1BLabel= tk.Label(tab1TopFrame, text=" ", bd=2,padx=1,pady=1, font=(None, 11), fg="maroon")
plot1BLabel.grid(row=4,column=2,padx=1,pady=1,sticky="w")

plotTypeOneButton = tk.Button(tab1TopFrame, text="Plot", command=plot1, font=(None, 8),width=25, state="disabled")
plotTypeOneButton.grid(row=3, column=3, padx=1, pady=1,ipadx=1,ipady=1,sticky="w")
latexBut1 = tk.Button(tab1TopFrame, text="Generate Table in Latex ", command=latex1, font=(None, 8),fg="DeepSkyBlue4",width=25, state="disabled")
latexBut1.grid(row=4, column=3, padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

# ____________________________________________________________________________________________________________________ #
# ************* GUI :  Plot TYPE 2 : Retrieval's Mean value of Baseline's Ranked Queries Percentiles   *************** #
# ____________________________________________________________________________________________________________________ #

#   Frame(tab1ButFrame) : {...}  #
tk.Label(tab1ButFrame, text="Plot Type 2 :  Plotting all queries mean retrieval effictiveness across baseline's ranked query percentiles.", font=(None, 9),fg="IndianRed3").grid(row=0,column=0,columnspan=4,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")
tk.Label(tab1ButFrame, text="Base Baseline Result File : ", font=(None, 8)).grid(row=1,column=0,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

baseBLfilename_P11 = tk.StringVar(app,tk.NONE)
baseBLfilename_P11.set(BBLnames_initOptions[0])
baseBLmenu_p1= tk.OptionMenu(tab1ButFrame,baseBLfilename_P11,*BBLnames_initOptions, command= baseMenu_P1)
baseBLmenu_p1.config(state= tk.DISABLED, width=8,font=(None, 8))
baseBLmenu_p1.grid(row=1,column=2,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

tk.Label(tab1ButFrame, text="Percentages : %", font=(None, 8)).grid(row=3 ,column=0,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")
Pcent_seq_l = tk.StringVar(None)
Pcent_seq_l.set("10,30,60,70,100")
Pcent_seq_ent = tk.Entry(tab1ButFrame, textvariable=Pcent_seq_l, fg="dim gray",width=14).grid(row=3, column=2,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

plot2Lable = tk.Label(tab1ButFrame, text=" ", font=(None, 8),fg="maroon")
plot2Lable.grid(row=3,column=3,padx=1, pady=1,ipadx=1,ipady=1,sticky="e")

# tk.Label(tab1ButFrame, text=" ", font=(None, 8)).grid(row=4,column=1,padx=1, pady=1,ipadx=1,ipady=1,sticky="e")

plot2 = tk.Button(tab1ButFrame, text="Plot", command=Plot2, font=(None, 8), state="disabled",width=25)
plot2.grid(row=3, column=4, padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

# ____________________________________________________________________________________________________________________ #
# ********************************************   GUI : HARD QUERIES   ************************************************ #
# ____________________________________________________________________________________________________________________ #

#   Frame(tab2) : {tab2TopFrame, tab2midFrame, tab2ButFrame, Label(x2)}
tab2TopFrame= tk.Frame(tab2,bd=2,padx=1,pady=1, relief="sunken")
tab2TopFrame.grid(row=1,column=0,padx=1,pady=1,ipadx=1,ipady=1,sticky="nwes")
tab2midFrame= tk.Frame(tab2,bd=2,padx=1,pady=1, relief="sunken")
tab2midFrame.grid(row=3,column=0,padx=1,pady=1,ipadx=1,ipady=1,sticky="nwes")
tab2butFrame= tk.Frame(tab2,bd=2,padx=1,pady=1, relief="sunken")
tab2butFrame.grid(row=4,column=0,padx=1,pady=1,ipadx=1,ipady=1,sticky="nwes")


tk.Label(tab2, text=" Step 2.1 Hard Queries Identification ", font=(None, 9),fg="maroon").grid(row=0,column=0,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")
tk.Label(tab2, text=" Step 2.2 Hard Queries Relative Representation :", font=(None, 9),fg="maroon").grid(row=2, column=0, padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

# ____________________________________________________________________________________________________________________ #
# *********************************  GUI : HARD QUERIES Identification   ********************************************* #
# ____________________________________________________________________________________________________________________ #
#   Frame(tab2TopFrame) : {...}
tk.Label(tab2TopFrame, text="Hard Queries Metric Selection and Cut-Off value Definition : ", font=(None, 9),fg="IndianRed3").grid(row=0, column=0,columnspan=4,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")
tk.Label(tab2TopFrame, text="IR Measurement : ", font=(None, 8)).grid(row=1,column=0,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

optionList = ("map" ,"gm_ap" ,"R-prec" ,"recip_rank" ,"ircl_prn.0.00","ircl_prn.0.10","ircl_prn.0.20","ircl_prn.0.30",
              "ircl_prn.0.40","ircl_prn.0.50","ircl_prn.0.60","ircl_prn.0.70", "ircl_prn.0.80","ircl_prn.0.90",
              "ircl_prn.1.00","P5","P10","P15","P20", "P30", "P100", "P200", "P500", "P1000")

measVar2 = tk.StringVar()
measVar2.set("Choose")
measMenu_P2 = tk.OptionMenu(tab2TopFrame, measVar2, *optionList, command=irMeas_P2)
measMenu_P2.config(state=tk.DISABLED,width=9,font=(None, 8))
measMenu_P2.grid(row=1,column=1,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

tk.Label(tab2TopFrame, text="Base Baseline Result File : ", font=(None, 8)).grid(row=1,column=2,padx=1, pady=1,ipadx=1, ipady=1, sticky="w")

baseBLfilename_P22=tk.StringVar(app,tk.NONE)
baseBLfilename_P22.set(BBLnames_initOptions[0])
baseBLmenu_p2= tk.OptionMenu(tab2TopFrame,baseBLfilename_P22,*BBLnames_initOptions, command= baseMenu_P2)
baseBLmenu_p2.config(state=tk.DISABLED, width=9,font=(None, 8))
baseBLmenu_p2.grid(row=1,column=3,padx=1, pady=1,ipadx=1,ipady=1)

hardLimitrangeLabel = tk.Label(tab2TopFrame, text="Value Cut-Off Range : ",font=(None, 8))
hardLimitrangeLabel.grid(row=1,column=4,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")
hardRRange=tk.StringVar()
hardRRange.set("0.05")
hardlimitrangeEntry=tk.Entry(tab2TopFrame,textvariable=hardRRange ,width=10 ,fg="dim gray", font=(None, 8))
hardlimitrangeEntry.grid(row=1, column=5, padx=1, pady=1, ipadx=1, ipady=1,sticky="e")

tk.Label(tab2TopFrame, text=" ", font=(None, 5)).grid(row=2,column=4, sticky="w")

# ____________________________________________________________________________________________________________________ #
# ********************  GUI :  Plot TYPE 3 : Help & Hurt Over Baseline's Ranked Hard Queries    ********************** #
# ____________________________________________________________________________________________________________________ #
#   Frame(tab2midFrame) : {...}
tk.Label(tab2midFrame, text="Plot Type 3 :  Plotting the improvement of selected IR measurement value of hard queries over the best baseline", font=(None, 9),fg="IndianRed3").grid(row=0, column=0,columnspan=4,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

tk.Label(tab2midFrame, text="Best Baseline Result File : ", font=(None, 8)).grid(row=1, column=0, padx=1, pady=1,ipadx=1,ipady=1,sticky="w")
bestBLfilename_P22=tk.StringVar(app,tk.NONE)
bestBLfilename_P22.set(BBLnames_initOptions[0])
bestBLmenu_P2= tk.OptionMenu(tab2midFrame,bestBLfilename_P22,*BBLnames_initOptions, command= bestMenu_P2)
bestBLmenu_P2.config(state= tk.DISABLED, width=9, font=(None, 8))
bestBLmenu_P2.grid(row=1, column=1, padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

plot3BLabel= tk.Label(tab2midFrame, text=" ", bd=2,padx=1,pady=1, font=(None, 8), fg="maroon")
plot3BLabel.grid(row=2,column=1,padx=1,pady=1,sticky="w")

plot3 = tk.Button(tab2midFrame, text="Plot", command=plot3, font=(None, 8), state="disabled",width=25)
plot3.grid(row=2, column=2, padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

latexBut2 = tk.Button(tab2midFrame, text="Generate Table in Latex", command=latex2, font=(None, 8),fg="DeepSkyBlue4",width=25, state="disabled")
latexBut2.grid(row=3, column=2, padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

# ____________________________________________________________________________________________________________________ #
# ********** GUI :  Plot TYPE 4 : Retrieval's Mean value of Baseline's Ranked Hard Queries Percentiles   **************#
# ____________________________________________________________________________________________________________________ #
#   Frame(tab2butFrame) : {...}
tk.Label(tab2butFrame, text="Plot Type 4 :  Plotting hard queries mean retrieval effictiveness across baseline's ranked query percentiles.", font=(None, 9),fg="IndianRed3").grid(row=0,column=0,columnspan=4,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

tk.Label(tab2butFrame, text="Percentages : %", font=(None, 8)).grid(row=3 ,column=0,padx=1, pady=1,ipadx=1,ipady=1,sticky="w")
Pcent_seq_l2 = tk.StringVar(None)
Pcent_seq_l2.set("10,30,60,70,100")
Pcent_seq_ent_2 = tk.Entry(tab2butFrame, textvariable=Pcent_seq_l2, fg="dim gray", width=14, font=(None, 8)).grid(row=3, column=1,padx=1, pady=1,ipadx=1,ipady=1,sticky="e")

plot4BLabel= tk.Label(tab2butFrame, text="          ", bd=2,padx=1,pady=1, font=(None, 11), fg="maroon")
plot4BLabel.grid(row=4,column=2,padx=1,pady=1,sticky="w")

plot4 = tk.Button(tab2butFrame, text="Plot", command=plot4, font=(None, 8), state="disabled",width=25)
plot4.grid(row=4, column=3, padx=1, pady=1,ipadx=1,ipady=1,sticky="w")

tabControl.grid(row=1, sticky='EW',padx=1, pady=1,ipadx=1,ipady=1)

app.mainloop()