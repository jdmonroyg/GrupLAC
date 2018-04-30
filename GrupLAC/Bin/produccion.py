def tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion):
    from init import Produccion
    aux=1
    #la tabla guias y proyectos tiene un tr fantasma
    if Tipo_Produccion == "Guias de práctica clínica" or Tipo_Produccion=="Proyectos de ley":
        aux=2
    for x in range(aux,len(container)):
        
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
            aux=containerb[1].text.replace(";","|").replace("ż", "¿").replace("Ż","¿").replace("ş"," ")\
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
            
            if Tipo_Produccion=="Signos distintivos" or Tipo_Produccion=="Proyectos" :
                Autores_Produccion="No aplica"

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

    ediciones=0
    even_cient=0
    infor_invest=0
    redes_conoci_especia=0
    genera_conte_impre=0
    genera_conte_multi=0
    genera_conte_virt=0
    estrat_comun_conoci=0
    estrat_pedag_fomen_cti=0
    espa_partici_ciuda=0
    part_ciuda_proye_cti=0
    produc_arte_arqui_dise=0

    
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
            ############################################################
            #otra clasificacion
            ############################################################
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
            elif buscarinfo.td.string =="Softwares ":
                softwar=a
            elif buscarinfo.td.string =="Empresas de base tecnológica ":
                emp_bas_tec=a
            ############################################################
            #otra clasificacion
            ############################################################
            elif buscarinfo.td.string =="Ediciones":
                ediciones=a
            elif buscarinfo.td.string =="Eventos Científicos":
                even_cient=a
            elif buscarinfo.td.string =="Informes de investigación":
                infor_invest=a
            elif buscarinfo.td.string =="Redes de Conocimiento Especializado":
                redes_conoci_especia=a
            elif buscarinfo.td.string =="Generación de Contenido Impreso":
                genera_conte_impre=a
            elif buscarinfo.td.string =="Generación de Contenido Multimedia":
                genera_conte_multi=a
            elif buscarinfo.td.string =="Generación de Contenido Virtual":
                genera_conte_virt=a
            elif buscarinfo.td.string =="Estrategias de Comunicación del Conocimiento":
                estrat_comun_conoci=a
            elif buscarinfo.td.string =="Estrategias Pedagógicas para el fomento a la CTI":
                estrat_pedag_fomen_cti=a
            elif buscarinfo.td.string =="Espacios de Participación Ciudadana":
                espa_partici_ciuda=a
            elif buscarinfo.td.string =="Participación Ciudadana en Proyectos de CTI":
                part_ciuda_proye_cti=a
            elif buscarinfo.td.string =="Producción en arte, arquitectura y diseño":
                produc_arte_arqui_dise=a
            #################################
            #otra clasificacion
            #################################
            elif buscarinfo.td.string =="Asesorías al Programa Ondas":
                asesor_program_onda=a
            elif buscarinfo.td.string =="Curso de Corta Duración Dictados":
                curs_cort_duracion_dictado=a
            elif buscarinfo.td.string =="Trabajos dirigidos/turorías":
                trabajo_dirigido_tutoria=a
            #################################
            #otra clasificacion
            #################################
            elif buscarinfo.td.string =="Jurado/Comisiones evaluadoras de trabajo de grado":
                jurado_comision_evaluador_trabajo_grado=a
            elif buscarinfo.td.string =="Participación en comités de evaluación":
                participacion_comite_evaluacion=a
            elif buscarinfo.td.string =="Demás trabajos":
                demas_trabajo=a
            elif buscarinfo.td.string =="Proyectos":
                proyectos=a

            
        except AttributeError:
            pass

    #extraccion tabla Articulos publicados
    container = containers[art_pub].findAll("tr")
    Tipo_Produccion="Artículos publicados"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    
    #extraccion tabla Articulos publicados
    container = containers[lib_pub].findAll("tr")
    Tipo_Produccion="Libros publicados"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    
    container = containers[cap_lib_pub].findAll("tr")
    Tipo_Produccion="Capítulos de libro publicados"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    
    container = containers[doc_trab].findAll("tr")
    Tipo_Produccion="Documentos de trabajo"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    
    container = containers[o_pub_div].findAll("tr")
    Tipo_Produccion="Otra publicación divulgativa"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    
    container = containers[o_art_pub].findAll("tr")
    Tipo_Produccion="Otros artículos publicados"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    
    container = containers[o_lib_pub].findAll("tr")
    Tipo_Produccion="Otros Libros publicados"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[trad].findAll("tr")
    Tipo_Produccion="Traducciones"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    ############################################################

    Clasificacion_Produccion='PRODUCCIÓN TÉCNICA Y TECNOLÓGICA'

    ############################################################

    container = containers[car_map_sim].findAll("tr")
    Tipo_Produccion="Cartas, mapas o similares"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[con_cie_tec_inf_tec].findAll("tr")
    Tipo_Produccion="Consultorías científico tecnológicas e Informes técnicos"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[dis_ind].findAll("tr")
    Tipo_Produccion="Diseños industriales"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    #pendiente
    container = containers[esq_tra_cir_int].findAll("tr")
    Tipo_Produccion="Esquemas de trazados de circuito integrado"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[inn_pro_pro].findAll("tr")
    Tipo_Produccion="Innovaciones en Procesos y Procedimientos"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[inn_gen_ges_emp].findAll("tr")
    Tipo_Produccion="Innovaciones generadas en la Gestión Empresarial"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    #pendiente
    container = containers[nue_var_ani].findAll("tr")
    Tipo_Produccion="Nuevas variedades animal"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    #pendiente
    container = containers[nue_var_veg].findAll("tr")
    Tipo_Produccion="Nuevas variedades vegetal"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[plan_pilot].findAll("tr")
    Tipo_Produccion="Plantas piloto"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[otr_pro_tec].findAll("tr")
    Tipo_Produccion="Otros productos tecnológicos"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[prototipos].findAll("tr")
    Tipo_Produccion="Prototipos"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[reg_nor].findAll("tr")
    Tipo_Produccion="Regulaciones y Normas"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[reg_tec].findAll("tr")
    Tipo_Produccion="Reglamentos técnicos"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    #pendiente
    container = containers[gui_pra_cli].findAll("tr")
    Tipo_Produccion="Guias de práctica clínica"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    #pendiente
    container = containers[pro_ley].findAll("tr")
    Tipo_Produccion="Proyectos de ley"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    
    container = containers[sig_dis].findAll("tr")
    Tipo_Produccion="Signos distintivos"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[softwar].findAll("tr")
    Tipo_Produccion="Softwares"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[emp_bas_tec].findAll("tr")
    Tipo_Produccion="Empresas de base tecnológica"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    
    
    ############################################################

    Clasificacion_Produccion='APROPIACIÓN SOCIAL Y CIRCULACIÓN DEL CONOCIMIENTO'

    ############################################################

    container = containers[ediciones].findAll("tr")
    Tipo_Produccion="Ediciones"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    #diferente extraccion
    container = containers[even_cient].findAll("tr")
    Tipo_Produccion="Eventos Científicos"
    tablaeventcientiextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[infor_invest].findAll("tr")
    Tipo_Produccion="Informes de investigación"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    #diferente extraccion
    container = containers[redes_conoci_especia].findAll("tr")
    Tipo_Produccion="Redes de Conocimiento Especializado"
    tablaredesconociespeciextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[genera_conte_impre].findAll("tr")
    Tipo_Produccion="Generación de Contenido Impreso"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[genera_conte_multi].findAll("tr")
    Tipo_Produccion="Generación de Contenido Multimedia"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[genera_conte_virt].findAll("tr")
    Tipo_Produccion="Generación de Contenido Virtual"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[estrat_comun_conoci].findAll("tr")
    Tipo_Produccion="Estrategias de Comunicación del Conocimiento"
    tablaestrategiasextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[estrat_pedag_fomen_cti].findAll("tr")
    Tipo_Produccion="Estrategias Pedagógicas para el fomento a la CTI"
    tablaestrategiasextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    
    container = containers[espa_partici_ciuda].findAll("tr")
    Tipo_Produccion="Espacios de Participación Ciudadana"
    tablaespaciosparticipaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[part_ciuda_proye_cti].findAll("tr")
    Tipo_Produccion="Participación Ciudadana en Proyectos de CTI"
    tablaestrategiasextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    #pendiente
    Tipo_Produccion="Obras o productos"
    tablaproduccionaadextract(produc_arte_arqui_dise,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)


    ####################################################################
    
    Clasificacion_Produccion='ACTIVIDADES DE FORMACIÓN'

    ####################################################################
    container = containers[asesor_program_onda].findAll("tr")
    Tipo_Produccion="Asesorías al Programa Ondas"
    tablaespaciosparticipaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[curs_cort_duracion_dictado].findAll("tr")
    Tipo_Produccion="Curso de Corta Duración Dictados"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[trabajo_dirigido_tutoria].findAll("tr")
    Tipo_Produccion="Trabajos dirigidos/turorías"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)
    

    ####################################################################
    
    Clasificacion_Produccion='ACTIVIDADES COMO EVALUADOR'
    
    ####################################################################
    container = containers[jurado_comision_evaluador_trabajo_grado].findAll("tr")
    Tipo_Produccion="Jurado/Comisiones evaluadoras de trabajo de grado"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[participacion_comite_evaluacion].findAll("tr")
    Tipo_Produccion="Participación en comités de evaluación"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[demas_trabajo].findAll("tr")
    Tipo_Produccion="Demás trabajos"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)

    container = containers[proyectos].findAll("tr")
    Tipo_Produccion="Proyectos"
    tablaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion)



def tablaeventcientiextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion):
    from init import Produccion
    aux=1
    
    for x in range(aux,len(container)):
        
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
            aux=containerb[1].text.replace(";","|").replace("ż", "¿").replace("Ż","¿").replace("ş"," ")\
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
            #for a in range(0,len(aux)):
            #    informacion= informacion + aux[a] + " "
            index1 = aux.find("Instituciones asociadas")
            index2 = len(aux)
            informacion=aux[index1+23:index2].split()
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
            
            #if Tipo_Produccion=="Signos distintivos":
            #    Autores_Produccion="No aplica"

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

def tablaredesconociespeciextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion):
    from init import Produccion
    aux=1
    
    for x in range(aux,len(container)):
        
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
            aux=containerb[1].text.replace(";","|").replace("ż", "¿").replace("Ż","¿").replace("ş"," ")\
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
            #for a in range(0,len(aux)):
            #    informacion= informacion + aux[a] + " "
            index1 = aux.find("Número de participantes:")
            index2 = len(aux)
            informacion=aux[index1:index2].split()
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
            
            #if Tipo_Produccion=="Signos distintivos":
            #    Autores_Produccion="No aplica"

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

def tablaestrategiasextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion):
    from init import Produccion
    aux=1
    
    for x in range(aux,len(container)):
        
        Validacion_Produccion="No"
        N_Registro_Produccion=""
        Descripcion_Produccion=""
        Nombre_Produccion=""    
        Informacion_Adicional_Produccion=""    
        Autores_Produccion="No aplica"
        
        containerb = container[x].findAll("td")
        
        if len(containerb[0])>2:
            Validacion_Produccion="Si"
        if len(containerb[1].text)>3:
            aux=containerb[1].text.replace(";","|").replace("ż", "¿").replace("Ż","¿").replace("ş"," ")\
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
            #for a in range(0,len(aux)):
            #    informacion= informacion + aux[a] + " "
            index1 = aux.find("Descripción:")
            index2 = len(aux)
            informacion=aux[index1:index2].split()
            for a in range(0,len(informacion)):
                Informacion_Adicional_Produccion= Informacion_Adicional_Produccion + informacion[a] + " "
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


            informacion=informacion=aux.split()
            for f in range(0,len(informacion)):
                Nombre_Produccion=Nombre_Produccion + informacion[f] + " "
            

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

def tablaespaciosparticipaextract(container,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion):
    from init import Produccion
    aux=1
    
    for x in range(aux,len(container)):
        
        Validacion_Produccion="No"
        N_Registro_Produccion=""
        Descripcion_Produccion=""
        Nombre_Produccion=""    
        Informacion_Adicional_Produccion=""    
        Autores_Produccion="No aplica"
        
        containerb = container[x].findAll("td")
        
        if len(containerb[0])>2:
            Validacion_Produccion="Si"
        if len(containerb[1].text)>3:
            aux=containerb[1].text.replace(";","|").replace("ż", "¿").replace("Ż","¿").replace("ş"," ")\
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

            #for a in range(0,len(aux)):
            #    informacion= informacion + aux[a] + " "
            index1 = aux.find("Número de participantes:")
            index2 = len(aux)
            informacion=aux[index1:index2].split()
            for a in range(0,len(informacion)):
                Autores_Produccion= Autores_Produccion + informacion[a] + " "
            aux=aux[0:index1]

            index1 = aux.find(".-")
            index2 = len(aux)
            informacion=aux[0:index1].split()
            for b in range(0,len(informacion)):
                N_Registro_Produccion= N_Registro_Produccion + informacion[b] + " "
            aux=aux[index1+2:index2]

            index1 = aux.find("en")
            index2 = len(aux)
            informacion=aux[0:index1].split()
            for c in range(0,len(informacion)):
                Descripcion_Produccion= Descripcion_Produccion + informacion[c] + " "
            aux=aux[index1:index2]

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


def tablaproduccionaadextract(produc_arte_arqui_dise,Clasificacion_Produccion,Col_Grupo_Codigo_GrupLAC,Tipo_Produccion):
    from init import Produccion
    from settings import containers2
    container = containers2[produc_arte_arqui_dise].findAll("tr")
    iterador=1
    contador=0
    for x in range(iterador,len(container)):
        if container[x].td.string == "Obras o productos":
            Tipo_Produccion= "Obras o productos"
            contador=1
            continue
        elif container[x].td.string == "Industrias creativas y culturales":
            Tipo_Produccion= "Industrias creativas y culturales"
            contador=1
            continue
        elif container[x].td.string == "Eventos Artísticos":
            Tipo_Produccion= "Eventos Artísticos"
            contador=1
            continue
        elif container[x].td.string == "Talleres de Creación":
            Tipo_Produccion= "Talleres de Creación"
            contador=1
            continue
        
        Validacion_Produccion="No"
        N_Registro_Produccion=""
        Descripcion_Produccion=""
        Nombre_Produccion=""    
        Informacion_Adicional_Produccion=""    
        Autores_Produccion="no aplica"
        
        containerb = container[x].findAll("td")
        if len(containerb[0])>2:
            Validacion_Produccion="Si"
        if len(containerb[1].text)>3:
            aux=containerb[1].text.replace(";","|").replace("ż", "¿").replace("Ż","¿").replace("ş"," ")\
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
            N_Registro_Produccion=contador
            Autores_Produccion="no aplica"
            contador =contador + 1

            index1 = aux.find(":")
            index3 =len(aux)
            informacion=aux[0:index1].split()
            for a in range(0,len(informacion)):
                Descripcion_Produccion= Descripcion_Produccion + informacion[a] + " "
            aux=aux[index1+1:index3]
            
            index2 = aux.find("\n")
            informacion=aux[0:index1].split()
            for c in range(0,len(informacion)):
                Nombre_Produccion= Nombre_Produccion + informacion[c] + " "
            aux=aux[index2:index3]

            informacion=aux.split()
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
