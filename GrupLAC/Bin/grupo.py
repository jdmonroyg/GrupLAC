

    
def infogrupextract():
    from settings import my_url, name, director, RH, containers
    from init import Col_Grupo
    #from urllib.request import urlopen as uReq
    #from bs4 import BeautifulSoup as soup
    global continfo

    #uClient = uReq(my_url)
    #page_html = uClient.read() 
    #uClient.close()
    all = 0
    all2 = 0
    
    #inicializo los campos de grupo
    
    Ano_Mes_Formacion_Grupo=""
    Departamento_Ciudad_Grupo=""
    Lider_Grupo=""
    Certificado_Grupo=""
    Pagina_Web_Grupo=""
    Email_Grupo=""
    Clasificacion_Grupo=""
    Area_Conocimiento_Grupo=""
    Programa_Nacional_Cyt_Grupo=""
    Programa_Nacional_Cyt_Sec_Grupo=""

    for a in range(0,len(containers)):
        buscarinfo = containers[a]
        #print(buscareconocimientos)
        try:
            if buscarinfo.td.string == "Plan Estratégico":
                all2 = a
                break

            elif buscarinfo.td.string == "Datos básicos":
                all = a
                #print(all)
        except AttributeError:
            pass
    #extraccion tabla Datos Basicos
    container = containers[all].findAll("td")
    containerb = containers[all].findAll("a")
    for x in range(0, len(container)-1):
        cont = container[x]
        if cont.string == "Año y mes de formación":
            Ano_Mes_Formacion_Grupo= container[x+1].string.strip()
        elif cont.string == "Departamento - Ciudad":
            Departamento_Ciudad_Grupo= container[x+1].string.strip()
        elif cont.string == "Líder":
            Lider_Grupo= container[x+1].string.strip()
        elif cont.string == "¿La información de este grupo se ha certificado? ":
            Certificado_Grupo= container[x+1].string.strip()
        elif cont.string == "Página web":
            Pagina_Web_Grupo= containerb[0].string.strip()
        elif cont.string == "E-mail":
            Email_Grupo= containerb[1].string.strip()
        elif cont.string == "Clasificación":
            aux= container[x+1].text.strip().replace("\n","").split()
            for x in range(0,len(aux)):
                Clasificacion_Grupo= Clasificacion_Grupo + aux[x] + " " 
        elif cont.string == "Área de conocimiento":
            Area_Conocimiento_Grupo= container[x+1].string.strip()
        elif cont.string == "Programa nacional de ciencia y tecnología":
            Programa_Nacional_Cyt_Grupo= container[x+1].string.strip()
        elif cont.string == "Programa nacional de ciencia y tecnología (secundario)":
            Programa_Nacional_Cyt_Sec_Grupo= container[x+1].string.strip()
    
    
    
    Col_Grupo.append(RH+ ";"\
+name+ ";"\
+str(Ano_Mes_Formacion_Grupo)+ ";"\
+str(Departamento_Ciudad_Grupo)+ ";"\
+str(Lider_Grupo)+ ";"\
+str(Certificado_Grupo)+ ";"\
+str(Pagina_Web_Grupo)+ ";"\
+str(Email_Grupo)+ ";"\
+str(Clasificacion_Grupo)+ ";"\
+str(Area_Conocimiento_Grupo)+ ";"\
+str(Programa_Nacional_Cyt_Grupo)+ ";"\
+str(Programa_Nacional_Cyt_Sec_Grupo)+ ";"\
#+str(Pe_Ptrabajo_Grupo) + ";"\
#+str(Pe_Earte_Grupo) + ";"\
#+str(Pe_Objetivos_Grupo) + ";"\
#+str(Pe_Retos_Grupo) + ";"\
#+str(Pe_Vision_Grupo)+";"\
+ "\n")
    #print (init.Col_Grupo)
    
