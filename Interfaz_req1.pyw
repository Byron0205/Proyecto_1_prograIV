from tkinter import *
import tkinter.font as tkfont
import tkinter.messagebox as alert
from tkinter import filedialog
from xml.dom import minidom
import xml.etree.ElementTree as ET
import os.path
#Clase creada para trabajar datos
from ClassCliente import Cliente, ClienteMenor
paddingForm= 10

#datos de prueba
""" p = Cliente(1234,'Byron','Sosa',56475647,'example@example.com',70.5,177,21,'M')
p.IMC = '26.0 Normal' """
p2= ClienteMenor(87654,'Juan','Perez',67894536,'example@example.com',45,136,14,'M',45326622)
p2.IMC= '14.7 Normal'

#Almacen de datos de clientes
listaPacientes=[]
#listaPacientes.append(p)
listaPacientes.append(p2)


def validarExtension():
    file_path=filedialog.askopenfilename()
    if os.path.splitext(file_path)[1].lower() == ".xml":
        # La extensión del archivo es .xml
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return file_path
        else:
            # La ruta no es válida o el archivo no existe
            alert.showerror(title='Error con el mensaje',message="El archivo no existe o la ruta es incorrecta.")
    else:
        # La extensión del archivo no es .xml
        alert.showinfo(title='Error de extension',message="El archivo no es un archivo XML.")

def EscribirXMl(): 
    root = ET.Element("ElementalNutricion")
    
    for datoC in listaPacientes:
        c1 = ET.SubElement(root,"cliente")
        i1 = ET.SubElement(c1, "identificación")
        i1.text = str(datoC.identificacion)
        n1 = ET.SubElement(c1, "nombre")
        n1.text = datoC.nombre
        a1 = ET.SubElement(c1, "apellido")
        a1.text = datoC.apellido
        t1 = ET.SubElement(c1, "telefono")
        t1.text = str(datoC.telefono)
        co1 = ET.SubElement(c1, "correo")
        co1.text = datoC.correo
        g1 = ET.SubElement(c1, "genero")
        g1.text = datoC.sexo
        e1 = ET.SubElement(c1, "estaturaCM")
        e1.text = str(datoC.altura)
        p1 = ET.SubElement(c1, "pesoKG")
        p1.text = str(datoC.peso)
        ed1 = ET.SubElement(c1, "edad")
        ed1.text = str(datoC.edad)
        imc1 = ET.SubElement(c1, "IMC")
        imc1.text = datoC.IMC
        tE1 = ET.SubElement(c1, "telefonoEncargado")
        if (hasattr(datoC,'telefonoP')):
            tE1.text = str(datoC.telefonoP)
            
    
    tree = ET.ElementTree(root)
    #tree.write('pacientesPrueba.xml', encoding="UTF-8", xml_declaration=True, method="xml")
    xml = minidom.parseString(ET.tostring(root, encoding='unicode'))

    with open('Pacientes.xml', 'w', encoding="UTF-8") as f:
        f.write(xml.toprettyxml(indent="    "))


def leerXML():
    file_path = validarExtension()
    if (os.path.exists(file_path)):
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        clients = root.findall('cliente')
        for c in clients:
            client = c.find('identificación')
            for p in listaPacientes:
                if client.text == str(p.identificacion):
                    break
            else:
                datos = []
                for child in c:
                        datos.append(child.text)
                        
                if (datos[10] == None):
                    p = Cliente(identificacion= datos[0],nombre= datos[1],apellido= datos[2],telefono= datos[3],correo= datos[4],sexo= datos[5],altura= datos[6],peso= datos[7],edad= datos[8])
                    p.IMC = datos[9]
                    listaPacientes.append(p)
                else:
                    p = ClienteMenor(identificacion= datos[0],nombre= datos[1],apellido= datos[2],telefono= datos[3],correo= datos[4],sexo= datos[5],altura= datos[6],peso= datos[7],edad= datos[8],telefonoP= datos[10])
                    p.IMC = datos[9]
                    listaPacientes.append(p)

global TablaIMCAdulto, TablaIMCNino,TablaIMCNina
#tablas de datos IMC
TablaIMCAdulto = [18.5,24.9, 25.0,29.9, 30.0]
TablaIMCNina = [12.7,18.5, 13.9,24.7, 16.9,29.4]
TablaIMCNino = [13.0,19.1, 14.1,24.8, 16.6,29.1]

def TablaIMC(datos, sexo, edad):
    try:
        if(edad>=20):
            if (datos < TablaIMCAdulto[0]):
                return "Bajo peso"
            elif(datos >= TablaIMCAdulto[0] and datos <= TablaIMCAdulto[1]):
                return "Peso normal"
            elif (datos>= TablaIMCAdulto[2] and datos <= TablaIMCAdulto[3]):
                return "Sobrepeso"
            elif (datos>=TablaIMCAdulto[4]):
                return "Obesidad"

        if (edad >5 and edad <=19 and sexo == "F"):
            if (datos < TablaIMCNina[0]):
                return "Bajo peso"
            elif (datos >= TablaIMCNina[0] and datos <= TablaIMCNina[1]):
                return "Bajo peso"
            elif(datos >= TablaIMCNina[2] and datos <= TablaIMCNina[3] ):
                return "Peso normal"
            elif (datos >= TablaIMCNina[4] and datos <=TablaIMCNina[5]):
                return "Sobrepeso"
            elif (datos>TablaIMCNina[5]):
                return "Obesidad"

        if (edad > 5 and edad <=19 and sexo == "M"):
            if (datos < TablaIMCNino[0]):
                return "Bajo peso"
            elif (datos >= TablaIMCNino[0] and datos <= TablaIMCNino[1]):
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
    alt = Altura*(1.0/100)
    Resultado = round(Peso/(alt**2),2)
    
    #Se llama la tabla para traer los datos y hacer la comparacion
    dato = TablaIMC(Resultado,Sexo,Edad)
        #Adultos
        #Por debajo de 18.5	Bajo peso
        #18.5 – 24.9	Normal
        #25.0 – 29.9	Sobrepeso
        #30.0 o más	Obesidad
    return f'{Resultado} {dato}'

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
                per = ClienteMenor(ced,nom,ape,int(tel),correo,float(peso),int(alt),int(edad),sexo,telE)

        else:
            per = Cliente(ced,nom,ape,int(tel),correo,float(peso),int(alt),int(edad),sexo)
        per.IMC= CalcularIMC(Peso=float(peso),Altura= int(alt),Edad= int(edad),Sexo= sexo) 
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

    lblpeso = Label(formMostrar, text="Peso (Kg)", pady=paddingForm, font=fontText)
    lblpeso.grid(column=1,row=6,padx=10)

    txtpeso= Label(formMostrar, text=p.peso)
    txtpeso.grid(column=2, row=6, padx=5,columnspan=2)

    lblaltura = Label(formMostrar, text="Altura (cm)", pady=paddingForm, font=fontText)
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

def modificarValoresIMC(a1,a2,a3,a4,a5, no1, no2,no3,no4,no5,no6, na1,na2,na3,na4,na5,na6):
    TablaIMCAdulto.clear()
    TablaIMCAdulto.extend([float(a1.get()),float(a2.get()),float(a3.get()),float(a4.get()),float(a5.get())])

    TablaIMCNino.clear()
    TablaIMCNino.extend([float(no1.get()),float(no2.get()),float(no3.get()),float(no4.get()),float(no5.get()),float(no6.get())])

    TablaIMCNina.clear()
    TablaIMCNina.extend([float(na1.get()),float(na2.get()),float(na3.get()),float(na4.get()),float(na5.get()),float(na6.get())])

    for p in listaPacientes:
        p.IMC= CalcularIMC(Peso=float(p.peso),Altura= int(p.altura),Edad= int(p.edad),Sexo= p.sexo) 

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

    lblaltura = Label(formPaciente, text="Altura (cm)", pady=paddingForm, font=fontText)
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
        telefE.trace("w", lambda *args: limitador(telefE,8))
        
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

#form
def ModificarTablaIMC(li1, li2, li3):
    aBajo= StringVar(value=li1[0])
    aMaxNormal = StringVar(value=li1[1])
    aMinSobre = StringVar(value=li1[2])
    aMaxSobre = StringVar(value=li1[3])
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

    lblAduto = Label(formTabla, text='Adultos', font=fontText)
    lblAduto.grid(row=1,column=0, pady=10)

    lblABajo = Label(formTabla, text="Bajo peso\nmenor a:")
    lblABajo.grid(row=2, column=0, padx=8)

    txtABajo = Entry(formTabla, textvariable=aBajo, font=fontText)
    txtABajo.grid(row=2, column=1, padx=8)
    
    lblANormal = Label(formTabla, text="Peso normal entre:", justify=CENTER)
    lblANormal.grid(row=3, column=0, padx=8)

    txtAnormal1 = Entry(formTabla, textvariable=aBajo, font=fontText)
    txtAnormal1.grid(row=3, column=1, padx=8)
    txtAnormal2 = Entry(formTabla, textvariable=aMaxNormal, font=fontText)
    txtAnormal2.grid(row=3, column=2, padx=8)
    
    lblAsobre = Label(formTabla, text="Sobrepeso entre:", justify=CENTER)
    lblAsobre.grid(row=4, column=0, padx=8)

    txtAsobre1 = Entry(formTabla, textvariable=aMinSobre, font=fontText)
    txtAsobre1.grid(row=4, column=1, padx=8)
    txtAsobre2 = Entry(formTabla, textvariable=aMaxSobre, font=fontText)
    txtAsobre2.grid(row=4, column=2, padx=8)
    
    lblAObesidad = Label(formTabla, text="Obesidad\nmayor a:", justify=CENTER)
    lblAObesidad.grid(row=5, column=0, padx=8)
    
    txtAsobre2 = Entry(formTabla, textvariable=aObesidad, font=fontText)
    txtAsobre2.grid(row=5, column=1, padx=8)
    
    lblNino = Label(formTabla, text='Niños', font=fontText)
    lblNino.grid(row=1,column=3, pady=10)

    lblNoBajo = Label(formTabla, text="Bajo peso\nmenor a:")
    lblNoBajo.grid(row=2, column=3, padx=8)

    txtNoBajo1 = Entry(formTabla, textvariable=ninoBajoMin, font=fontText)
    txtNoBajo1.grid(row=2, column=4, padx=8)
    txtNoBajo2 = Entry(formTabla, textvariable=ninoBajoMax, font=fontText)
    txtNoBajo2.grid(row=2, column=5, padx=8)
    
    lblNoNormal = Label(formTabla, text="Peso normal entre:", justify=CENTER)
    lblNoNormal.grid(row=3, column=3, padx=8)

    txtNoNormal1 = Entry(formTabla, textvariable=ninoNornalMin, font=fontText)
    txtNoNormal1.grid(row=3, column=4, padx=8)
    txtNoNormal2 = Entry(formTabla, textvariable=ninoNormalMax, font=fontText)
    txtNoNormal2.grid(row=3, column=5, padx=8)
    
    lblNosobre = Label(formTabla, text="Sobrepeso entre:", justify=CENTER)
    lblNosobre.grid(row=4, column=3, padx=8)

    txtNosobre1 = Entry(formTabla, textvariable=ninoSobreMin, font=fontText)
    txtNosobre1.grid(row=4, column=4, padx=8)
    txtNosobre2 = Entry(formTabla, textvariable=ninoSobreMax, font=fontText)
    txtNosobre2.grid(row=4, column=5, padx=8)
    
    lblNoObesidad = Label(formTabla, text="Obesidad\nmayor a:", justify=CENTER)
    lblNoObesidad.grid(row=5, column=3, padx=8)
    
    txtNosobre2 = Entry(formTabla, textvariable=ninoSobreMax, font=fontText)
    txtNosobre2.grid(row=5, column=4, padx=8)
    #ninna
    lblNina = Label(formTabla, text='Niñas', font=fontText)
    lblNina.grid(row=6,column=0, pady=10)

    lblNaBajo = Label(formTabla, text="Bajo peso\nmenor a:")
    lblNaBajo.grid(row=7, column=0, padx=8)

    txtNaBajo1 = Entry(formTabla, textvariable=ninaBajoMin, font=fontText)
    txtNaBajo1.grid(row=7, column=1, padx=8)
    txtNaBajo2 = Entry(formTabla, textvariable=ninaBajoMax, font=fontText)
    txtNaBajo2.grid(row=7, column=2, padx=8)
    
    lblNaNormal = Label(formTabla, text="Peso normal entre:", justify=CENTER)
    lblNaNormal.grid(row=8, column=0, padx=8)

    txtNaNormal1 = Entry(formTabla, textvariable=ninaNornalMin, font=fontText)
    txtNaNormal1.grid(row=8, column=1, padx=8)
    txtNaNormal2 = Entry(formTabla, textvariable=ninaNormalMax, font=fontText)
    txtNaNormal2.grid(row=8, column=2, padx=8)
    
    lblNasobre = Label(formTabla, text="Sobrepeso entre:", justify=CENTER)
    lblNasobre.grid(row=9, column=0, padx=8)

    txtNasobre1 = Entry(formTabla, textvariable=ninaSobreMin, font=fontText)
    txtNasobre1.grid(row=9, column=1, padx=8)
    txtNasobre2 = Entry(formTabla, textvariable=ninaSobreMax, font=fontText)
    txtNasobre2.grid(row=9, column=2, padx=8)
    
    lblNaObesidad = Label(formTabla, text="Obesidad\nmayor a:", justify=CENTER)
    lblNaObesidad.grid(row=10, column=0, padx=8)
    
    txtNasobre2 = Entry(formTabla, textvariable=ninaSobreMax, font=fontText)
    txtNasobre2.grid(row=10, column=1, padx=8)

    btnModificar= Button(formTabla, text="Modificar Datos", 
    command=lambda: modificarValoresIMC(aBajo,aMaxNormal,aMinSobre,aMaxSobre,aObesidad,
    ninaBajoMin,ninaBajoMax,ninoNornalMin,ninoNormalMax,ninoSobreMin,ninoSobreMax,
    ninaBajoMin, ninaBajoMax,ninaNornalMin,ninaNormalMax,ninaSobreMin,ninaSobreMax), width=20)
    btnModificar.grid(column=4, row=8, padx=18, pady=10, rowspan=2)

    formTabla.mainloop()


#definicion form principal
root= Tk()
#root.geometry("600x400")
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
btnModificarPaciente.grid(column=2, row=2, padx=18, pady=10)

#Modificar datos de IMC
btnModificarPaciente= Button(root, text="Modificar Tabla IMC",command= lambda:ModificarTablaIMC(TablaIMCAdulto, TablaIMCNino, TablaIMCNina), width=14, height=5, font=fontText, padx=10, border=5, borderwidth=3)
btnModificarPaciente.grid(column=3, row=2, padx=18, pady=10)

#Seccion de archivos xml

#boton generar xml
btnGenerarXML= Button(root, text="Exportar\nPacientes",command=EscribirXMl, width=14, height=5, font=fontText, padx=10, border=5, borderwidth=3)
btnGenerarXML.grid(column=2, row=3, padx=18, pady=10)

#Leer xml
btnLeerXML= Button(root, text="Leer\nPacientes",command=leerXML, width=14, height=5, font=fontText, padx=10, border=5, borderwidth=3)
btnLeerXML.grid(column=3, row=3, padx=18,pady=10)

root.mainloop()
