
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "http://scienti.colciencias.gov.co:8085/gruplac/jsp/visualiza/visualizagr.jsp?nro=00000000000422"

uClient = uReq(my_url)
page_html = uClient.read() 
uClient.close()

page_soup = soup(page_html,"html.parser") #convierte a codigo html
containers = page_soup.findAll("table")

all = 0
all2 = 2
a = 0
x = 0
y = 0
name="Quimica"
#identacion corrida para probar en consola
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
container = containers[all].findAll("tr")
containerb = containers[all].findAll("a")
for x in range(0, len(container)-1):
    #td class="celdasTitulo"
    cont = container[x]
    #info_reconocimientos = cont.text
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
Col_Grupo.append(RH + ";"\
+name + ";"\
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
+str("aaa") + ";"\
+ "\n")




aux=containerb[1].text.replace(";","|").replace("ż", "¿").replace("Ż","¿").replace("ş"," ").replace("ń","ñ").replace("ŕ"," ").replace("−","-").replace("Ń","Ñ").replace("Ň","Ñ").replace("ň","ñ").replace("ě","e")
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

informacion=aux.split()
for f in range(0,len(informacion)):
    Informacion_Adicional_Produccion=Informacion_Adicional_Produccion + informacion[f] + " "