ramos = open("PARSEAR.py", "r")
prejson = dict()
problemas = ["direccion de estudio","ingeniería química y ambiental", "obras civiles", "ingeniería comercial", "estudios humanisticos", "ingeniería eléctrica", "ingeniería mecánica", "ingeniería metlúrgica y de materiales", "ingeniería en diseño", "direccion gral. docencia"]
for i in ramos:
	i = i.strip().split(" ")
	listtotal=list()
	for k in i:
		k = k.strip().split("\t")
		for j in k:
			listtotal.append(j.strip())
	i = listtotal
	if i[0][0].isalpha():
		actualramo = i[0].strip()
		if i[0].strip() not in prejson:
			prejson[i[0]] = list()
		a = 1
		linea = ""
		while (i[a].strip()[0].isalpha()):
			linea += i[a] + " "
			a += 1
		nombreramo = linea
		linea = ""
		flag = 0
		while(i[a] != "Ver"):
			if(i[a].isdigit() and flag == 0):
				linea += i[a]+"#"
				flag += 1
			elif(i[a].isdigit()):
				linea += "#" + i[a]
			else:
				linea += i[a] + " "
			a += 1
		linea = linea.strip()
		profe = linea
		prejson[i[0]].append((nombreramo, profe))
	else:
		c, d = prejson[actualramo][-1]
		flag = 0
		a = 0
		linea = ""
		while (i[a] != "Ver"):
			if (i[a].isdigit() and flag == 0):
				linea += "#" + i[a] + "#"
				flag += 1
			elif(i[a].isdigit()):
				linea += "#" + i[a]
			else:
				linea += i[a]+" "
			a+=1
		d+=linea
		prejson[actualramo][-1] = (c,d)
ramos.close()
for i in prejson:
	actual = prejson[i]
	nombre = actual[0][0].strip()
	profes = actual[0][1].strip().split("#")
	profes = list(map(str.strip, profes))
	lista=list()
	j = 0
	while(j < len(profes) - 2):
		tupla = tuple(profes[j: j+3])
		j+=3
		lista.append(tupla)
	prejson[i] = (nombre, lista)

json = list()
a = 1
deptos = {"IAO MRA ARQ":"ARQUITECTURA", "EFI":"DEFIDER", "BIE CERT PRE REE":"DIRECCION DE ESTUDIO", 
"IWG LASPAU":"DIRECCION GRAL. DOCENCIA", "IPD TEL ELO":"ELECTRONICA", 
"HIW HRW HFW HAH HTW HCW HAF":"ESTUDIOS HUMANISTICOS", "AYF FIS LAB":"FISICA",
"ICN PII IWN ILN III":"INDUSTRIAS", "INF IWI ILI ICI":"INFORMATICA", 
"ICS ICVESP":"INGENIERÍA COMERCIAL", "ELI":"INGENIERÍA ELÉCTRICA", "ICM IWM MEC ILM ICM IMM":"INGENIERÍA MECÁNICA",
"IWC MIN MET ILC":"INGENIERÍA METALÚRGICA Y DE MATERIALES",
"IWQ ICQ IQA ILQ IMQ IPQ":"INGENIERÍA QUIMICA Y AMBIENTAL",
"IDP":"Ingeniería en Diseño", "MAT MATE":"MATEMATICA", "CON CIV IPO":"OBRAS CIVILES",
"QUI AYQ":"QUIMICA", "ACTPPI":"V.R.A."}
for i in prejson:
	flag = 1
	actualramo = {"id":0, "sigla":0, "asignatura":0, "departamento":0,"paralelos":0, "semestre":1 }
	actualramo["id"]=a
	actualramo["sigla"]=i
	ramo = prejson[i][0]
	flag2 = 1
	for k in problemas:

		if k.lower() in ramo.lower():
			ramo = ramo.lower().replace(k.lower(), "", 1)
			flag2 = 0
	if flag2:
		ramo = " ".join(ramo.split(" ")[0:-1])
	ramo = ramo.lower().split(" ")
	for j in range(0,len(ramo)):
		if len(ramo[j])>1:
			if ramo[j][0] == ramo[j][1] or ramo[j][1] == ".":
				ramo[j] = ramo[j].upper()
			else:
				ramo[j] = ramo[j].capitalize()
		else:
			ramo[j] = ramo[j].capitalize()
	ramo = (" ".join(ramo)).strip()
	actualramo["asignatura"] = ramo
	for j in deptos:
		if i[0:3] in j:
			d = deptos[j]
			d = d.split(" ")
			d = list(map(str.capitalize, d))
			d = " ".join(d)
			if d.lower()== "v.r.a.":
				d = "V.R.A."
			d = d.strip()
			actualramo["departamento"]=d
			break
	lista=[]
	for paralelonum,nombreprofe,cupos in prejson[i][1]:
		try:
			paralelonum = int(paralelonum)
			cupos = int(cupos)
		except:
			flag = 0
		nombreprofe = nombreprofe.split(" ")
		nombreprofe = list(map(str.capitalize, nombreprofe))
		nombreprofe = " ".join(nombreprofe)
		if nombreprofe.lower() == "nn":
			nombreprofe = "NN"
		profe = {"id":paralelonum, "profesor":nombreprofe, "cupos":cupos}
		lista.append(profe)
	actualramo["paralelos"]=lista

	#"paralelos": [{ "id": 1, "profesor": 'profe1', "cupos": 20},  { "id": 2, "profesor": 'profe2', "cupos": 30}]
	a+=1
	if(flag == 0):
		continue
	json.append(actualramo)
archivo = open("final.txt", "w")
archivo.write("const CURSOS_LIST = ["+"\n")
for i in json:
	if i!=json[-1]:
		archivo.write(str(i)+',\n')
	else:
		archivo.write(str(i)+'\n')
archivo.write("];")
archivo.close()