def intextract():
    from settings import my_url, name, director, RH, containers 
    from init import Integrante
    
    all=0
    global contint
    contint=0
    
    idIntegrante=""    
    Col_Grupo_Codigo_GrupLAC=str(RH)

    for a in range(0,len(containers)):
    	buscarinfo = containers[a]
    	try:
    		if buscarinfo.td.string== "Integrantes del grupo":
    			all=a
    			break
    	except AttributeError:
    		pass

    #extraccion tabla Integrantes
    
    container = containers[all].findAll("td")
    containerb = containers[all].findAll("a")
    #1=nombre 2=vinculacion 3=horas 4=ini-fin
    for x in range(5,len(container),4):
        Numero_Integrante=""
        Nombre_Integrante=""
        Vinculacion_Integrante=""
        Hora_Dedicacion_Integrante=""
        Inicio_Vinculacion_Integrante=""
        Fin_Vinculacion_Integrante=""
        Cod_RH_CvLAC=""
        if container[0].string == "Integrantes del grupo":
        
            Nombre_Integrante=containerb[contint].string.replace("ń","ñ").replace("Ń","Ñ")
            link_CvLAC = containerb[contint].get("href")
            index1=link_CvLAC.find("cod_rh")
            index2=len(link_CvLAC)
            Cod_RH_CvLAC=link_CvLAC[index1:index2]
            contint=contint+1
            
            aux= container[x+1].string.replace("\n","").split()
            for a in range(0,len(aux)):
                Vinculacion_Integrante= Vinculacion_Integrante + aux[a] + " "

            aux= container[x+2].string.replace("\n","").split()
            for a in range(0,len(aux)):
                Hora_Dedicacion_Integrante= Hora_Dedicacion_Integrante + aux[a] + " "
            
            aux= container[x+3].string.replace("\n","").split()
            for a in range(0,len(aux)):
                if len(aux)>=3:
                    Inicio_Vinculacion_Integrante= aux[0]
                    Fin_Vinculacion_Integrante=aux[2]
                else:
                    Inicio_Vinculacion_Integrante= Inicio_Vinculacion_Integrante + aux[a] + " "
                    Fin_Vinculacion_Integrante= Fin_Vinculacion_Integrante + aux[a] + " "


        Integrante.append(str(len(Integrante))+ ";"\
+str(contint) + ";"\
+str(Nombre_Integrante) + ";"\
+str(Vinculacion_Integrante) + ";"\
+str(Hora_Dedicacion_Integrante) + ";"\
+str(Inicio_Vinculacion_Integrante) + ";"\
+str(Fin_Vinculacion_Integrante) + ";"\
+str(Col_Grupo_Codigo_GrupLAC) + ";"\
+str(Cod_RH_CvLAC) + ";"\
+ "\n")
