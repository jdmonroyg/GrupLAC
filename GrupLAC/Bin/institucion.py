def instextract():
    from settings import my_url, name, director, RH, containers 
    from init import Institucion
    
    all=0
    global continst
    continst=0
    
    idInstitucion=""
    Numero_Institucion=""
    Nombre_Institucion=""
    Col_Grupo_Codigo_GrupLAC=str(RH)

    for a in range(0,len(containers)):
    	buscarinfo = containers[a]
    	try:
    		if buscarinfo.td.string== "Instituciones":
    			all=a
    			break
    	except AttributeError:
    		pass

    #extraccion tabla Instituciones
    
    container = containers[all].findAll("td")
    for x in range(1,len(container)):
        if container[0].string == "Instituciones":
            continst=continst+1
            aux= container[x].string.replace("\n","").split()
            for x in range(0,len(aux)):
                Nombre_Institucion= Nombre_Institucion + aux[x] + " "
            index1=Nombre_Institucion.find(".- ")+3
            index2=len(Nombre_Institucion)
            Nombre_Institucion=Nombre_Institucion[index1:index2]
        Institucion.append(str(len(Institucion))+ ";"\
+str(continst) + ";"\
+str(Nombre_Institucion) + ";"\
+str(Col_Grupo_Codigo_GrupLAC) + ";"\
+ "\n")
