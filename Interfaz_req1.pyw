from tkinter import *
import tkinter.font as tkfont
import tkinter.messagebox as alert

#Clase creada para trabajar datos
from ClassCliente import Cliente, ClienteMenor
paddingForm= 10

#datos de prueba
p = Cliente(1234,'Byron','Sosa',56475647,'example@example.com',70.5,1.77,21,'M')
p.IMC = '12.5 Normal'
p2= ClienteMenor(87654,'Juan','Perez',67894536,'example@example.com',45,1.36,14,'M',45326622)
p2.IMC= '14.7 Bajo'


#Almacen de datos de clientes
listaPacientes=[]
listaPacientes.append(p)
listaPacientes.append(p2)


def TablaIMC(datos,sexo, edad):
    try:
        if(edad>=20):
            if (datos < 18.5):
                return "Bajo peso"
            elif(datos <= 18.5 or datos >= 24.9 ):
                return "Peso normal"
            elif (datos<= 25.0 or datos >=29.9):
                return "Sobrepeso"
            elif (datos>=30.0):
                return "Obesidad"
        if (edad <=5 or edad >=10 and sexo == "F"):
            if (datos <= 13.8):
                return "Bajo peso"
            elif(datos <= 13.9 or datos >= 16.8 ):
                return "Peso normal"
            elif (datos<= 16.9 or datos >=18.8):
                return "Sobrepeso"
            elif (datos>=18.9):
                return "Obesidad"
            if (edad <=10 or edad >=19 and sexo == "M"):
                if (datos <= 16.4):
                    return "Bajo peso"
            elif(datos <= 18.6 or datos >= 24.7 ):
                return "Peso normal"
            elif (datos<= 24.8 or datos >=29.4):
                return "Sobrepeso"
            elif (datos>=29.5):
                return "Obesidad"
    except:
        print("El dato a comparar no corresponde")

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

def AgregarCliente(ced,nom, ape,tel,peso,alt,edad,sexo,frm,correo='', telE=0):
    if nom == '' or peso == 0 or alt == 0 or edad == 0 or tel == 0:
        alert.showerror(title='Compos Incompletos',message='Debe completar minimo los campos de nombre,telefono,peso, altura y edad')
    else:
        if telE != 0:
            per = ClienteMenor(ced,nom,ape,tel,correo,peso,alt,edad,sexo,telE)
        else:
            per = Cliente(ced,nom,ape,tel,correo,peso,alt,edad,sexo)
            
        per.IMC= CalcularIMC(Peso=peso,Altura= alt,Edad= edad,Sexo= sexo) 
        listaPacientes.append(per)
        alert.showinfo(title='Resultado', message="Usuario guardado con exito")
        frm.destroy()

def  mostrarPaciente(p):
    formMostrar = Toplevel(root)
    formMostrar.geometry("+{}+{}".format(root.winfo_x() + root.winfo_width(), root.winfo_y()))
    formMostrar.title('Mostrar Datos')

    lblIMC = Label(formMostrar, text='IMC',pady=paddingForm, font=fontText)
    lblIMC.grid(column=1,row=0, padx=10)

    txtIMC = Label(formMostrar, text=p.IMC)
    txtIMC.grid(column=2, row=0, columnspan=2)

    lblIdentificacion = Label(formMostrar, text="Identificacion", pady=paddingForm, font=fontText)
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

    lblTelefono= Label(formMostrar, text="Telefono",pady=paddingForm, font=fontText)
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
        lbltelEncargado = Label(formMostrar, text='Telefono Encargado', font=fontText, pady=paddingForm)
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

def modificar(p, ced,nom, ape, tel, mail,peso,alt,edad, gender,frm, telE =0):
    try:
        p.nombre = nom
        p.identificacion = ced
        p.apellido= ape
        p.telefono= tel
        p.correo= mail
        p.peso= peso
        p.altura = alt
        p.edad = edad
        p.sexo = gender

        if telE != 0:
            p.telefonoP = telE
        alert.showinfo(title='Resultado',message='Usuario modificado correctamente')
        p.IMC= CalcularIMC(Peso=peso,Altura= alt,Edad= edad,Sexo= gender)
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


    lblIdentificacion = Label(formModificar, text="Identificacion", pady=paddingForm, font=fontText)
    lblIdentificacion.grid(column=1,row=1,padx=10)

    txtIdentificacion = Entry(formModificar,font=fontText, textvariable=ced)#colocar el font a los entry aumenta el tamano
    txtIdentificacion.grid(column=2,row=1,columnspan=2)


    lblNombre = Label(formModificar, text="Nombre", pady=paddingForm, font=fontText)
    lblNombre.grid(column=1,row=2,padx=10)

    txtNombre= Entry(formModificar, font=fontText, textvariable=nom)
    txtNombre.grid(column=2, row=2, padx=5,columnspan=2)
    
    lblapellido = Label(formModificar, text="Apellidos", pady=paddingForm, font=fontText)
    lblapellido.grid(column=1,row=3,padx=10)

    txtapellido= Entry(formModificar, font=fontText, textvariable=ape)
    txtapellido.grid(column=2, row=3, padx=5,columnspan=2)

    lblTelefono= Label(formModificar, text="Telefono",pady=paddingForm, font=fontText)
    lblTelefono.grid(column=1,row=4)

    txtTelefono = Entry(formModificar, font=fontText, textvariable=tel)
    txtTelefono.grid(column=2,row=4,columnspan=2)
    
    lblCorreo= Label(formModificar, text="Correo",pady=paddingForm, font=fontText)
    lblCorreo.grid(column=1,row=5)

    txtCorreo = Entry(formModificar, font=fontText, textvariable=mail)
    txtCorreo.grid(column=2,row=5,columnspan=2)

    lblpeso = Label(formModificar, text="Peso", pady=paddingForm, font=fontText)
    lblpeso.grid(column=1,row=6,padx=10)

    txtpeso= Entry(formModificar, font=fontText, textvariable=peso)
    txtpeso.grid(column=2, row=6, padx=5,columnspan=2)

    lblaltura = Label(formModificar, text="Altura", pady=paddingForm, font=fontText)
    lblaltura.grid(column=1,row=7,padx=10)

    txtaltura= Entry(formModificar, font=fontText, textvariable=alt)
    txtaltura.grid(column=2, row=7, padx=5,columnspan=2)

    lbledad = Label(formModificar, text="Edad", pady=paddingForm, font=fontText)
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
        tel=int(txtTelefono.get()),
        mail=txtCorreo.get(),
        peso=float(txtpeso.get()),
        alt= float(txtaltura.get()),
        edad=int(txtedad.get()),
        gender=gender.get()), width=12, height=2, border=1)
    btnModificar.grid(column=1, row=10, columnspan=3, pady=10)

    btnEliminar = Button(formModificar, text='Eliminar', command=lambda:Eliminar(p,formModificar), width=15, height=2, border=1)
    btnEliminar.grid(column=1, row=11, columnspan=3, pady=10)

    #verificar si existe el atributo en el objeto
    if hasattr(p, 'telefonoP'):
        lbltelEncargado = Label(formModificar, text='Telefono Encargado', font=fontText, pady=paddingForm)
        lbltelEncargado.grid(column=1,row=10)

        telEncargado = StringVar(value=p.telefonoP)
        txttelEncargado= Entry(formModificar, font=fontText, textvariable=telEncargado)
        txttelEncargado.grid(column=2,row=10, columnspan=2)

        btnModificar.grid(column=1, row=11, columnspan=3, pady=10)
        btnEliminar.grid(column=1, row=12, columnspan=3, pady=10)
    formModificar.mainloop()

#form
def nuevoPaciente():
    resp=alert.askquestion(title='Tipo Paciente', message='¿Va a agregar un menor?')

    formPaciente = Toplevel(root)
    formPaciente.title("Registro Paciente")
    formPaciente.geometry("+{}+{}".format(root.winfo_x() + root.winfo_width(), root.winfo_y()))


    lblTitulo = Label(formPaciente, text="Datos", font=fontTitle, justify=CENTER)
    lblTitulo.grid(column=1,row=0, columnspan=2,padx=10)


    lblIdentificacion = Label(formPaciente, text="Identificacion", pady=paddingForm, font=fontText)
    lblIdentificacion.grid(column=1,row=1,padx=10)

    txtIdentificacion = Entry(formPaciente,font=fontText)#colocar el font a los entry aumenta el tamano
    txtIdentificacion.grid(column=2,row=1,columnspan=2)


    lblNombre = Label(formPaciente, text="Nombre", pady=paddingForm, font=fontText)
    lblNombre.grid(column=1,row=2,padx=10)

    txtNombre= Entry(formPaciente, font=fontText)
    txtNombre.grid(column=2, row=2, padx=5,columnspan=2)
    
    lblapellido = Label(formPaciente, text="Apellidos", pady=paddingForm, font=fontText)
    lblapellido.grid(column=1,row=3,padx=10)

    txtapellido= Entry(formPaciente, font=fontText)
    txtapellido.grid(column=2, row=3, padx=5,columnspan=2)

    lblTelefono= Label(formPaciente, text="Telefono",pady=paddingForm, font=fontText)
    lblTelefono.grid(column=1,row=4)

    txtTelefono = Entry(formPaciente, font=fontText)
    txtTelefono.grid(column=2,row=4,columnspan=2)
    
    lblCorreo= Label(formPaciente, text="Correo",pady=paddingForm, font=fontText)
    lblCorreo.grid(column=1,row=5)

    txtCorreo = Entry(formPaciente, font=fontText)
    txtCorreo.grid(column=2,row=5,columnspan=2)

    lblpeso = Label(formPaciente, text="Peso", pady=paddingForm, font=fontText)
    lblpeso.grid(column=1,row=6,padx=10)

    txtpeso= Entry(formPaciente, font=fontText)
    txtpeso.grid(column=2, row=6, padx=5,columnspan=2)

    lblaltura = Label(formPaciente, text="Altura", pady=paddingForm, font=fontText)
    lblaltura.grid(column=1,row=7,padx=10)

    txtaltura= Entry(formPaciente, font=fontText)
    txtaltura.grid(column=2, row=7, padx=5,columnspan=2)

    lbledad = Label(formPaciente, text="Edad", pady=paddingForm, font=fontText)
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
    ced= txtIdentificacion.get(),
    nom= txtNombre.get(),
    ape= txtapellido.get(), 
    tel= int(txtTelefono.get()),
    correo= txtCorreo.get(),
    peso= float(txtpeso.get()),
    alt= float(txtaltura.get()),
    edad= int(txtedad.get()),
    sexo= gender.get()), width=10)
    btnAceptar.grid(column=1, row=10, columnspan=3, pady=10)

    if resp == 'yes':
        
        lbltelEncargado = Label(formPaciente, text='Telefono Encargado', font=fontText, pady=paddingForm)
        lbltelEncargado.grid(column=1,row=10)

        txttelEncargado= Entry(formPaciente, font=fontText)
        txttelEncargado.grid(column=2,row=10, columnspan=2)
        btnAceptar.grid_forget()
        btnAceptarM= Button(formPaciente, text="Aceptar", command=lambda:AgregarCliente(
    frm=formPaciente,
    ced=txtIdentificacion.get(),
    nom= txtNombre.get(),
    ape= txtapellido.get(), 
    tel= int(txtTelefono.get()),
    correo= txtCorreo.get(),
    peso= float(txtpeso.get()),
    alt= float(txtaltura.get()),
    edad= int(txtedad.get()),
    sexo= gender.get(),
    telE= int(txttelEncargado.get())), width=10)
        btnAceptarM.grid(column=1, row=11, columnspan=3, pady=10)
    formPaciente.mainloop()

#form
def ConsultarPaciente():
    global pacientes, txtBuscar
    formConsultar = Toplevel(root)
    formConsultar.title("Busqueda")

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
    formConsultar.title("Busqueda")

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

#definicion form principal
root= Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("Pacientes - Elemental Nutricion")


#variables interfaz
fontTitle = tkfont.Font(size=25)
fontText = tkfont.Font(size=13)

lblTitulo= Label(root, text="Control de Pacientes",font=fontTitle)
lblTitulo.grid(column=2, row=0, pady=15, columnspan=3)

#Nuevo Paciente
btnNuevoPaciente= Button(root, text="Nuevo Paciente", command=nuevoPaciente, width=14, height=5, font=fontText, padx=10, border=5, borderwidth=3)
btnNuevoPaciente.grid(column=2, row=1, padx=10)# agregar el padx aqui crea separacion con otros elementos

#consultar paciente
btnRevisarPaciente= Button(root, text="Consultar Paciente", command=ConsultarPaciente, width=14, height=5, font=fontText, padx=10, border=5, borderwidth=3)
btnRevisarPaciente.grid(column=3, row=1, padx=10)

#Modificar / eliminar Paciente
btnModificarPaciente= Button(root, text="Modificar Paciente",command=ConsultarPacienteMod, width=14, height=5, font=fontText, padx=10, border=5, borderwidth=3)
btnModificarPaciente.grid(column=4, row=1, padx=10)

root.mainloop()
