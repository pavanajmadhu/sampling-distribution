import plotly.figure_factory as ff
import pandas as pd
import csv
import random
import statistics
import plotly.graph_objects as go

df=pd.read_csv("medium_data.csv")
data=df["title"].tolist()


populationmean=statistics.mean(data)
stddeviation=statistics.stdev(data)
print("standard deviation is : ", stddeviation)
print("mean is : ",populationmean)

def randommeans(counter):
    dataset=[]
    for i in range(0,counter):
       randomindex=random.randint(0,len(data))
       value=data[randomindex]
       dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def showfig(meanlist):
    df=meanlist
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        setofmeans=randommeans(30)
        mean_list.append(setofmeans)
    showfig(mean_list)
    mean=statistics.mean(mean_list)
    print("mean of sampling distribution : ",mean)

def standarddeviation():
    meanlist=[]
    for i in range(0,100):
        setofmeans=randommeans(30)
        meanlist.append(setofmeans)
    stddevtion=statistics.stdev(meanlist)
    print("standard deviation of sampling distribution : ",stddevtion)


setup()
standarddeviation()


