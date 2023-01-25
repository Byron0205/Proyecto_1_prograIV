from tkinter import *
import tkinter.font as tkfont
import tkinter.messagebox as alert

#Clase creada para trabajar datos
from ClassCliente import Cliente

paddingForm= 10

#Almacen de datos de clientes
listaPacientes=[]

#Eliminar
def Eliminar(self,DatoparaEliminar):
    try:
        for line in self:
            if line == DatoparaEliminar: #Esto cambia dependiendo de como se ordene la lista
                self.pop(line) 
    except:
        alert.showinfo(title='Error', message='No es posible eliminar el paciente')

#IMC
def CalcularIMC(self,Peso,Altura,Edad):
    #Adultos 20 o más años, Peso(kg) ÷ (Altura(cm))Elevado a 2 = Resultado
    #Niños y Adolecentes 2 a 19 años, 

    Resultado = Peso/(Altura**2)
    
    #Se llama la tabla para traer los datos y hacer la comparacion
    DatosdeReferencia = 0
    
    if (Resultado < DatosdeReferencia):
        pass
        #Adultos
        #Por debajo de 18.5	Bajo peso
        #18.5 – 24.9	Normal
        #25.0 – 29.9	Sobrepeso
        #30.0 o más	Obesidad

def on_select():
    selected = pacientes.get(pacientes.curselection())
    #falta funcion para ver datos al seleccionar el paciente
    print(selected)

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
            

def mensajePrueba(nom, id, telefono, correo, frm):
    nombre = nom
    ced= id
    tel = telefono
    mail = correo

    alert.showinfo(title="datos",message= f"identificacion: {ced} nombre: {nombre} telefono: {tel} correo: {mail}")

    if alert.askokcancel(title="Confirmar", message="Desea guardar el paciente?"):
        #agregar proceso de guardado en lista de los registros
        frm.destroy()

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
    
    btnAceptar= Button(formPaciente, text="Aceptar", command=lambda:mensajePrueba(txtNombre.get(),txtIdentificacion.get(), txtTelefono.get(),txtCorreo.get(),formPaciente), width=10)
    btnAceptar.grid(column=1, row=10, columnspan=3, pady=10)

    if resp == 'yes':
        lbltelEncargado = Label(formPaciente, text='Telefono Encargado', font=fontText, pady=paddingForm)
        lbltelEncargado.grid(column=1,row=10)

        txttelEncargado= Entry(formPaciente, font=fontText)
        txttelEncargado.grid(column=2,row=10, columnspan=2)

        btnAceptar.grid(column=1, row=11, columnspan=3, pady=10)
    formPaciente.mainloop()


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
        pacientes.insert('end', p)

    btnAceptar= Button(formConsultar, text="Aceptar", command=on_select, width=10, padx=10)
    btnAceptar.grid(column=1, row=3, columnspan=2, pady=10)


    formConsultar.mainloop()

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

#falta command
#Modificar Paciente
btnModificarPaciente= Button(root, text="Modificar Paciente", width=14, height=5, font=fontText, padx=10, border=5, borderwidth=3)
btnModificarPaciente.grid(column=4, row=1, padx=10)

root.mainloop()
