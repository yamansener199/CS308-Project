import openpyxl
from pathlib import Path
import pandas as pd
import sqlite3
import pandas as pd
def ReadData():
    filename="hospital_info.xlsx"
    df=pd.read_excel(filename, 'Sheet', usecols = "C:G,I:K")
    print(df.head(0))
    return df

def Hospital_Lat_Len():
    filename="hospital_info.xlsx"
    df=pd.read_excel(filename, 'Sheet', usecols = "C:G,I:K")
    

