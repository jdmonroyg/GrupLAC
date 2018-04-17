def instextract():
    from settings import my_url, name, director, RH, COD_GRUPO 
    import init
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    global continst
    continst=1
    idInstitucion=continst
	Nombre_Institucion=""
	Col_Grupo_Codigo_GrupLAC=str(RH)