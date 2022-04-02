import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def laborStatisticsPlot(filename):
    fileIn = open(filename, "r")
    xAxis = []
    dataPoints = []
    word = ""
    data = 0
    next(fileIn)
    for textLine in fileIn:
        textLine = textLine.strip()
        textLine = textLine.split()
        for i in textLine:
            if textLine[0] == i:
                word = word+i
            elif textLine[1] == i:
                word = word+" "+i
            elif textLine[2] == i:
                data = data+float(i)
        xAxis.append(word)
        dataPoints.append(data)
        word = ""
        data = 0
    fig, ax = plt.subplots()
    ax.plot(xAxis, dataPoints)
    ax.set(title='Real Wages in the US from 2006 to 2021')
    ax.set_ylabel('Real Weekly Wage')
    fmt_half_year = mdates.MonthLocator(interval=2)
    ax.xaxis.set_major_locator(fmt_half_year)
    ax.grid(True)
    ax.grid(True)
    plt.show()
laborStatisticsPlot("Labor_Data.txt")