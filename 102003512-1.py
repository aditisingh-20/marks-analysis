import sys
import time
import pandas as pd

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
        df=pd.read_csv(fname,na_values=['NAN','X','-','nan','Na','N/A','n/a',' '])
    except:
        logFile.write(str(time.asctime())+' Error in reading dataframe from the file.')

    n=len(df.columns)
    if n!=3:
        print(n)
        logFile.write(str(time.asctime())+' DataFrame does not have 3 columns. Exiting..')
        sys.exit(0)

    df=df.fillna(0)
    df1 = pd.DataFrame()
    df1=df.reset_index().groupby(['RollNumber', 'Submission'])['Marks'].aggregate('first').unstack()
    df1=df1.fillna(0)
    df1.to_csv('output.csv')

if __name__ == '__main__':
    main()