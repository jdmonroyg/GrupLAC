def prodbiblioextract():
    from settings import my_url, name, director, RH, containers 
    from init import Produccion
    
    art_pub=0
    cap_lib_pub=0
    doc_trab=0
    lib_pub=0
    o_pub_div=0
    o_art_pub=0
    o_lib_pub=0
    trad=0

    global contprodbiblio
    contprodbiblio=0

    
    Clasificacion_Produccion="PRODUCCIÓN BIBLIOGRÁFICA"
    Col_Grupo_Codigo_GrupLAC=str(RH)

    for a in range(0,len(containers)):
        buscarinfo = containers[a]
        try:
            if buscarinfo.td.string== "Artículos publicados":
                art_pub=a
            elif buscarinfo.td.string =="Capítulos de libro publicados ":
                cap_lib_pub=a
            elif buscarinfo.td.string =="Documentos de trabajo ":
                doc_trab=a
            elif buscarinfo.td.string ==" Libros publicados ":
                lib_pub=a
            elif buscarinfo.td.string =="Otra publicación divulgativa":
                o_pub_div=a
            elif buscarinfo.td.string =="Otros artículos publicados":
                o_art_pub=a
            elif buscarinfo.td.string ==" Otros Libros publicados ":
                o_lib_pub=a
            elif buscarinfo.td.string =="Traducciones ":
                trad=a
                break
        except AttributeError:
            pass

    #extraccion tabla Articulos publicados
    
    container = containers[art_pub].findAll("tr")
    # containerb[27].findAll("img")
    #1=nombre 2=vinculacion 3=horas 4=ini-fin
    for x in range(1,len(container)):
        Tipo_Produccion="Artículos publicados"
        Validacion_Produccion="No"
        N_Registro_Produccion=""
        Descripcion_Produccion=""
        Nombre_Produccion=""    
        Informacion_Adicional_Produccion=""    
        Autores_Produccion=""
        
        containerb = container[x].findAll("td")
        
        if len(containerb[0])>2:
            Validacion_Produccion="Si"
        for y in range(0,len(containerb)):
            if len(containerb[y].text)>3:
                aux=containerb[y].text.replace(";","|").replace("ż", "").replace("Ż","¿").replace("ş","").replace("ń","ñ").replace("ŕ","r").replace("−","-").replace("Ń","Ñ").replace("Ň","Ñ").replace("ň","ñ").replace("ě","e")
                #for a in range(0,len(aux)):
                #    informacion= informacion + aux[a] + " "
                index1 = aux.find("Autores:")
                index2 = len(aux)
                informacion=aux[index1+8:index2].split()
                for a in range(0,len(informacion)):
                    Autores_Produccion= Autores_Produccion + informacion[a] + " "
                aux=aux[0:index1]

                index1 = aux.find(".-")
                index2 = len(aux)
                informacion=aux[0:index1].split()
                for a in range(0,len(informacion)):
                    N_Registro_Produccion= N_Registro_Produccion + informacion[a] + " "
                aux=aux[index1+2:index2]

                index1 = aux.find(":")
                index2 = len(aux)
                Descripcion_Produccion=aux[0:index1]
                aux=aux[index1+1:index2]

                index1 = aux.find("\n")
                index2 = len(aux)
                informacion=aux[0:index1].split()
                for a in range(0,len(informacion)):
                    Nombre_Produccion= Nombre_Produccion + informacion[a] + " "
                aux=aux[index1+1:index2]

                informacion=aux.split()
                for a in range(0,len(informacion)):
                    Informacion_Adicional_Produccion=Informacion_Adicional_Produccion + informacion[a] + " "
        
        Produccion.append(str(len(Produccion))+ ";"\
+str(Clasificacion_Produccion) + ";"\
+str(Tipo_Produccion) + ";"\
+str(Validacion_Produccion) + ";"\
+str(N_Registro_Produccion) + ";"\
+str(Descripcion_Produccion) + ";"\
+str(Nombre_Produccion) + ";"\
+str(Informacion_Adicional_Produccion) + ";"\
+str(Autores_Produccion) + ";"\
+str(Col_Grupo_Codigo_GrupLAC) + ";"\
+ "\n")

    container = containers[cap_lib_pub].findAll("tr")
    # containerb[27].findAll("img")
    #1=nombre 2=vinculacion 3=horas 4=ini-fin
    for x in range(1,len(container)):
        Tipo_Produccion="Capítulos de libro publicados"
        Validacion_Produccion="No"
        N_Registro_Produccion=""
        Descripcion_Produccion=""
        Nombre_Produccion=""    
        Informacion_Adicional_Produccion=""    
        Autores_Produccion=""
        
        containerb = container[x].findAll("td")
        
        if len(containerb[0])>2:
            Validacion_Produccion="Si"
        for y in range(0,len(containerb)):
            if len(containerb[y].text)>3:
                aux=containerb[y].text.replace(";","|").replace("ż", "").replace("Ż","¿").replace("ş","").replace("ń","ñ").replace("ŕ","r").replace("−","-").replace("Ń","Ñ").replace("Ň","Ñ").replace("ň","ñ").replace("ě","e")
                #for a in range(0,len(aux)):
                #    informacion= informacion + aux[a] + " "
                index1 = aux.find("Autores:")
                index2 = len(aux)
                informacion=aux[index1+8:index2].split()
                for a in range(0,len(informacion)):
                    Autores_Produccion= Autores_Produccion + informacion[a] + " "
                aux=aux[0:index1]

                index1 = aux.find(".-")
                index2 = len(aux)
                informacion=aux[0:index1].split()
                for a in range(0,len(informacion)):
                    N_Registro_Produccion= N_Registro_Produccion + informacion[a] + " "
                aux=aux[index1+2:index2]

                index1 = aux.find(":")
                index2 = len(aux)
                Descripcion_Produccion=aux[0:index1]
                aux=aux[index1+1:index2]

                index1 = aux.find("\n")
                index2 = len(aux)
                informacion=aux[0:index1].split()
                for a in range(0,len(informacion)):
                    Nombre_Produccion= Nombre_Produccion + informacion[a] + " "
                aux=aux[index1+1:index2]

                informacion=aux.split()
                for a in range(0,len(informacion)):
                    Informacion_Adicional_Produccion=Informacion_Adicional_Produccion + informacion[a] + " "
        
        Produccion.append(str(len(Produccion))+ ";"\
+str(Clasificacion_Produccion) + ";"\
+str(Tipo_Produccion) + ";"\
+str(Validacion_Produccion) + ";"\
+str(N_Registro_Produccion) + ";"\
+str(Descripcion_Produccion) + ";"\
+str(Nombre_Produccion) + ";"\
+str(Informacion_Adicional_Produccion) + ";"\
+str(Autores_Produccion) + ";"\
+str(Col_Grupo_Codigo_GrupLAC) + ";"\
+ "\n")

    container = containers[doc_trab].findAll("tr")
    # containerb[27].findAll("img")
    #1=nombre 2=vinculacion 3=horas 4=ini-fin
    for x in range(1,len(container)):
        Tipo_Produccion="Documentos de trabajo"
        Validacion_Produccion="No"
        N_Registro_Produccion=""
        Descripcion_Produccion=""
        Nombre_Produccion=""    
        Informacion_Adicional_Produccion=""    
        Autores_Produccion=""
        
        containerb = container[x].findAll("td")
        
        if len(containerb[0])>2:
            Validacion_Produccion="Si"
        for y in range(0,len(containerb)):
            if len(containerb[y].text)>3:
                aux=containerb[y].text.replace(";","|").replace("ż", "").replace("Ż","¿").replace("ş","").replace("ń","ñ").replace("ŕ","r").replace("−","-").replace("Ń","Ñ").replace("Ň","Ñ").replace("ň","ñ").replace("ě","e")
                #for a in range(0,len(aux)):
                #    informacion= informacion + aux[a] + " "
                index1 = aux.find("Autores:")
                index2 = len(aux)
                informacion=aux[index1+8:index2].split()
                for a in range(0,len(informacion)):
                    Autores_Produccion= Autores_Produccion + informacion[a] + " "
                aux=aux[0:index1]

                index1 = aux.find(".-")
                index2 = len(aux)
                informacion=aux[0:index1].split()
                for a in range(0,len(informacion)):
                    N_Registro_Produccion= N_Registro_Produccion + informacion[a] + " "
                aux=aux[index1+2:index2]

                index1 = aux.find(":")
                index2 = len(aux)
                Descripcion_Produccion=aux[0:index1]
                aux=aux[index1+1:index2]

                index1 = aux.find("\n")
                index2 = len(aux)
                informacion=aux[0:index1].split()
                for a in range(0,len(informacion)):
                    Nombre_Produccion= Nombre_Produccion + informacion[a] + " "
                aux=aux[index1+1:index2]

                informacion=aux.split()
                for a in range(0,len(informacion)):
                    Informacion_Adicional_Produccion=Informacion_Adicional_Produccion + informacion[a] + " "
        
        Produccion.append(str(len(Produccion))+ ";"\
+str(Clasificacion_Produccion) + ";"\
+str(Tipo_Produccion) + ";"\
+str(Validacion_Produccion) + ";"\
+str(N_Registro_Produccion) + ";"\
+str(Descripcion_Produccion) + ";"\
+str(Nombre_Produccion) + ";"\
+str(Informacion_Adicional_Produccion) + ";"\
+str(Autores_Produccion) + ";"\
+str(Col_Grupo_Codigo_GrupLAC) + ";"\
+ "\n")