from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template("Index.html")

@app.route('/pag1')
def pag1():
    return render_template("Info.html")



@app.route('/personal')
def personal():
    return render_template("personal.html")

#area
@app.route('/formularioarea')
def formularioarea():
    return render_template("formularioarea.html")

@app.route('/area')
def area():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select idarea, descripcion from area order by idarea')
    datos = cursor.fetchall()
    return render_template("area.html", descripcion=datos)

@app.route('/editararea/<string:id>')
def editararea(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh',)
    cursor = conn.cursor()
    cursor.execute('select idarea, descripcion from area where idarea = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editararea.html", comentar=dato[0])

@app.route('/editar_area/<string:idarea>',methods=['POST'])
def editar_area(idarea):
    if request.method == 'POST':
        corr=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('update area set descripcion=%s where idarea=%s', (corr,idarea))
        conn.commit()
    return redirect(url_for('area'))

@app.route('/borrararea/<string:id>')
def borrararea(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('delete from area where idarea = {0}'.format(id))
    conn.commit()
    return redirect(url_for('area'))


@app.route('/agrega_area', methods=['POST'])
def agrega_area():
    if request.method == 'POST':
        aux_Descripcion = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('insert into area (descripcion) values (%s)',(aux_Descripcion))
        conn.commit()
    return redirect(url_for('area'))

#escolaridad

@app.route('/formularioescolaridad')
def formularioescolaridad():
    return render_template("formularioescolaridad.html")

@app.route('/escolaridad')
def escolaridad():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select idescolaridad, descripcionescolaridad from escolaridad order by idescolaridad')
    datos = cursor.fetchall()
    return render_template("escolaridad.html", descripcionescolaridad=datos)

@app.route('/editarescolaridad/<string:id>')
def editarescolaridad(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh',)
    cursor = conn.cursor()
    cursor.execute('select idescolaridad, descripcionescolaridad from escolaridad where idescolaridad = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editarescolaridad.html", comentar=dato[0])

@app.route('/editar_escolaridad/<string:idescolaridad>',methods=['POST'])
def editar_escolaridad(id):
    if request.method == 'POST':
        corr1=request.form['descripcionescolaridad']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('update escolaridad set descripcionescolaridad=%s where idescolaridad=%s', (corr1,idarea))
        conn.commit()
    return redirect(url_for('escolaridad'))

@app.route('/borrarescolaridad/<string:id>')
def borrarescolaridad(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('delete from escolaridad where idescolaridad = {0}'.format(id))
    conn.commit()
    return redirect(url_for('escolaridad'))


@app.route('/agrega_escolaridad', methods=['POST'])
def agrega_escolaridad():
    if request.method == 'POST':
        aux_Descripcionescolaridad = request.form['descripcionescolaridad']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('insert into escolaridad (descripcionescolaridad) values (%s)',(aux_Descripcionescolaridad))
        conn.commit()
    return redirect(url_for('escolaridad'))

#Estado Civil

@app.route('/formularioestadocivil')
def formularioestadocivil():
    return render_template("formularioestadocivil.html")

@app.route('/estadocivil')
def estadocivil():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select idestadocivil, descripcionestadocivil from estadocivil order by idestadocivil')
    datos = cursor.fetchall()
    return render_template("estadocivil.html", descripcionestadocivil=datos)

@app.route('/editarestadocivil/<string:id>')
def editarestadocivil(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh',)
    cursor = conn.cursor()
    cursor.execute('select idestadocivil, descripcionestadocivil from estadocivil where idestadocivil = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editarestadocivil.html", comentar=dato[0])

@app.route('/editar_estadocivil/<string:idestadocivil>',methods=['POST'])
def editar_estadocivil(idestadocivil):
    if request.method == 'POST':
        corr1=request.form['descripcionestadocivil']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('update estadocivil set descripcionestadocivil=%s where idestadocivil=%s', (corr1,idestadocivil))
        conn.commit()
    return redirect(url_for('estadocivil'))

@app.route('/borrarestadocivil/<string:id>')
def borrarestadocivil(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('delete from estadocivil where idestadocivil = {0}'.format(id))
    conn.commit()
    return redirect(url_for('estadocivil'))


@app.route('/agrega_estadocivil', methods=['POST'])
def agrega_estadocivil():
    if request.method == 'POST':
        aux_Descripcionestadocivil = request.form['descripcionestadocivil']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('insert into estadocivil (descripcionestadocivil) values (%s)',(aux_Descripcionestadocivil))
        conn.commit()
    return redirect(url_for('estadocivil'))

#Grado

@app.route('/formulariogrado')
def formulariogrado():
    return render_template("formulariogrado.html")

@app.route('/grado')
def grado():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select idgrado, descripciongrado from grado order by idgrado')
    datos = cursor.fetchall()
    return render_template("grado.html", descripciongrado=datos)

@app.route('/editargrado/<string:id>')
def editargrado(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh',)
    cursor = conn.cursor()
    cursor.execute('select idgrado, descripciongrado from grado where idgrado = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editargrado.html", comentar=dato[0])

@app.route('/editar_grado/<string:idgrado>',methods=['POST'])
def editar_grado(idgrado):
    if request.method == 'POST':
        corr1=request.form['descripciongrado']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('update grado set descripciongrado=%s where idgrado=%s', (corr1,idgrado))
        conn.commit()
    return redirect(url_for('grado'))

@app.route('/borrargrado/<string:id>')
def borrargrado(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('delete from grado where idgrado = {0}'.format(id))
    conn.commit()
    return redirect(url_for('grado'))


@app.route('/agrega_grado', methods=['POST'])
def agrega_grado():
    if request.method == 'POST':
        aux_Descripciongrado = request.form['descripciongrado']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('insert into grado (descripciongrado) values (%s)',(aux_Descripciongrado))
        conn.commit()
    return redirect(url_for('grado'))

#habilidades

@app.route('/formulariohabilidades')
def formulariohabilidades():
    return render_template("formulariohabilidades.html")

@app.route('/habilidades')
def habilidades():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select idhabilidades, descripcionhabilidades from habilidades order by idhabilidades')
    datos = cursor.fetchall()
    return render_template("habilidades.html", descripcionhabilidades=datos)

@app.route('/editarhabilidades/<string:id>')
def editarhabilidades(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh',)
    cursor = conn.cursor()
    cursor.execute('select idhabilidades, descripcionhabilidades from habilidades where idhabilidades = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editarhabilidades.html", comentar=dato[0])

@app.route('/editar_habilidades/<string:idhabilidades>',methods=['POST'])
def editar_habilidades(idhabilidades):
    if request.method == 'POST':
        corr1=request.form['descripcionhabilidades']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('update habilidades set descripcionhabilidades=%s where idhabilidades=%s', (corr1,idhabilidades))
        conn.commit()
    return redirect(url_for('habilidades'))

@app.route('/borrarhabilidades/<string:id>')
def borrarhabilidades(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('delete from habilidades where idhabilidades = {0}'.format(id))
    conn.commit()
    return redirect(url_for('habilidades'))


@app.route('/agrega_habilidades', methods=['POST'])
def agrega_habilidades():
    if request.method == 'POST':
        aux_Descripcionhabilidades = request.form['descripcionhabilidades']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('insert into habilidades (descripcionhabilidades) values (%s)',(aux_Descripcionhabilidades))
        conn.commit()
    return redirect(url_for('habilidades'))

#idioma

@app.route('/formularioidioma')
def formularioidioma():
    return render_template("formularioidioma.html")

@app.route('/idioma')
def idioma():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select ididioma, descripcionidioma from idioma order by ididioma')
    datos = cursor.fetchall()
    return render_template("idioma.html", descripcionidioma=datos)

@app.route('/editaridioma/<string:id>')
def editaridioma(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh',)
    cursor = conn.cursor()
    cursor.execute('select ididioma, descripcionidioma from idioma where ididioma = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editaridioma.html", comentar=dato[0])

@app.route('/editar_idioma/<string:ididioma>',methods=['POST'])
def editar_idioma(ididioma):
    if request.method == 'POST':
        corr1=request.form['descripcionidioma']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('update idioma set descripcionidioma=%s where ididioma=%s', (corr1,ididioma))
        conn.commit()
    return redirect(url_for('idioma'))

@app.route('/borraridioma/<string:id>')
def borraridioma(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('delete from idioma where ididioma = {0}'.format(id))
    conn.commit()
    return redirect(url_for('idioma'))


@app.route('/agrega_idioma', methods=['POST'])
def agrega_idioma():
    if request.method == 'POST':
        aux_Descripcionidioma = request.form['descripcionidioma']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('insert into idioma (descripcionidioma) values (%s)',(aux_Descripcionidioma))
        conn.commit()
    return redirect(url_for('idioma'))

#Medio

@app.route('/formulariomedio')
def formulariomedio():
    return render_template("formulariomedio.html")

@app.route('/medio')
def medio():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select idmedio, descripcionmedio from medio order by idmedio')
    datos = cursor.fetchall()
    return render_template("medio.html", descripcionmedio=datos)

@app.route('/editarmedio/<string:id>')
def editarmedio(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh',)
    cursor = conn.cursor()
    cursor.execute('select idmedio, descripcionmedio from medio where idmedio = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editarmedio.html", comentar=dato[0])

@app.route('/editar_medio/<string:idmedio>',methods=['POST'])
def editar_medio(idmedio):
    if request.method == 'POST':
        corr1=request.form['descripcionmedio']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('update medio set descripcionmedio=%s where idmedio=%s', (corr1,idmedio))
        conn.commit()
    return redirect(url_for('medio'))

@app.route('/borrarmedio/<string:id>')
def borrarmedio(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('delete from medio where idmedio = {0}'.format(id))
    conn.commit()
    return redirect(url_for('medio'))


@app.route('/agrega_medio', methods=['POST'])
def agrega_medio():
    if request.method == 'POST':
        aux_Descripcionmedio = request.form['descripcionmedio']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('insert into medio (descripcionmedio) values (%s)',(aux_Descripcionmedio))
        conn.commit()
    return redirect(url_for('medio'))

#Documentos

@app.route('/formulariodocumentos')
def formulariodocumentos():
    return render_template("formulariodocumentos.html")

@app.route('/documentos')
def documentos():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select iddocumentos, descripciondocumentos from documentos order by iddocumentos')
    datos = cursor.fetchall()
    return render_template("documentos.html", descripciondocumentos=datos)

@app.route('/editardocumentos/<string:id>')
def editardocumentos(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh',)
    cursor = conn.cursor()
    cursor.execute('select iddocumentos, descripciondocumentos from documentos where iddocumentos = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editardocumentos.html", comentar=dato[0])

@app.route('/editar_documentos/<string:iddocumentos>',methods=['POST'])
def editar_documentos(iddocumentos):
    if request.method == 'POST':
        corr1=request.form['descripciondocumentos']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('update documentos set descripciondocumentos=%s where iddocumentos=%s', (corr1,iddocumentos))
        conn.commit()
    return redirect(url_for('documentos'))

@app.route('/borrardocumentos/<string:id>')
def borrardocumentos(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('delete from documentos where iddocumentos = {0}'.format(id))
    conn.commit()
    return redirect(url_for('documentos'))


@app.route('/agrega_documentos', methods=['POST'])
def agrega_documentos():
    if request.method == 'POST':
        aux_Descripciondocumentos = request.form['descripciondocumentos']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('insert into documentos (descripciondocumentos) values (%s)',(aux_Descripciondocumentos))
        conn.commit()
    return redirect(url_for('documentos'))

#Carrera
@app.route('/formulariocarrera')
def formulariocarrera():
    return render_template("formulariocarrera.html")

@app.route('/carrera')
def carrera():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select idcarrera, descripcioncarrera from carrera order by idcarrera')
    datos = cursor.fetchall()
    return render_template("carrera.html", descripcioncarrera=datos)

@app.route('/editarcarrera/<string:id>')
def editarcarrera(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh',)
    cursor = conn.cursor()
    cursor.execute('select idcarrera, descripcioncarrera from carrera where idcarrera = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editarcarrera.html", comentar=dato[0])

@app.route('/editar_carrera/<string:idcarrera>',methods=['POST'])
def editar_carrera(idcarrera):
    if request.method == 'POST':
        corr1=request.form['descripcioncarrera']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('update carrera set descripcioncarrera=%s where idcarrera=%s', (corr1,idcarrera))
        conn.commit()
    return redirect(url_for('carrera'))

@app.route('/borrarcarrera/<string:id>')
def borrarcarrera(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('delete from carrera where idcarrera = {0}'.format(id))
    conn.commit()
    return redirect(url_for('carrera'))


@app.route('/agrega_carrera', methods=['POST'])
def agrega_carrera():
    if request.method == 'POST':
        aux_Descripcioncarrera = request.form['descripcioncarrera']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('insert into carrera (descripcioncarrera) values (%s)',(aux_Descripcioncarrera))
        conn.commit()
    return redirect(url_for('carrera'))

#Puesto

@app.route('/puesto')
def puesto():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
    cursor = conn.cursor()
    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()
    return render_template("puesto.html", pue=datos, dat='     ', catarea='     ', catEdoCivil='    ',
                            catescolaridad='    ', catgrado='    ', catcarrera='     ', catidioma='     ' , cathabilidades='     ')

@app.route('/puesto_fdetalle/<string:idP>', methods=['GET'])
def puesto_fdetalle(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()
    cursor.execute('select idPuesto,codPuesto,idarea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,''funciones,edad,sexo,idestadocivil,idescolaridad,idgrado,idcarrera,experiencia,conocimientos,manejoEquipo,''reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select a.idarea, a.descripcion from area a, puesto b where a.idarea = b.idarea and b.idPuesto = %s', (idP))
    datos1 = cursor.fetchall()
    cursor.execute('select a.idestadocivil, a.descripcionestadocivil from estadocivil a, puesto b where a.idestadocivil = b.idestadocivil and b.idPuesto = %s', (idP))
    datos2 = cursor.fetchall()
    cursor.execute('select a.idescolaridad, a.descripcionescolaridad from escolaridad a, puesto b where a.idescolaridad = b.idescolaridad and b.idPuesto = %s', (idP))
    datos3 = cursor.fetchall()
    cursor.execute('select a.idgrado, a.descripciongrado from grado a, puesto b where a.idgrado = b.idgrado and b.idPuesto = %s', (idP))
    datos4 = cursor.fetchall()
    cursor.execute('select a.idcarrera, a.descripcioncarrera from carrera a, puesto b where a.idcarrera = b.idcarrera and b.idPuesto = %s', (idP))
    datos5 = cursor.fetchall()
    cursor.execute('select a.idPuesto, b.ididioma, b.descripcionidioma from puesto a, idioma b, puesto_has_idioma c ''where a.idPuesto = c.idPuesto and b.ididioma = c.ididioma and a.idPuesto = %s',(idP))

    datos6 = cursor.fetchall()
    cursor.execute('select a.idPuesto, b.idhabilidades, b.descripcionhabilidades from puesto a, habilidades b, puesto_has_habilidades c ''where a.idPuesto = c.idPuesto and b.idhabilidades = c.idhabilidades and a.idPuesto =%s', (idP))

    datos7 = cursor.fetchall()
    return render_template("puesto.html", pue = datos, dat=dato[0], catarea=datos1[0],
    catEdoCivil=datos2[0], catescolaridad=datos3[0],catgrado=datos4[0], catcarrera=datos5[0], catidioma=datos6,cathabilidades=datos7)

@app.route('/puesto_borrar/<string:idP>')
def puesto_borrar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('delete from puesto where idPuesto = %s',(idP))
    conn.commit()
    cursor.execute('delete from puesto_has_habilidades where idPuesto =%s ', (idP))
    conn.commit()
    cursor.execute('delete from puesto_has_idioma where idPuesto =%s ', (idP))
    conn.commit()
    return redirect(url_for('puesto'))

@app.route('/puesto_agregar')
def puesto_agregar():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()

    cursor.execute('select idarea, descripcion from area ')
    datos1 = cursor.fetchall()
    cursor.execute('select idestadocivil, descripcionestadocivil from estadocivil ')
    datos2 = cursor.fetchall()
    cursor.execute('select idescolaridad, descripcionescolaridad from escolaridad ')
    datos3 = cursor.fetchall()
    cursor.execute('select idgrado, descripciongrado from grado ')
    datos4 = cursor.fetchall()
    cursor.execute('select idcarrera, descripcioncarrera from carrera ')
    datos5 = cursor.fetchall()
    cursor.execute('select ididioma, descripcionidioma from idioma ')
    datos6 = cursor.fetchall()
    cursor.execute('select idhabilidades, descripcionhabilidades from habilidades ')
    datos7 = cursor.fetchall()
    return render_template("puesto_agr.html", catarea=datos1, catEdoCivil=datos2,
    catescolaridad=datos3, catgrado=datos4, catcarrera=datos5, catidioma=datos6,
    cathabilidades=datos7)

@app.route('/puesto_fagrega', methods=['POST'])
def puesto_fagrega():
    if request.method == 'POST':
        if 'idarea' in request.form:idAr = request.form['idarea']
    else:
        idAr = '1'
    if 'idestadocivil' in request.form:idEC = request.form['idestadocivil']
    else:
        idEC = '1'
    if 'idescolaridad' in request.form:idEs = request.form['idescolaridad']
    else:
        idEs = '1'
    if 'idgrado' in request.form:idGA = request.form['idgrado']
    else:
        idGA = '1'
    if 'idcarrera' in request.form:idCa = request.form['idcarrera']
    else:
        idCa = '1'
    if 'sexo' in request.form:sex = request.form['sexo']
    else:
        sex = '1'
    
    codP = request.form['codPuesto']
    nomP = request.form['nomPuesto']
    pueJ = request.form['puestoJefeSup']
    jorn = request.form['jornada']
    remu = request.form['remunMensual']
    pres = request.form['prestaciones']
    descolaridad = request.form['descripcionGeneral']
    func = request.form['funciones']
    eda = request.form['edad']
    expe = request.form['experiencia']
    cono = request.form['conocimientos']
    manE = request.form['manejoEquipo']
    reqF = request.form['reqFisicos']
    reqP = request.form['reqPsicologicos']
    resp = request.form['responsabilidades']
    conT = request.form['condicionesTrabajo']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('insert into puesto(codPuesto,idarea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,''funciones,edad,sexo,idestadocivil,idescolaridad,idgrado,idcarrera,experiencia,conocimientos,manejoEquipo,''reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(codP, idAr, nomP, pueJ, jorn, remu, pres, descolaridad, func, eda, sex, idEC, idEs, idGA, idCa,expe, cono, manE, reqF, reqP, resp, conT))
    conn.commit()
    cursor.execute('select idPuesto, nomPuesto from puesto where idPuesto=(select max(idPuesto) from puesto) ')
    dato=cursor.fetchall()
    idpue = dato[0]
    idP = idpue[0]
    cursor.execute('select count(*) from idioma ')
    dato = cursor.fetchall()
    nidio = dato[0]
    ni = nidio[0] + 1
    for i in range(1, ni):
        idio = 'i' + str(i)
    if idio in request.form:
        cursor.execute('insert into puesto_has_idioma(idPuesto,ididioma) values (%s,%s)', (idP,i))

    conn.commit()
    cursor.execute('select count(*) from habilidades ')
    dato = cursor.fetchall()
    nhab = dato[0]
    nh = nhab[0] + 1

    for i in range(1, nh):
        habi = 'h' + str(i)
    if habi in request.form:
        cursor.execute('insert into puesto_has_habilidades(idPuesto,idhabilidades) values (%s,%s)',(idP, i))

    conn.commit()
    return redirect(url_for('puesto'))

@app.route('/puesto_editar/<string:idP>')
def puesto_editar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select idPuesto,codPuesto,idarea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
        'funciones,edad,sexo,idestadocivil,idescolaridad,idgrado,idcarrera,experiencia,conocimientos,manejoEquipo,'
        'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select idarea, descripcion from area ')
    datos1 = cursor.fetchall()

    cursor.execute('select idestadocivil, descripcionestadocivil from estadocivil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idescolaridad, descripcionescolaridad from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idgrado, descripciongrado from grado ')
    datos4 = cursor.fetchall()

    cursor.execute('select idcarrera, descripcioncarrera from carrera ')
    datos5 = cursor.fetchall()

    cursor.execute('select ididioma, descripcionidioma from idioma ')
    datos6 = cursor.fetchall()

    cursor.execute('select idhabilidades, descripcionhabilidades from habilidades ')
    datos7 = cursor.fetchall()

    cursor.execute('select a.idarea, a.descripcion from area a, puesto b where a.idarea = b.idarea and b.idPuesto = %s',
                   (idP))
    datos11 = cursor.fetchall()

    cursor.execute(
        'select a.idestadocivil, a.descripcionestadocivil from estadocivil a, puesto b where a.idestadocivil = b.idestadocivil and b.idPuesto = %s',
        (idP))
    datos12 = cursor.fetchall()

    cursor.execute(
        'select a.idescolaridad, a.descripcionescolaridad from escolaridad a, puesto b where a.idescolaridad = b.idescolaridad and b.idPuesto = %s',
        (idP))
    datos13 = cursor.fetchall()

    cursor.execute(
        'select a.idgrado, a.descripciongrado from grado a, puesto b where a.idgrado = b.idgrado and b.idPuesto = %s',
        (idP))
    datos14 = cursor.fetchall()

    cursor.execute(
        'select a.idcarrera, a.descripcioncarrera from carrera a, puesto b where a.idcarrera = b.idcarrera and b.idPuesto = %s',
        (idP))
    datos15 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.ididioma, b.descripcionidioma from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.ididioma = c.ididioma and a.idPuesto = %s', (idP))
    datos16 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idhabilidades, b.descripcionhabilidades from puesto a, habilidades b, puesto_has_habilidades c '
                   'where a.idPuesto = c.idPuesto and b.idhabilidades = c.idhabilidades and a.idPuesto = %s', (idP))
    datos17 = cursor.fetchall()

    return render_template("puesto_edi.html", dat=dato[0], catarea=datos1, catEdoCivil=datos2, catescolaridad=datos3,
                           catgrado=datos4, catcarrera=datos5, catidioma=datos6, cathabilidades=datos7,
                           area=datos11[0], EdoCivil=datos12[0], escolaridad=datos13[0], grado=datos14[0],
                           carrera=datos15[0], idioma=datos16, habilidades=datos17, )


@app.route('/puesto_fedita/<string:idP>', methods=['POST'])
def puesto_fedita(idP):
    if request.method == 'POST':
        if 'idgrado' in request.form:
            idGA = request.form['idgrado']
        else:
            idGA = '1'
        if 'idcarrera' in request.form:
            idCa = request.form['idcarrera']
        else:
            idCa = '1'
        codP = request.form['codPuesto']
        idAr = request.form['idarea']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        sex = request.form['sexo']
        idEC = request.form['idestadocivil']
        idEs = request.form['idescolaridad']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('update puesto set codPuesto = %s, idarea = %s, nomPuesto = %s, puestoJefeSup = %s, jornada = %s, '
                   'remunMensual = %s, prestaciones = %s, descripcionGeneral = %s, funciones = %s, edad = %s, sexo = %s, '
                   'idestadocivil = %s, idescolaridad = %s, idgrado = %s, idcarrera = %s, experiencia = %s, '
                   'conocimientos = %s, manejoEquipo = %s, reqFisicos = %s, reqPsicologicos = %s, responsabilidades = %s, '
                   'condicionesTrabajo = %s where idPuesto = %s', (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda,
                   sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF, reqP, resp, conT, idP))
    conn.commit()
    return redirect(url_for('puesto'))

#Requisicion
@app.route('/pendientes')
def pendientes():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
    cursor = conn.cursor()
    cursor.execute('select a.idRequisicion, a.folio, b.nomPuesto from requisicion a,puesto b where a.idPuesto=b.idPuesto and a.autorizada like 0')
    datos = cursor.fetchall()
    return render_template("pendientes.html", pue=datos, dat='    ', catArea='     ', catEdoCivil='     ', 
                            catEscolaridad='     ', catgrado='     ', catCarrera='     ', catidioma='     ', cathabilidades='      ' , catAreaR='      ')
@app.route('/pendientes_fdetalle/<string:idR>', methods=['GET'])
def pendientes_fdetalle(idR):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select a.idRequisicion,a.folio, b.nomPuesto from requisicion a,puesto b where a.idPuesto=b.idPuesto and a.autorizada like 0')
    datos = cursor.fetchall()
    cursor.execute('select a.idpuesto,a.codPuesto,a.idarea,a.nomPuesto,a.puestoJefeSup,a.jornada,a.remunMensual,a.prestaciones,a.descripcionGeneral,' 'a.funciones,a.edad,a.sexo,a.idestadocivil,a.idescolaridad,a.idgrado,a.idCarrera,a.funciones,a.conocimientos,a.manejoEquipo,' 'a.reqFisicos,a.reqPsicologicos,a.responsabilidades,a.condicionesTrabajo,b.folio,b.fechaElab,b.fechaRecluta,b.fechaInicVac,b.motivoRequisicion,b.motivoEspecifique,b.tipoVacante,b.nomSolicita from puesto a, requisicion b where a.idPuesto=b.idPuesto and b.idRequisicion = %s', (idR))
    dato = cursor.fetchall()
    cursor.execute('select a.idarea, a.descripcion from area a, puesto b, requisicion c where a.idarea = b.idarea and c.idRequisicion = %s', (idR))
    datos1 = cursor.fetchall()
    cursor.execute('select a.idestadocivil, a.descripcionestadocivil from estadocivil a, puesto b, requisicion c where a.idestadocivil = b.idestadocivil and b.idPuesto=c.idPuesto and c.idRequisicion = %s', (idR))
    datos2 = cursor.fetchall()
    cursor.execute('select a.idescolaridad, a.descripcionescolaridad from escolaridad a, puesto b, requisicion c where a.idescolaridad = b.idescolaridad and b.idPuesto=c.idPuesto and c.idRequisicion = %s', (idR))
    datos3 = cursor.fetchall()
    cursor.execute('select a.idgrado, a.descripciongrado from grado a, puesto b, requisicion c where a.idgrado = b.idgrado and c.idRequisicion = %s', (idR))
    datos4 = cursor.fetchall()
    cursor.execute('select a.idcarrera, a.descripcioncarrera from carrera a, puesto b, requisicion c where a.idCarrera = b.idCarrera and c.idRequisicion = %s', (idR))
    datos5 = cursor.fetchall()
    cursor.execute('select a.idpuesto, b.ididioma, b.descripcionidioma from puesto a, idioma b, puesto_has_idioma c , requisicion d' ' where a.idpuesto = c.idpuesto and b.ididioma = c.ididioma and d.idRequisicion = %s', (idR))
    datos6 = cursor.fetchall()
    cursor.execute('select a.idpuesto, b.idhabilidades, b.descripcionhabilidades from puesto a, habilidades b, puesto_has_habilidades c, requisicion d ''where a.idpuesto = c.idpuesto and b.idhabilidades = c.idhabilidades and d.idRequisicion = %s', (idR))
    datos7 = cursor.fetchall()
    cursor.execute('select a.idarea, a.descripcion from area a, requisicion b where a.idarea = b.idarea and  b.idRequisicion = %s', (idR))
    datos8 = cursor.fetchall()
    
    print(idR)
    print(dato)
    print(datos1)
    print(datos2)
    print(datos3)
    print(datos4)
    print(datos5)
    print(datos6)
    print(datos7)
    print(datos8)
    return render_template("pendientes.html", pue = datos, dat=dato[0], catArea=datos1[0], 
    catEdoCivil=datos2[0], catEscolaridad=datos3[0], catgrado=datos4[0], catCarrera=datos5[0], catidioma=datos6, cathabilidades=datos7, catAreaR=datos8[0])
@app.route('/pendientes_borrar/<string:idR>')
def pendientes_borrar(idR):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('delete from requisicion where idRequisicion = %s',(idR))
    conn.commit()
    return redirect(url_for('pendientes'))
@app.route('/req_agregar')
def req_agregar():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()

    cursor.execute('select idarea, descripcion from area ')
    datos1 = cursor.fetchall()
    cursor.execute('select idPuesto, nomPuesto from Puesto ')
    datos2 = cursor.fetchall()
    return render_template("req_agr.html", catarea=datos1, catPuesto=datos2)
@app.route('/req_fagrega', methods=['POST'])
def req_fagrega():
    if request.method == 'POST':
        if 'idarea' in request.form:idAr = request.form['idarea']
    else:
        idAr = '1'
    if 'idPuesto' in request.form:idPu = request.form['idPuesto']
    else:
        idPu = '1'

    
    fol = request.form['folio']
    fecEl = request.form['fechaElab']
    fecRe = request.form['fechaRecluta']
    fecInVa = request.form['fechaInicVac']
    motRe = request.form['motivoRequisicion']
    motEs = request.form['motivoEspecifique']
    tipVa = request.form['tipoVacante']
    nomSoli = request.form['nomSolicita']
    


    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('insert into requisicion(folio,idarea,fechaElab,idPuesto,nomSolicita,fechaRecluta,fechaInicVac,tipoVacante,motivoRequisicion,motivoEspecifique) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(fol, idAr, fecEl, idPu, nomSoli, fecRe, fecInVa, tipVa, motRe, motEs))
    conn.commit()
    return redirect(url_for('pendientes'))

@app.route('/req_editar/<string:idR>')
def req_editar(idR):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select a.idRequisicion, a.folio, b.nomPuesto,a.nomRevisa,a.nomAutoriza from requisicion a,puesto b where a.idPuesto=b.idPuesto and a.idRequisicion = %s', (idR))
    dato = cursor.fetchall()

    return render_template("req_edi.html", dat=dato[0])


@app.route('/req_fedita/<string:idR>', methods=['POST'])
def req_fedita(idR):
    if request.method == 'POST':
        if 'idarea' in request.form:idAr = request.form['idarea']
    else:
        idAr = '1'
    if 'idPuesto' in request.form:idPu = request.form['idPuesto']
    else:
        idPu = '1'
        nomRe = request.form['nomRevisa']
        nomAu = request.form['nomAutoriza']
        aut = request.form['autorizada']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('update requisicion set nomRevisa = %s, nomAutoriza = %s, autorizada = %s where idRequisicion = %s', (nomRe,nomAu,aut,idR))
    conn.commit()
    return redirect(url_for('pendientes'))

@app.route('/autorizadas')
def autorizadas():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
    cursor = conn.cursor()
    cursor.execute('select a.idRequisicion, a.folio, b.nomPuesto from requisicion a,puesto b where a.idPuesto=b.idPuesto and a.autorizada like 1')
    datos = cursor.fetchall()
    return render_template("autorizadas.html", pue=datos, dat='    ', catArea='     ', catEdoCivil='     ', 
                            catEscolaridad='     ', catgrado='     ', catCarrera='     ', catidioma='     ', cathabilidades='      ' , catAreaR='      ')
@app.route('/autorizadas_fdetalle/<string:idR>', methods=['GET'])
def autorizadas_fdetalle(idR):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select a.idRequisicion,a.folio, b.nomPuesto from requisicion a,puesto b where a.idPuesto=b.idPuesto and a.autorizada like 1')
    datos = cursor.fetchall()
    cursor.execute('select a.idpuesto,a.codPuesto,a.idarea,a.nomPuesto,a.puestoJefeSup,a.jornada,a.remunMensual,a.prestaciones,a.descripcionGeneral,' 'a.funciones,a.edad,a.sexo,a.idestadocivil,a.idescolaridad,a.idgrado,a.idCarrera,a.funciones,a.conocimientos,a.manejoEquipo,' 'a.reqFisicos,a.reqPsicologicos,a.responsabilidades,a.condicionesTrabajo,b.folio,b.fechaElab,b.fechaRecluta,b.fechaInicVac,b.motivoRequisicion,b.motivoEspecifique,b.tipoVacante,b.nomSolicita, b.nomAutoriza,nomRevisa from puesto a, requisicion b where a.idPuesto=b.idPuesto and b.idRequisicion = %s', (idR))
    dato = cursor.fetchall()
    cursor.execute('select a.idarea, a.descripcion from area a, puesto b, requisicion c where a.idarea = b.idarea and c.idRequisicion = %s', (idR))
    datos1 = cursor.fetchall()
    cursor.execute('select a.idestadocivil, a.descripcionestadocivil from estadocivil a, puesto b, requisicion c where a.idestadocivil = b.idestadocivil and b.idPuesto=c.idPuesto and c.idRequisicion = %s', (idR))
    datos2 = cursor.fetchall()
    cursor.execute('select a.idescolaridad, a.descripcionescolaridad from escolaridad a, puesto b, requisicion c where a.idescolaridad = b.idescolaridad and b.idPuesto=c.idPuesto and c.idRequisicion = %s', (idR))
    datos3 = cursor.fetchall()
    cursor.execute('select a.idgrado, a.descripciongrado from grado a, puesto b, requisicion c where a.idgrado = b.idgrado and c.idRequisicion = %s', (idR))
    datos4 = cursor.fetchall()
    cursor.execute('select a.idcarrera, a.descripcioncarrera from carrera a, puesto b, requisicion c where a.idCarrera = b.idCarrera and c.idRequisicion = %s', (idR))
    datos5 = cursor.fetchall()
    cursor.execute('select a.idpuesto, b.ididioma, b.descripcionidioma from puesto a, idioma b, puesto_has_idioma c , requisicion d' ' where a.idpuesto = c.idpuesto and b.ididioma = c.ididioma and d.idRequisicion = %s', (idR))
    datos6 = cursor.fetchall()
    cursor.execute('select a.idpuesto, b.idhabilidades, b.descripcionhabilidades from puesto a, habilidades b, puesto_has_habilidades c, requisicion d ''where a.idpuesto = c.idpuesto and b.idhabilidades = c.idhabilidades and d.idRequisicion = %s', (idR))
    datos7 = cursor.fetchall()
    cursor.execute('select a.idarea, a.descripcion from area a, requisicion b where a.idarea = b.idarea and  b.idRequisicion = %s', (idR))
    datos8 = cursor.fetchall()
    
    print(idR)
    print(dato)
    print(datos1)
    print(datos2)
    print(datos3)
    print(datos4)
    print(datos5)
    print(datos6)
    print(datos7)
    print(datos8)
    return render_template("autorizadas.html", pue = datos, dat=dato[0], catArea=datos1[0], 
    catEdoCivil=datos2[0], catEscolaridad=datos3[0], catgrado=datos4[0], catCarrera=datos5[0], catidioma=datos6, cathabilidades=datos7, catAreaR=datos8[0])

if __name__ == "__main__":
    app.run(debug=True)
