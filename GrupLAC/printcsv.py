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
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/Institucion_Grupo.csv", "w")
for item in init.Institucion:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/Linea_Grupo.csv", "w")
for item in init.Linea:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/Sector_Grupo.csv", "w")
for item in init.Sector:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/Integrante_Grupo.csv", "w")
for item in init.Integrante:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/Produccion_Grupo.csv", "w")
for item in init.Produccion:
    #try:
    f.write(item)
    #except UnicodeEncodeError:
       #pass
f.close()