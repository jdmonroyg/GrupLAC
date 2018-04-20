def tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion):
    from init import Produccion
    for x in range(1,len(container)):
        
        Validacion_Produccion="No"
        N_Registro_Produccion=""
        Descripcion_Produccion=""
        Nombre_Produccion=""    
        Informacion_Adicional_Produccion=""    
        Autores_Produccion=""
        
        containerb = container[x].findAll("td")
        
        if len(containerb[0])>2:
            Validacion_Produccion="Si"
        if len(containerb[1].text)>3:
            aux=containerb[1].text.replace(";","|").replace("ż", "¿").replace("Ż","¿").replace("ş"," ").replace("Ş"," ").replace("ń","ñ").replace("ŕ"," ").replace("−","-").replace("Ń","Ñ").replace("Ň","Ñ").replace("ň","ñ").replace("ě","e").replace('"'," ").replace("+","(simbolo más)")
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
            for b in range(0,len(informacion)):
                N_Registro_Produccion= N_Registro_Produccion + informacion[b] + " "
            aux=aux[index1+2:index2]

            index1 = aux.find(":")
            index2 = len(aux)
            informacion=aux[0:index1].split()
            for c in range(0,len(informacion)):
                Descripcion_Produccion= Descripcion_Produccion + informacion[c] + " "
            aux=aux[index1+1:index2]

            index1 = aux.find("\n")
            index2 = len(aux)
            informacion=aux[0:index1].split()
            for d in range(0,len(informacion)):
                Nombre_Produccion= Nombre_Produccion + informacion[d] + " "
            aux=aux[index1+1:index2]

            informacion=informacion=aux.split()
            for f in range(0,len(informacion)):
                Informacion_Adicional_Produccion=Informacion_Adicional_Produccion + informacion[f] + " "
        
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

def prodgrupextract():
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
    
    car_map_sim=0
    con_cie_tec_inf_tec=0
    dis_ind=0
    esq_tra_cir_int=0
    inn_pro_pro=0
    inn_gen_ges_emp=0
    nue_var_ani=0
    nue_var_veg=0
    plan_pilot=0
    otr_pro_tec=0
    prototipos=0
    reg_nor=0
    reg_tec=0
    gui_pra_cli=0
    pro_ley=0
    sig_dis=0
    softwar=0
    emp_bas_tec=0

    
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
            #otra clasificacion
            elif buscarinfo.td.string =="Cartas, mapas o similares":
                car_map_sim=a
            elif buscarinfo.td.string =="Consultorías científico tecnológicas e Informes técnicos":
                con_cie_tec_inf_tec=a
            elif buscarinfo.td.string =="Diseños industriales":
                dis_ind=a
            elif buscarinfo.td.string =="Esquemas de trazados de circuito integrado":
                esq_tra_cir_int=a
            elif buscarinfo.td.string =="Innovaciones en Procesos y Procedimientos":
                inn_pro_pro=a
            elif buscarinfo.td.string =="Innovaciones generadas en la Gestión Empresarial":
                inn_gen_ges_emp=a
            elif buscarinfo.td.string =="Nuevas variedades animal":
                nue_var_ani=a
            elif buscarinfo.td.string =="Nuevas variedades vegetal":
                nue_var_veg=a
            elif buscarinfo.td.string =="Plantas piloto":
                plan_pilot=a
            elif buscarinfo.td.string =="Otros productos tecnológicos":
                otr_pro_tec=a
            elif buscarinfo.td.string =="Prototipos":
                prototipos=a
            elif buscarinfo.td.string =="Regulaciones y Normas":
                reg_nor=a
            elif buscarinfo.td.string =="Reglamentos técnicos":
                reg_tec=a
            elif buscarinfo.td.string =="Guias de práctica clínica":
                gui_pra_cli=a
            elif buscarinfo.td.string =="Proyectos de ley":
                pro_ley=a
            elif buscarinfo.td.string =="Signos distintivos ":
                sig_dis=a
            elif buscarinfo.td.string =="Softwares":
                softwar=a
            elif buscarinfo.td.string =="Empresas de base tecnológica ":
                emp_bas_tec=a
                break

            
        except AttributeError:
            pass

    #extraccion tabla Articulos publicados
    container = containers[art_pub].findAll("tr")
    Tipo_Produccion="Artículos publicados"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    
    #extraccion tabla Articulos publicados
    container = containers[lib_pub].findAll("tr")
    Tipo_Produccion="Libros publicados"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    
    container = containers[cap_lib_pub].findAll("tr")
    Tipo_Produccion="Capítulos de libro publicados"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    
    container = containers[doc_trab].findAll("tr")
    Tipo_Produccion="Documentos de trabajo"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    
    container = containers[o_pub_div].findAll("tr")
    Tipo_Produccion="Otra publicación divulgativa"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    
    container = containers[o_art_pub].findAll("tr")
    Tipo_Produccion="Otros artículos publicados"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    
    container = containers[o_lib_pub].findAll("tr")
    Tipo_Produccion="Otros Libros publicados"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[trad].findAll("tr")
    Tipo_Produccion="Traducciones"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    Clasificacion_Produccion='PRODUCCIÓN TÉCNICA Y TECNOLÓGICA'

    container = containers[car_map_sim].findAll("tr")
    Tipo_Produccion="Cartas, mapas o similares"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[con_cie_tec_inf_tec].findAll("tr")
    Tipo_Produccion="Consultorías científico tecnológicas e Informes técnicos"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[dis_ind].findAll("tr")
    Tipo_Produccion="Diseños industriales"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    #pendiente
    container = containers[esq_tra_cir_int].findAll("tr")
    Tipo_Produccion="Esquemas de trazados de circuito integrado"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[inn_pro_pro].findAll("tr")
    Tipo_Produccion="Innovaciones en Procesos y Procedimientos"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[inn_gen_ges_emp].findAll("tr")
    Tipo_Produccion="Innovaciones generadas en la Gestión Empresarial"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    #pendiente
    container = containers[nue_var_ani].findAll("tr")
    Tipo_Produccion="Nuevas variedades animal"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    #pendiente
    container = containers[nue_var_veg].findAll("tr")
    Tipo_Produccion="Nuevas variedades vegetal"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[plan_pilot].findAll("tr")
    Tipo_Produccion="Plantas piloto"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[otr_pro_tec].findAll("tr")
    Tipo_Produccion="Otros productos tecnológicos"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[prototipos].findAll("tr")
    Tipo_Produccion="Prototipos"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[reg_nor].findAll("tr")
    Tipo_Produccion="Regulaciones y Normas"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[reg_tec].findAll("tr")
    Tipo_Produccion="Reglamentos técnicos"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    #pendiente
    #container = containers[gui_pra_cli].findAll("tr")
    #Tipo_Produccion="Guias de práctica clínica"
    #tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    #pendiente
    #container = containers[pro_ley].findAll("tr")
    #Tipo_Produccion="Proyectos de ley"
    #tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    #pendiente
    container = containers[sig_dis].findAll("tr")
    Tipo_Produccion="Signos distintivos"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[softwar].findAll("tr")
    Tipo_Produccion="Softwares"
    tablaextrat(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    
    """
    sig_dis=0
    softwares=0
    emp_bas_tec=0"""