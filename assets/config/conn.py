import pyodbc
from controllers import Funciones

server = 'ITSUPPORT-PC\\ITSUPPORT' 
database = 'RelojPonchesDB' 
username = '' 
password = ''


try:             
    connOpen = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
except Exception as ex:
    Funciones.MessageTipo.vistamensageNormal("E",ex)
