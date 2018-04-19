def inicio():
	global Col_Grupo
	global Institucion
	global Produccion
	global Integrante
	global Sector	
	global Linea	
	global Plan_Estrategico
	
	#Tabla Col_Grupo
	Col_Grupo = ["Codig_GrupLAC;\
Nombre_Grupo;\
Ano_Mes_Formacion_Grupo;\
Departamento_Ciudad_Grupo;\
Lider_Grupo;\
Certificado_Grupo;\
Pagina_Web_Grupo;\
Email_Grupo;\
Clasificacion_Grupo;\
Area_Conocimiento_Grupo;\
Programa_Nacional_Cyt_Grupo;\
Programa_Nacional_Cyt_Sec_Grupo\n"]

	#Tabla Institucion
	Institucion = ["idInstitucion;\
Numero_Institucion;\
Nombre_Institucion;\
Col_Grupo_Codigo_GrupLAC\n"]

	#Tabla Produccion
	Produccion = ["idProduccion; \
Clasificacion_Produccion; \
Tipo_Produccion; \
Validacion_Produccion; \
N_Registro_Produccion; \
Descripcion_Produccion; \
Nombre_Produccion;\
Informacion_Adicional_Produccion;\
Autores_Produccion; \
Col_Grupo_Codigo_GrupLAC\n"]

	#Tabla Linea
	Linea = ["idLinea; \
Numero_Linea;\
Nombre_Linea; \
Col_Grupo_Codigo_GrupLAC\n"]
	
	#Tabla Sector
	Sector = ["idSector; \
Numero_Sector;\
Nombre_Sector; \
Col_Grupo_Codigo_GrupLAC\n"]

	#Tabla Integrante
	Integrante = ["idIntegrante; \
Numero_Integrante;\
Nombre_Integrante; \
Vinculacion_Integrante; \
Hora_Dedicacion_Integrante; \
Inicio_Vinculacion_Integrante; \
Fin_Vinculacion_Integrante; \
Col_Grupo_Codigo_GrupLAC\n"]
	
	Plan_Estrategico = ["idPlan;\
Col_Grupo_Codigo_GrupLAC;\
Pe_Ptrabajo_Grupo;\
Pe_Earte_Grupo;\
Pe_Objetivos_Grupo;\
Pe_Retos_Grupo;\
Pe_Vision_Grupo\n"]