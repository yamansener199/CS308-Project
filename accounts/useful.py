from os import PRIO_PGRP
import openpyxl
from pathlib import Path
import pandas as pd
import sqlite3
import pandas as pd
from json import dumps
FILENAME="hospital_info.xlsx"

def ReadData():
    filename="hospital_info.xlsx"
    df=pd.read_excel(FILENAME, 'Sheet', usecols = "C:G,I:K")
    return df
    
def Hospital_Markers_Turkey():
    df=pd.read_excel(FILENAME, 'Sheet', usecols = "C:G,I:K")
    list_of_list=[]
    for index, row in df.iterrows():
        test_elem=row.to_list()
        if(test_elem[0]=="İSTANBUL"):
            list_of_list.append(test_elem)
    data_hospital={}
    for i in range(len(list_of_list)):
        data_hospital[i]={
                    'province':str(list_of_list[i][0]),
					'district':str(list_of_list[i][1]),
					'hospital_name':str(list_of_list[i][2]),
                    'hospital_type':str(list_of_list[i][3]),
					'service_type':str(list_of_list[i][4]),
					'lat':float(list_of_list[i][5]),
					'len':float(list_of_list[i][6]),
                    'telephone':str(list_of_list[i][7])}
    dataJSON = dumps(data_hospital)
    return dataJSON

def Patient_Markers(Patient):
    coordinates=[]
    lat_len={}
    for object in Patient:
        coordinates.append([
		    object['name'],
			object['surname'],
			object['hospital_name'],
			object['lat'],
			object['len'],
			object['Doctorname'],
			object['bloodtype']])
    for i in range(len(coordinates)):
        lat_len[i]={'patient_name':str(coordinates[i][0]),
					'patient_surname':str(coordinates[i][1]),
					'hospital_name':str(coordinates[i][2]),
					'lat':float(coordinates[i][3]),
					'len':float(coordinates[i][4]),
					'Doctorname':str(coordinates[i][5]),
					'bloodtype':str(coordinates[i][6])}
    dataJSON = dumps(lat_len)
    return dataJSON