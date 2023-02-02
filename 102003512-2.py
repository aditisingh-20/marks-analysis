import sys
import time
import pandas as pd
from matplotlib import pyplot as plt

def main():
    argumentList=sys.argv
    logFile=open('102003512-log.txt','w')
    logFile.flush()
    if(len(argumentList)<2):
        logFile.write(str(time.asctime())+' Not enough argument.')
        sys.exit(0)
    elif len(argumentList)>2:
        logFile.write(str(time.asctime())+' Too many arguments.')
        sys.exit(0)
    
    fname=argumentList[1]
    
    try:
        df=pd.read_csv(fname)
    except:
        logFile.write(str(time.asctime())+' Error in reading dataframe from the file.')

    plt.figure(figsize=(20,20))
    plt.subplot(3, 3, 1)
    plt.hist(df['P1'])
    plt.subplot(3, 3, 2)
    plt.hist(df['P2'])
    plt.subplot(3, 3, 3)
    plt.hist(df['P3'])
    plt.subplot(3, 3, 4)
    plt.hist(df['P4'])
    plt.subplot(3, 3, 5)
    plt.hist(df['P5'])
    plt.savefig('102003512-histogram-count.png')

    df['Total']=df['P1']+df['P2']+df['P3']+df['P4']+df['P5']
    plt.subplot(1,1,1)
    plt.hist(df['Total'])
    plt.savefig('102003512-histogram-total.png')

    plt.figure(figsize=(20,20))
    plt.subplot(3, 3, 1)
    plt.plot(df['P1'])
    plt.subplot(3, 3, 2)
    plt.plot(df['P2'])
    plt.subplot(3, 3, 3)
    plt.plot(df['P3'])
    plt.subplot(3, 3, 4)
    plt.plot(df['P4'])
    plt.subplot(3, 3, 5)
    plt.plot(df['P5'])
    plt.savefig('102003512-line-count.png')

    plt.subplot(1,1,1)
    plt.plot(df['Total'])
    plt.savefig('102003512-line-total.png')

    plt.figure(figsize=(20,20))
    plt.subplot(3, 3, 1)
    plt.pie(df['P1'])
    plt.subplot(3, 3, 2)
    plt.pie(df['P2'])
    plt.subplot(3, 3, 3)
    plt.pie(df['P3'])
    plt.subplot(3, 3, 4)
    plt.pie(df['P4'])
    plt.subplot(3, 3, 5)
    plt.pie(df['P5'])
    plt.savefig('102003512-pie-count.png')

    plt.subplot(1,1,1)
    plt.pie(df['Total'])
    plt.savefig('102003512-pie-total.png')

    cols = set(df.columns) - {'RollNumber'}
    df1 = df[list(cols)]
    df1.describe()

    stats=open('102003512-statistics.txt','w')
    stats.flush()
    stats.write(str(df1.describe()))

if __name__ == '__main__':
    main()