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
            Plan_Estrategico_Grupo= container[x+1].text.strip().replace("\n","")\
.replace("\r\n\r\n","").replace("\r\n","").replace("\r","").replace("\r\r","")\
.replace(";","|").replace("ż", "¿").replace("Ż","¿").replace("ş"," ")\
.replace("Ş"," ").replace("ń","ñ").replace("ŕ","á").replace("−","-").replace("Ń","Ñ").replace("Ň","Ó")\
.replace("ň","ó").replace('"'," ").replace("ă","ó").replace("Ă","ó").replace("ˇ"," ").replace("³","")\
.replace("Č","É").replace("Ě","Í").replace("Ŕ","Á").replace("Ő","Õ").replace("č","è").replace("ě","ì")\
.replace("ł","").replace("ﬁ","fi").replace("\u200b","").replace("\u0104","¡").replace("a"+"\u0301","á")\
.replace("e"+"\u0301","é").replace("i"+"\u0301","í").replace("o"+"\u0301","ó").replace("u"+"\u0301","ú")\
.replace("\u0119","e").replace("\u03b3","(gamma)").replace("\u03b2","(beta)").replace("́ı","í").replace("μ","(mi)")\
.replace("˜","").replace("\uf062","").replace("\uf061","").replace("Ť","<<").replace("ť",">>").replace("α","(alfa)")\
.replace("\u010f","í").replace("\u013e","í").replace("\u0131","í").replace("\uf0a7","").replace("ů","ú")\
.replace("A"+"\u0301","Á").replace("E"+"\u0301","É").replace("I"+"\u0301","Í").replace("O"+"\u0301","Í")\
.replace("U"+"\u0301","Ú").replace("n"+"\u0303","ñ").replace("\x98","").replace("\u0301"+"e","é")\
.replace("aspx"+"\u0301","?")
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