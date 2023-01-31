from tkinter import *
import tkinter.font as tkfont
import tkinter.messagebox as alert
from xml.dom import minidom

#Clase creada para trabajar datos
from ClassCliente import Cliente, ClienteMenor
paddingForm= 10

#datos de prueba
p = Cliente(1234,'Byron','Sosa',56475647,'example@example.com',70.5,1.77,21,'M')
p.IMC = '26.0 Normal'
p2= ClienteMenor(87654,'Juan','Perez',67894536,'example@example.com',45,1.36,14,'M',45326622)
p2.IMC= '14.7 Normal'

#tablas de datos IMC
TablaIMCAdulto = [18.5,24.9, 25.0,29.9, 30.0]
TablaIMCNina = [12.7,18.5, 13.9,24.7, 16.9,29.4]
TablaIMCNino = [13.0,19.1, 14.1,24.8, 16.6,29.1]

#Almacen de datos de clientes
listaPacientes=[]
listaPacientes.append(p)
listaPacientes.append(p2)

document = "Clientes.xml"

doc = xml.dom.minidom.parseString(document)

#Leer
name = doc.getElementsByTagName("name")[0]
print(name.firstChild.data)

staffs = doc.getElementsByTagName("staff")
for staff in staffs:
        sid = staff.getAttribute("id")
        nickname = staff.getElementsByTagName("nickname")[0]
        salary = staff.getElementsByTagName("salary")[0]
        print("id:%s, nickname:%s, salary:%s" %
              (sid, nickname.firstChild.data, salary.firstChild.data))

#Escribir
def getText(nodelist): 
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            listaPacientes.append(node.data)
    return ''.join(listaPacientes)

def handleSlideshow(slideshow):
    print("<html>")
    handleSlideshowTitle(slideshow.getElementsByTagName("title")[0])
    slides = slideshow.getElementsByTagName("slide")
    handleToc(slides)
    handleSlides(slides)
    print("</html>")

def handleSlides(slides):
    for slide in slides:
        handleSlide(slide)

def handleSlide(slide):
    handleSlideTitle(slide.getElementsByTagName("title")[0])
    handlePoints(slide.getElementsByTagName("point"))

def handleSlideshowTitle(title):
    print(f"<title>{getText(title.childNodes)}</title>")

def handleSlideTitle(title):
    print(f"<h2>{getText(title.childNodes)}</h2>")

def handlePoints(points):
    print("<ul>")
    for point in points:
        handlePoint(point)
    print("</ul>")

def handlePoint(point):
    print(f"<li>{getText(point.childNodes)}</li>")

def handleToc(slides):
    for slide in slides:
        title = slide.getElementsByTagName("title")[0]
        print(f"<p>{getText(title.childNodes)}</p>")

handleSlideshow(doc)

def TablaIMC(datos, sexo, edad):
    try:
        if(edad>=20):
            if (datos < TablaIMCAdulto[0]):
                return "Bajo peso"
            elif(datos > TablaIMCAdulto[0] and datos < TablaIMCAdulto[1]):
                return "Peso normal"
            elif (datos> TablaIMCAdulto[2] and datos < TablaIMCAdulto[3]):
                return "Sobrepeso"
            elif (datos>TablaIMCAdulto[4]):
                return "Obesidad"

        if (edad >5 and edad <=19 and sexo == "F"):
            if (datos <= TablaIMCNina[0] and datos <= TablaIMCNina[1]):
                return "Bajo peso"
            elif(datos >= TablaIMCNina[2] and datos <= TablaIMCNina[3] ):
                return "Peso normal"
            elif (datos >= TablaIMCNina[4] and datos <=TablaIMCNina[5]):
                return "Sobrepeso"
            elif (datos>TablaIMCNina[5]):
                return "Obesidad"

        if (edad > 5 and edad <=19 and sexo == "M"):
            if (datos <= TablaIMCNino[0] and datos <= TablaIMCNino[1]):
                return "Bajo peso"
            elif(datos >= TablaIMCNino[2] and datos <= TablaIMCNino[3] ):
                return "Peso normal"
            elif (datos >= TablaIMCNino[4] and datos <=TablaIMCNino[5]):
                return "Sobrepeso"
            elif (datos>TablaIMCNino[5]):
                return "Obesidad"
    except:
        alert.showerror(title="Error", message="Error al calcular el IMC")

#IMC
def CalcularIMC(Peso,Altura,Edad,Sexo):
    #Adultos 20 o más años, Peso(kg) ÷ (Altura(cm))Elevado a 2 = Resultado
    #Niños y Adolecentes 2 a 19 años, 

    Resultado = round(Peso/(Altura**2),2)
    
    #Se llama la tabla para traer los datos y hacer la comparacion
    dato = TablaIMC(Resultado,Sexo,Edad)
        #Adultos
        #Por debajo de 18.5	Bajo peso
        #18.5 – 24.9	Normal
        #25.0 – 29.9	Sobrepeso
        #30.0 o más	Obesidad
    return f'{Resultado} / {dato}'

def limitador(entry_text, limit):
    if len(entry_text.get()) > 0:
        #donde esta el :5 limitas la cantidad d caracteres
        entry_text.set(entry_text.get()[:limit])

def AgregarCliente(ced,nom, ape,tel,peso,alt,edad,sexo,frm,correo, telE=''):
    validar = False
    if ced == '' or nom == '' or ape == '' or tel == '' or correo == '' or peso == '' or alt == '' or edad == '' or sexo == '' or tel == 0:
        alert.showerror(title='Campos Incompletos',message='Debe completar todos los datos.')
        validar = True
    if len(ape) > 60:
        alert.showerror(title='Apellidos demasiado grandes',message='El máximo de carácteres de los apellidos es de 60')
        validar = True
    if len(tel) != 8:
        alert.showerror(title='Teléfono inválido',message='El teléfono debe ser de 8 carácteres.')
        validar = True
    if not tel.isnumeric():
        alert.showerror(title='Teléfono no es numérico',message='El teléfono debe ser numérico.')
        validar = True
    if not edad.isnumeric():
        alert.showerror(title='Edad no es numérico',message='La edad debe ser numérico.')
        validar = True
    try:
        if telE != '':
            if len(telE) != 8:
                alert.showerror(title='Teléfono del encargado inválido',message='El teléfono del encargado debe ser de 8 carácteres.')
                validar = True
            if not telE.isnumeric():
                alert.showerror(title='Teléfono del encargado no es numérico',message='El teléfono del encargado debe ser numérico.')
                validar = True
            if int(edad) >= 20:
                alert.showerror(title='Edad inválida para un niño(a)',message='Para ser niño debe tener edad menor o igual a 19 años')
                validar = True
            if validar:
                raise "Revise los datos"
            else:
                per = ClienteMenor(ced,nom,ape,int(tel),correo,float(peso),float(alt),int(edad),sexo,telE)
        else:
            per = Cliente(ced,nom,ape,int(tel),correo,float(peso),float(alt),int(edad),sexo)
        per.IMC= CalcularIMC(Peso=float(peso),Altura= float(alt),Edad= int(edad),Sexo= sexo) 
        listaPacientes.append(per)
        alert.showinfo(title='Resultado', message="Usuario guardado con exito")
        frm.destroy()
    except:
        alert.showerror(title='Resultado',message='Error al agregar')
        

def  mostrarPaciente(p):
    formMostrar = Toplevel(root)
    formMostrar.geometry("+{}+{}".format(root.winfo_x() + root.winfo_width(), root.winfo_y()))
    formMostrar.title('Mostrar Datos')

    lblIMC = Label(formMostrar, text='IMC',pady=paddingForm, font=fontText)
    lblIMC.grid(column=1,row=0, padx=10)

    txtIMC = Label(formMostrar, text=p.IMC)
    txtIMC.grid(column=2, row=0, columnspan=2)

    lblIdentificacion = Label(formMostrar, text="Identificación", pady=paddingForm, font=fontText)
    lblIdentificacion.grid(column=1,row=1,padx=10)

    txtIdentificacion = Label(formMostrar, text=p.identificacion)
    txtIdentificacion.grid(column=2,row=1,columnspan=2)

    lblNombre = Label(formMostrar, text="Nombre", pady=paddingForm, font=fontText)
    lblNombre.grid(column=1,row=2,padx=10)

    txtNombre= Label(formMostrar, text=p.nombre)
    txtNombre.grid(column=2, row=2, padx=5,columnspan=2)
    
    lblapellido = Label(formMostrar, text="Apellidos", pady=paddingForm, font=fontText)
    lblapellido.grid(column=1,row=3,padx=10)

    txtapellido= Label(formMostrar, text=p.apellido)
    txtapellido.grid(column=2, row=3, padx=5,columnspan=2)

    lblTelefono= Label(formMostrar, text="Teléfono",pady=paddingForm, font=fontText)
    lblTelefono.grid(column=1,row=4)

    txtTelefono = Label(formMostrar, text=p.telefono)
    txtTelefono.grid(column=2,row=4,columnspan=2)
    
    lblCorreo= Label(formMostrar, text="Correo",pady=paddingForm, font=fontText)
    lblCorreo.grid(column=1,row=5)

    txtCorreo = Label(formMostrar, text=p.correo)
    txtCorreo.grid(column=2,row=5,columnspan=2)

    lblpeso = Label(formMostrar, text="Peso", pady=paddingForm, font=fontText)
    lblpeso.grid(column=1,row=6,padx=10)

    txtpeso= Label(formMostrar, text=p.peso)
    txtpeso.grid(column=2, row=6, padx=5,columnspan=2)

    lblaltura = Label(formMostrar, text="Altura", pady=paddingForm, font=fontText)
    lblaltura.grid(column=1,row=7,padx=10)

    txtaltura= Label(formMostrar, text=p.altura)
    txtaltura.grid(column=2, row=7, padx=5,columnspan=2)

    lbledad = Label(formMostrar, text="Edad", pady=paddingForm, font=fontText)
    lbledad.grid(column=1,row=8,padx=10)

    txtedad= Label(formMostrar, text=p.edad)
    txtedad.grid(column=2, row=8, padx=5,columnspan=2)

    lblsexo = Label(formMostrar, text='Sexo', pady=paddingForm, font=fontText)
    lblsexo.grid(column=1, row=9)

    txtsexo = Label(formMostrar, text=p.sexo)
    txtsexo.grid(column=2, row=9,padx=5,columnspan=2)


    if hasattr(p,'telefonoP'):
        lbltelEncargado = Label(formMostrar, text='Teléfono Encargado', font=fontText, pady=paddingForm)
        lbltelEncargado.grid(column=1,row=10)

        txttelEncargado= Label(formMostrar, text=p.telefonoP)
        txttelEncargado.grid(column=2,row=10, columnspan=2)
        

    formMostrar.mainloop()

def SeleccionPacienteModificar():
    selected = pacientes.get(pacientes.curselection())
    #falta funcion para ver datos al seleccionar el paciente
    for i in range(pacientes.size()):
        if pacientes.get(i) == selected:
            ModificarPaciente(listaPacientes[i])

def Eliminar(p,frm):
    if p in listaPacientes:
        confirmar = alert.askokcancel(title='Confirmar', message=f'¿Seguro que desea eliminar a {p.nombre}?')
        if confirmar:
            listaPacientes.remove(p)
            frm.destroy()
    else:
        alert.showerror(title='Error', message='No se pudo eliminar el paciente')

def modificar(p, ced,nom, ape, tel, mail,peso,alt,edad, gender,frm, telE =''):
    validar = False
    if ced == '' or nom == '' or ape == '' or tel == '' or mail == '' or peso == '' or alt == '' or edad == '' or gender == '' or tel == 0:
        alert.showerror(title='Campos Incompletos',message='Debe completar todos los datos.')
        validar = True
    if len(nom) > 30:
        alert.showerror(title='Nombre demasiado grande',message='El máximo de carácteres del nombre es de 30.')
        validar = True
    if len(ced) != 9:
        alert.showerror(title='Identificación inválido',message='La identificación debe ser de 9 carácteres.')
        validar = True
    if len(ape) > 60:
        alert.showerror(title='Apellidos demasiado grandes',message='El máximo de carácteres de los apellidos es de 60')
        validar = True
    if len(tel) != 8:
        alert.showerror(title='Teléfono inválido',message='El teléfono debe ser de 8 carácteres.')
        validar = True
    if not tel.isnumeric():
        alert.showerror(title='Teléfono no es numérico',message='El teléfono debe ser numérico.')
        validar = True
    if not edad.isnumeric():
        alert.showerror(title='Edad no es numérico',message='La edad debe ser numérico.')
        validar = True
    if (telE != ''):
        if len(telE) != 8:
            alert.showerror(title='Teléfono del encargado inválido',message='El teléfono del encargado debe ser de 8 carácteres.')
            validar = True
        if not telE.isnumeric():
            alert.showerror(title='Teléfono del encargado no es numérico',message='El teléfono del encargado debe ser numérico.')
            validar = True
        if int(edad) >= 20:
            alert.showerror(title='Edad inválida para un niño(a)',message='Para ser niño debe tener edad menor o igual a 19 años')
            validar = True
    try:
        if validar:
            alert.showwarning(message="Datos incorrectos revise y vuelva a intentarlo", title="Aviso!!!")
        p.nombre = nom
        p.identificacion = ced
        p.apellido= ape
        p.telefono= int(tel)
        p.correo= mail
        p.peso= float(peso)
        p.altura = float(alt)
        p.edad = int(edad)
        p.sexo = gender

        if telE != 0:
            p.telefonoP = telE
        alert.showinfo(title='Resultado',message='Usuario modificado correctamente')
        p.IMC= CalcularIMC(Peso=float(peso),Altura= float(alt),Edad= int(edad),Sexo= gender)
        frm.destroy()
    except :
        alert.showerror(title='Resultado',message='Error al modificar')

def seleccionPacienteConsultar():
    selected = pacientes.get(pacientes.curselection())
    #falta funcion para ver datos al seleccionar el paciente
    for i in range(pacientes.size()):
        if pacientes.get(i) == selected:
            mostrarPaciente(listaPacientes[i])

#metodo buscar en la lista de pacientes
def buscarPaciente(text, frm):
    pacientes.select_clear(0, 'end')
    for i in range(pacientes.size()):
        if pacientes.get(i).startswith(text.capitalize()):
            pacientes.activate(i)
            pacientes.select_set(i, last=i)
            break
        elif pacientes.get(i).endswith(text.capitalize()):
            pacientes.activate(i)
            pacientes.select_set(i, last=i)
            break
        elif text.capitalize() in pacientes.get(i):
            pacientes.activate(i)
            pacientes.select_set(i, last=i)
            break
    else:
        frm.grab_set()
        alert.showinfo(title='NO FOUND', message='No existe un registro que coincida')

        frm.grab_release()

#form
def ModificarPaciente(p):

    ced = StringVar(value=p.identificacion)
    nom = StringVar(value=p.nombre)
    ape = StringVar(value=p.apellido)
    tel= StringVar(value=p.telefono)
    mail = StringVar(value=p.correo)
    peso = StringVar(value=p.peso)
    alt = StringVar(value=p.altura)
    edad = StringVar(value=p.edad)
    gender = StringVar(value=p.sexo)

    formModificar = Toplevel(root)
    formModificar.title("Actualizar Datos")
    formModificar.geometry("+{}+{}".format(root.winfo_x() + root.winfo_width(), root.winfo_y()))


    lblTitulo = Label(formModificar, text="Datos", font=fontTitle, justify=CENTER)
    lblTitulo.grid(column=1,row=0, columnspan=2,padx=10)


    lblIdentificacion = Label(formModificar, text="Identificación", pady=paddingForm, font=fontText)
    lblIdentificacion.grid(column=1,row=1,padx=10)

    txtIdentificacion = Entry(formModificar,font=fontText, textvariable=ced)#colocar el font a los entry aumenta el tamano
    txtIdentificacion.grid(column=2,row=1,columnspan=2)
    ced.trace("w", lambda *args: limitador(ced,9))


    lblNombre = Label(formModificar, text="Nombre", pady=paddingForm, font=fontText)
    lblNombre.grid(column=1,row=2,padx=10)

    txtNombre= Entry(formModificar, font=fontText, textvariable=nom)
    txtNombre.grid(column=2, row=2, padx=5,columnspan=2)
    nom.trace("w", lambda *args: limitador(nom,30))
    
    lblapellido = Label(formModificar, text="Apellidos", pady=paddingForm, font=fontText)
    lblapellido.grid(column=1,row=3,padx=10)

    txtapellido= Entry(formModificar, font=fontText, textvariable=ape)
    txtapellido.grid(column=2, row=3, padx=5,columnspan=2)
    ape.trace("w", lambda *args: limitador(ape,60))

    lblTelefono= Label(formModificar, text="Teléfono",pady=paddingForm, font=fontText)
    lblTelefono.grid(column=1,row=4)

    txtTelefono = Entry(formModificar, font=fontText, textvariable=tel)
    txtTelefono.grid(column=2,row=4,columnspan=2)
    tel.trace("w", lambda *args: limitador(tel,8))
    
    lblCorreo= Label(formModificar, text="Correo",pady=paddingForm, font=fontText)
    lblCorreo.grid(column=1,row=5)

    txtCorreo = Entry(formModificar, font=fontText, textvariable=mail)
    txtCorreo.grid(column=2,row=5,columnspan=2)

    lblpeso = Label(formModificar, text="Peso (kg)", pady=paddingForm, font=fontText)
    lblpeso.grid(column=1,row=6,padx=10)

    txtpeso= Entry(formModificar, font=fontText, textvariable=peso)
    txtpeso.grid(column=2, row=6, padx=5,columnspan=2)

    lblaltura = Label(formModificar, text="Altura (metros)", pady=paddingForm, font=fontText)
    lblaltura.grid(column=1,row=7,padx=10)

    txtaltura= Entry(formModificar, font=fontText, textvariable=alt)
    txtaltura.grid(column=2, row=7, padx=5,columnspan=2)

    lbledad = Label(formModificar, text="Edad\n(años cumplidos)", pady=paddingForm, font=fontText)
    lbledad.grid(column=1,row=8,padx=10)

    txtedad= Entry(formModificar, font=fontText, textvariable=edad)
    txtedad.grid(column=2, row=8, padx=5,columnspan=2)

    lblsexo = Label(formModificar, text='Sexo', pady=paddingForm, font=fontText)
    lblsexo.grid(column=1, row=9)

    #variable radiobuton
    g1 = Radiobutton(formModificar,text='M', variable=gender, value='M')
    g2 = Radiobutton(formModificar,text='F', variable=gender, value='F')

    g1.grid(column=2,row=9)
    g2.grid(column=3, row=9)

    #falta command
    btnModificar= Button(formModificar, text="Modificar", command=lambda:modificar(frm=formModificar,
        p=p, ced= txtIdentificacion.get(),
        nom=txtNombre.get(),
        ape=txtapellido.get(),
        tel=txtTelefono.get(),
        mail=txtCorreo.get(),
        peso=txtpeso.get(),
        alt= txtaltura.get(),
        edad=txtedad.get(),
        gender=gender.get()), width=12, height=2, border=1)
    btnModificar.grid(column=1, row=10, columnspan=3, pady=10)

    btnEliminar = Button(formModificar, text='Eliminar', command=lambda:Eliminar(p,formModificar), width=15, height=2, border=1)
    btnEliminar.grid(column=1, row=11, columnspan=3, pady=10)

    #verificar si existe el atributo en el objeto
    if hasattr(p, 'telefonoP'):
        lbltelEncargado = Label(formModificar, text='Teléfono Encargado', font=fontText, pady=paddingForm)
        lbltelEncargado.grid(column=1,row=10)

        telEncargado = StringVar(value=p.telefonoP)
        txttelEncargado= Entry(formModificar, font=fontText, textvariable=telEncargado)
        txttelEncargado.grid(column=2,row=10, columnspan=2)

        btnModificar.grid(column=1, row=11, columnspan=3, pady=10)
        btnEliminar.grid(column=1, row=12, columnspan=3, pady=10)
    formModificar.mainloop()

#form
def nuevoPaciente():
    ced= StringVar()
    nom = StringVar()
    ape =StringVar()
    tel = StringVar()
    telefE = StringVar()
    resp=alert.askquestion(title='Tipo Paciente', message='¿Va a agregar un menor?')

    formPaciente = Toplevel(root)
    formPaciente.title("Registro Paciente")
    formPaciente.geometry("+{}+{}".format(root.winfo_x() + root.winfo_width(), root.winfo_y()))


    lblTitulo = Label(formPaciente, text="Datos", font=fontTitle, justify=CENTER)
    lblTitulo.grid(column=1,row=0, columnspan=2,padx=10)


    lblIdentificacion = Label(formPaciente, text="Identificación", pady=paddingForm, font=fontText)
    lblIdentificacion.grid(column=1,row=1,padx=10)

    txtIdentificacion = Entry(formPaciente,font=fontText, textvariable=ced)#colocar el font a los entry aumenta el tamano
    txtIdentificacion.grid(column=2,row=1,columnspan=2)
    ced.trace("w", lambda *args: limitador(ced,9))


    lblNombre = Label(formPaciente, text="Nombre", pady=paddingForm, font=fontText)
    lblNombre.grid(column=1,row=2,padx=10)

    txtNombre= Entry(formPaciente, font=fontText, textvariable=nom)
    txtNombre.grid(column=2, row=2, padx=5,columnspan=2)
    nom.trace("w", lambda *args: limitador(nom,30))
    
    lblapellido = Label(formPaciente, text="Apellidos", pady=paddingForm, font=fontText)
    lblapellido.grid(column=1,row=3,padx=10)

    txtapellido= Entry(formPaciente, font=fontText, textvariable=ape)
    txtapellido.grid(column=2, row=3, padx=5,columnspan=2)
    ape.trace("w", lambda *args: limitador(ape,60))

    lblTelefono= Label(formPaciente, text="Teléfono",pady=paddingForm, font=fontText)
    lblTelefono.grid(column=1,row=4)

    txtTelefono = Entry(formPaciente, font=fontText, textvariable=tel)
    txtTelefono.grid(column=2,row=4,columnspan=2)
    tel.trace("w", lambda *args: limitador(tel,8))
    
    lblCorreo= Label(formPaciente, text="Correo",pady=paddingForm, font=fontText)
    lblCorreo.grid(column=1,row=5)

    txtCorreo = Entry(formPaciente, font=fontText)
    txtCorreo.grid(column=2,row=5,columnspan=2)

    lblpeso = Label(formPaciente, text="Peso (kg)", pady=paddingForm, font=fontText)
    lblpeso.grid(column=1,row=6,padx=10)

    txtpeso= Entry(formPaciente, font=fontText)
    txtpeso.grid(column=2, row=6, padx=5,columnspan=2)

    lblaltura = Label(formPaciente, text="Altura (metros)", pady=paddingForm, font=fontText)
    lblaltura.grid(column=1,row=7,padx=10)

    txtaltura= Entry(formPaciente, font=fontText)
    txtaltura.grid(column=2, row=7, padx=5,columnspan=2)

    lbledad = Label(formPaciente, text="Edad\n(años cumplidos)", pady=paddingForm, font=fontText)
    lbledad.grid(column=1,row=8,padx=10)

    txtedad= Entry(formPaciente, font=fontText)
    txtedad.grid(column=2, row=8, padx=5,columnspan=2)

    lblsexo = Label(formPaciente, text='Sexo', pady=paddingForm, font=fontText)
    lblsexo.grid(column=1, row=9)

    #variable radiobuton
    gender = StringVar()
    g1 = Radiobutton(formPaciente,text='M', variable=gender, value='M')
    g2 = Radiobutton(formPaciente,text='F', variable=gender, value='F')

    g1.grid(column=2,row=9)
    g2.grid(column=3, row=9)

    #definir valor inicial marcado
    gender.set('M')
    
    btnAceptar= Button(formPaciente, text="Aceptar", command=lambda:AgregarCliente(
    frm=formPaciente,
    ced= ced.get(),
    nom= nom.get(),
    ape= ape.get(), 
    tel= tel.get(),
    correo= txtCorreo.get(),
    peso= txtpeso.get(),
    alt= txtaltura.get(),
    edad= txtedad.get(),
    sexo= gender.get()), width=10)
    btnAceptar.grid(column=1, row=10, columnspan=3, pady=10)

    if resp == 'yes':
        
        lbltelEncargado = Label(formPaciente, text='Teléfono Encargado', font=fontText, pady=paddingForm)
        lbltelEncargado.grid(column=1,row=10)

        txttelEncargado= Entry(formPaciente, font=fontText, textvariable = telefE)
        txttelEncargado.grid(column=2,row=10, columnspan=2)
        telefE.trace("w", lambda *args: limitador(telefE,9))
        
        btnAceptar.grid_forget()
        btnAceptarM= Button(formPaciente, text="Aceptar", command=lambda:AgregarCliente(
        frm=formPaciente,
        ced=txtIdentificacion.get(),
        nom= txtNombre.get(),
        ape= txtapellido.get(), 
        tel= txtTelefono.get(),
        correo= txtCorreo.get(),
        peso= txtpeso.get(),
        alt= txtaltura.get(),
        edad= txtedad.get(),
        sexo= gender.get(),
        telE= txttelEncargado.get()), width=10)
        btnAceptarM.grid(column=1, row=11, columnspan=3, pady=10)
    formPaciente.mainloop()

#form
def ConsultarPaciente():
    global pacientes, txtBuscar
    formConsultar = Toplevel(root)
    formConsultar.title("Búsqueda")

    lblBuscar = Label(formConsultar, text='Digite el nombre o apellido',justify='center', font=fontText)
    lblBuscar.grid(column=1,row=0)

    txtBuscar = Entry(formConsultar, font=fontText)
    txtBuscar.grid(column=1, row=1)

    btnBuscar= Button(formConsultar, text='Buscar',command=lambda:buscarPaciente(txtBuscar.get(), formConsultar), width=10)
    btnBuscar.grid(column=2,row=1,pady=10)

    #lista de pacientes
    pacientes = Listbox(formConsultar,font=fontText,justify='center')
    pacientes.grid(row=2,column=1)

    for p in listaPacientes:
        pacientes.insert('end',  p.nombre +" "+p.apellido)
        

    btnAceptar= Button(formConsultar, text="Aceptar", command=seleccionPacienteConsultar, width=10, padx=10)
    btnAceptar.grid(column=1, row=3, columnspan=2, pady=10)

    formConsultar.mainloop()

#form
def ConsultarPacienteMod():
    global pacientes, txtBuscar
    formConsultar = Toplevel(root)
    formConsultar.title("Búsqueda")

    lblBuscar = Label(formConsultar, text='Digite el nombre o apellido',justify='center', font=fontText)
    lblBuscar.grid(column=1,row=0)

    txtBuscar = Entry(formConsultar, font=fontText)
    txtBuscar.grid(column=1, row=1)

    btnBuscar= Button(formConsultar, text='Buscar',command=lambda:buscarPaciente(txtBuscar.get(), formConsultar), width=10)
    btnBuscar.grid(column=2,row=1,pady=10)

    #lista de pacientes
    pacientes = Listbox(formConsultar,font=fontText,justify='center')
    pacientes.grid(row=2,column=1)

    for p in listaPacientes:
        pacientes.insert('end',  p.nombre +" "+p.apellido)
        

    btnAceptar= Button(formConsultar, text="Aceptar", command=SeleccionPacienteModificar, width=10, padx=10)
    btnAceptar.grid(column=1, row=3, columnspan=2, pady=10)

    formConsultar.mainloop()

def ModificarTablaIMC(li1, li2, li3):
    aBajo= StringVar(value=li1[0])
    aMinNormal = StringVar(value=li1[1])
    aMaxNormal = StringVar(value=li1[2])
    aMinSobre = StringVar(value=li1[3])
    aMaxSobre = StringVar(value=li1[4])
    aObesidad = StringVar(value=li1[4])

    ninoBajoMin = StringVar(value= li2[0])
    ninoBajoMax = StringVar(value=li2[1])
    ninoNornalMin = StringVar(value=li2[2])
    ninoNormalMax = StringVar(value=li2[3])
    ninoSobreMin = StringVar(value=li2[4])
    ninoSobreMax = StringVar(value=li2[5])
    
    ninaBajoMin = StringVar(value= li3[0])
    ninaBajoMax = StringVar(value=li3[1])

    ninaNornalMin = StringVar(value=li3[2])
    ninaNormalMax = StringVar(value=li3[3])

    ninaSobreMin = StringVar(value=li3[4])
    ninaSobreMax = StringVar(value=li3[5])

    formTabla= Toplevel(root)
    formTabla.title("Modificar Tabla de IMC")
    formTabla.geometry("+{}+{}".format(root.winfo_x() + root.winfo_width(), root.winfo_y()))

    lblTitulo = Label(formTabla, text="Tabla IMC", font=fontTitle)
    lblTitulo.grid(row=0,column=1,columnspan=3, padx=10, pady=10)

    lblAduto = Label(formTabla, text='Adutos', font=fontText, justify=CENTER)
    lblAduto.grid(row=0,column=0, rowspan=4)

    lblABajo = Label(formTabla, text="Bajo peso\nmenor a:")
    lblABajo.grid(row=1, column=0, padx=8)

    txtABajo = Entry(formTabla, textvariable=aBajo, font=fontText)
    txtABajo.grid(row=1, column=1, padx=8)



    formTabla.mainloop()


#definicion form principal
root= Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("Pacientes - Elemental Nutrición")


#variables interfaz
fontTitle = tkfont.Font(size=25)
fontText = tkfont.Font(size=13)

lblTitulo= Label(root, text="Control de Pacientes",font=fontTitle)
lblTitulo.grid(column=2, row=0, pady=15, columnspan=3)

#Nuevo Paciente
btnNuevoPaciente= Button(root, text="Nuevo Paciente", command=nuevoPaciente, width=14, height=5, font=fontText, padx=10, border=5, borderwidth=3)
btnNuevoPaciente.grid(column=2, row=1, padx=18, pady=10)# agregar el padx aqui crea separacion con otros elementos

#consultar paciente
btnRevisarPaciente= Button(root, text="Consultar Paciente", command=ConsultarPaciente, width=14, height=5, font=fontText, padx=10, border=5, borderwidth=3)
btnRevisarPaciente.grid(column=3, row=1, padx=18, pady=10)

#Modificar / eliminar Paciente
btnModificarPaciente= Button(root, text="Modificar Paciente",command=ConsultarPacienteMod, width=14, height=5, font=fontText, padx=10, border=5, borderwidth=3)
btnModificarPaciente.grid(column=2, row=2, padx=18)

#Modificar datos de IMC
btnModificarPaciente= Button(root, text="Modificar Tabla IMC",command= lambda:ModificarTablaIMC(TablaIMCAdulto, TablaIMCNino, TablaIMCNina), width=14, height=5, font=fontText, padx=10, border=5, borderwidth=3)
btnModificarPaciente.grid(column=3, row=2, padx=18)

#boton generar xml
#falta command
btnGenerarXML= Button(root, text="Exportar\nPacientes", width=10, height=2, font=fontText, padx=10, border=5, borderwidth=3)
btnGenerarXML.grid(column=4, row=2, padx=18, sticky="S")

root.mainloop()
