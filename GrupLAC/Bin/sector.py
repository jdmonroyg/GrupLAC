def secextract():
    from settings import my_url, name, director, RH, containers 
    from init import Sector
    
    all=0
    global contsec
    contsec=0
    
    idSector=""
    Numero_Sector=""
    Nombre_Sector=""
    Col_Grupo_Codigo_GrupLAC=str(RH)

    for a in range(0,len(containers)):
    	buscarinfo = containers[a]
    	try:
    		if buscarinfo.td.string== "Sectores de aplicación":
    			all=a
    			break
    	except AttributeError:
    		pass

    #extraccion tabla Instituciones
    
    container = containers[all].findAll("td")
    for x in range(1,len(container)):
        if container[0].string == "Sectores de aplicación":
            contsec=contsec+1
            aux= container[x].string.replace("\n","").split()
            for x in range(0,len(aux)):
                Nombre_Sector= Nombre_Sector + aux[x] + " "
            index1=Nombre_Sector.find(".- ")+3
            index2=len(Nombre_Sector)
            Nombre_Sector=Nombre_Sector[index1:index2]
        Sector.append(str(len(Sector))+ ";"\
+str(contsec) + ";"\
+str(Nombre_Sector) + ";"\
+str(Col_Grupo_Codigo_GrupLAC) + ";"\
+ "\n")
