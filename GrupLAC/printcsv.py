import init

f = open ("./Resultados/Col_Grupo.csv", "w")
for item in init.Col_Grupo:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/Plan_Estrategico_Grupo.csv", "w")
for item in init.Plan_Estrategico:
	
    f.write(item)
    	
f.close()