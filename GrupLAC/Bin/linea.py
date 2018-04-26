def linextract():
    from settings import my_url, name, director, RH, containers 
    from init import Linea
    
    all=0
    global contlin
    contlin=0
    
    idLinea=""
    Numero_Linea=""
    Nombre_Linea=""
    Col_Grupo_Codigo_GrupLAC=str(RH)

    for a in range(0,len(containers)):
    	buscarinfo = containers[a]
    	try:
    		if buscarinfo.td.string== "Líneas de investigación declaradas por el grupo":
    			all=a
    			break
    	except AttributeError:
    		pass

    #extraccion tabla Instituciones
    
    container = containers[all].findAll("td")
    for x in range(1,len(container)):
        if container[0].string == "Líneas de investigación declaradas por el grupo":
            contlin=contlin+1
            aux= container[x].string.replace("\n","").replace(";","|").replace("ż", "¿").replace("Ż","¿").replace("ş"," ").replace("Ş"," ").replace("ń","ñ").replace("ŕ","á").replace("−","-").replace("Ń","Ñ").replace("Ň","Ó").replace("ň","ó").replace('"'," ").replace("ă","ó").replace("Ă","ó").replace("ˇ"," ").replace("³","").replace("Č","É").replace("Ě","Í").replace("Ŕ","Á").replace("Ő","Õ").replace("č","è").replace("ě","ì").replace("ł","").split()
            for x in range(0,len(aux)):
                Nombre_Linea= Nombre_Linea + aux[x] + " "
            index1=Nombre_Linea.find(".- ")+3
            index2=len(Nombre_Linea)
            Nombre_Linea=Nombre_Linea[index1:index2]
        Linea.append(str(len(Linea))+ ";"\
+str(contlin) + ";"\
+str(Nombre_Linea) + ";"\
+str(Col_Grupo_Codigo_GrupLAC) + ";"\
+ "\n")
