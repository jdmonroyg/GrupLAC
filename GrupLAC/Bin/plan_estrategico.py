def pegrupextract():
    from settings import my_url, name, director, RH, containers
    from init import Plan_Estrategico
    import re
    global contpegrup
    all2 = 0
    
    #inicializo los campos de grupo
    
    Plan_Estrategico_Grupo=""
    idPlan= ""
    Pe_Ptrabajo_Grupo=""
    Pe_Earte_Grupo=""
    Pe_Objetivos_Grupo=""
    Pe_Retos_Grupo=""
    Pe_Vision_Grupo=""

    for a in range(0,len(containers)):
        buscarinfo = containers[a]
        #print(buscareconocimientos)
        try:
            if buscarinfo.td.string == "Plan Estratégico":
                all2 = a
                break
        except AttributeError:
            pass
    #extraccion tabla Datos Basicos
    
    container = containers[all2].findAll("td")
    for x in range(0,len(container)-1):
        cont = container[x]
        if cont.string == "Plan Estratégico":
            Plan_Estrategico_Grupo= container[x+1].text.strip().replace("\n","").replace("\r\n\r\n","").replace("\r\n","").replace("\r","").replace("\r\r","").replace("ˇ"," ").replace(";","|").replace("ń","ñ").replace('"',"").replace("'","").replace("ż","¿")


    #Depurando tabla Plan Estrategico Grupo
    #Vision
    index1 = Plan_Estrategico_Grupo.find("Visión:")
    index2 = len(Plan_Estrategico_Grupo)
    Pe_Vision_Grupo=Plan_Estrategico_Grupo[index1+7:index2].replace(";",",")
    Plan_Estrategico_Grupo=Plan_Estrategico_Grupo[0:index1]
    #Retos
    index1 = Plan_Estrategico_Grupo.find("Retos:")
    index2 = len(Plan_Estrategico_Grupo)
    Pe_Retos_Grupo=Plan_Estrategico_Grupo[index1+6:index2].replace(";",",")
    Plan_Estrategico_Grupo=Plan_Estrategico_Grupo[0:index1]
    #Objetivos
    index1 = Plan_Estrategico_Grupo.find("Objetivos:")
    index2 = len(Plan_Estrategico_Grupo)
    Pe_Objetivos_Grupo=Plan_Estrategico_Grupo[index1+10:index2].replace(";",",")
    Plan_Estrategico_Grupo=Plan_Estrategico_Grupo[0:index1]
    #Estado del arte
    index1 = Plan_Estrategico_Grupo.find("Estado del arte:")
    index2 = len(Plan_Estrategico_Grupo)
    Pe_Earte_Grupo=Plan_Estrategico_Grupo[index1+16:index2].replace(";",",")
    Plan_Estrategico_Grupo=Plan_Estrategico_Grupo[0:index1]
    #Plan de trabajo
    index1 = Plan_Estrategico_Grupo.find("Plan de trabajo:")
    index2 = len(Plan_Estrategico_Grupo)
    Pe_Ptrabajo_Grupo=Plan_Estrategico_Grupo[index1+16:index2].replace(";",",")
    
    #Pe_Ptrabajo_Grupo="aa"
    #Pe_Earte_Grupo="aa"
    #Pe_Objetivos_Grupo="aa"
    #Pe_Retos_Grupo="aa"
    #Pe_Vision_Grupo="aa"
    
    Plan_Estrategico.append(str(len(Plan_Estrategico))+ ";"\
+RH + ";"\
+str(Pe_Ptrabajo_Grupo) + ";"\
+str(Pe_Earte_Grupo) + ";"\
+str(Pe_Objetivos_Grupo) + ";"\
+str(Pe_Retos_Grupo) + ";"\
+str(Pe_Vision_Grupo)+";"\
+ "\n")
    #print (init.Col_Grupo)
    #print (Plan_Estrategico)
    #COD_PLAN=COD_PLAN+1
    #contpegrup = [COD_PLAN]