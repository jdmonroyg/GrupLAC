#
#
# #############################################################################
#       Copyright (c) 2018 Universidad Nacional de Colombia All Rights Reserved.
#
#             This work was made as a development to improve data collection
#       for self-assessment and accreditation processes in the Vicedeanship
#       of academic affairs in the Engineering Faculty of the Universidad
#       Nacional de Colombia and is licensed under a Creative Commons
#       Attribution-NonCommercial - ShareAlike 4.0 International License
#       and MIT Licence.
#
#       by Manuel Embus. Edit by Jesus Monroy
#
#       For more information write me to jai@mfneirae.com
#       Or visit my webpage at https://mfneirae.com/
#       
# #############################################################################
#
#

import openpyxl, sys, os, time, logging
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup       
start_time = time.time()
Dir = os.getcwd()
os.chdir(Dir+"/Bin")
sys.path.append('../Bin')

import grupo, init, plan_estrategico, institucion, linea, sector, integrante, produccion

os.chdir(Dir)
global COD_PRODUCTO
condition = 0


while condition != 1:
    try:
        print ("------> Seleccione la forma en la que desea obtener la información:")
        #print ("1) Imprimir datos en CSV y en Insert")
        #print ("2) Imprimir datos en Insert para MySQL")
        print ("3) Imprimir datos en CSV")
        mode = int(input('-> Seleccione una opción: '))
        #if mode == 1 or mode == 2 or mode == 3:
        if mode ==3:
            condition = 1
        else:
            print ("El varlor escogido no es valido")
    except ValueError:
        print ("Not a number")
print ("------> Inicio de Importación de Registros.")
wb = openpyxl.load_workbook('./Input/Base.xlsx')
sheet = wb['Sheet1']
#total = 7
total = sheet.max_row +1
COD_PRODUCTO = 1
COD_PLAN = 1

init.inicio()
LOG_FILENAME = './Logs/Registros.log'
#print (LOG_FILENAME)
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,
                        format = '%(asctime)s:%(levelname)s:%(message)s')
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}
if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)

print("------> Los GrupLAC han sido cargados, Estado: " + str(1/(total-1)*100) + "%")
print(total)
#2
for q in range(2,total):
    director = sheet['A'+str(q)].value
    name = sheet['B'+str(q)].value
    #last = sheet['C'+str(q)].value
    my_url = sheet['C'+str(q)].value
    #print (type(my_url))
    index1 = my_url.find("nro=")
    index2 = len(my_url)
    RH = my_url[index1:index2]
    
    uClient = uReq(my_url)
    page_html = uClient.read() 
    uClient.close()
    page_soup = soup(page_html,"html.parser") #convierte a codigo html
    containers = page_soup.findAll("table")


    #init.Col_Grupo.append(str(doc) + ";"\
    #+ str(RH) \
    #+ "\n")
    #init.inrel_persona_colciencias.append("REPLACE INTO `uapa_db`.`rel_persona_colciencias` (`cod_rh`,`dni_persona`) VALUES " \
    #+ "('" + str(RH) + "','" + str(doc) + "');\n")
    
    if my_url != '-':
        #from plan_estrategico import contpegrup
        #COD_PRODUCTO = int("".join(str(x) for x in contpegrup))        
        
        #grupo.infogrupextract()
        #plan_estrategico.pegrupextract()
        #institucion.instextract()
        #linea.linextract()
        #sector.secextract()
        #integrante.intextract()
        produccion.prodbiblioextract()
        print("------> "+ name + " por " + director + " ha sido procesado, Estado: " + str(q/(total-1)*100) + "%")
        if q==total-1:
            logging.shutdown()
            print ("------> Escribiendo las bases de datos.")
            import printcsv
            print ("-----------------------------------------------------------------------------------------------")
            print ("")
            print ("------> ¡Extracción Exitosa!")
            print ("------> La información se encuentra en la carpeta: Resultados.")
            print ("------> Tiempo de ejecución: %s Minutos." % ((time.time() - start_time)/60))
            print ("")
            print ("***********************************************************************************************")
            sys.exit()
    COD_PRODUCTO = 1;
    
