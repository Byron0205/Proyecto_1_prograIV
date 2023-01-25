from tkinter import *
import tkinter.font as tkfont
import tkinter.messagebox as alert

#Clase creada para trabajar datos
from ClassCliente import Cliente

paddingForm= 10

#Almacen de datos de clientes
listaPacientes=[]

global nom,ced

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
    formPaciente = Toplevel(root)
    formPaciente.title("Registro Paciente")
    formPaciente.geometry("+{}+{}".format(root.winfo_x() + root.winfo_width(), root.winfo_y()))


    lblTitulo = Label(formPaciente, text="Datos", font=fontTitle, justify=CENTER)
    lblTitulo.grid(column=1,row=0, columnspan=2,padx=10)


    lblIdentificacion = Label(formPaciente, text="Identificacion", pady=paddingForm, font=fontText)
    lblIdentificacion.grid(column=1,row=1,padx=10)

    txtIdentificacion = Entry(formPaciente,font=fontText)#colocar el font a los entry aumenta el tamano
    txtIdentificacion.grid(column=2,row=1)


    lblNombre = Label(formPaciente, text="Nombre", pady=paddingForm, font=fontText)
    lblNombre.grid(column=1,row=2,padx=10)

    txtNombre= Entry(formPaciente, font=fontText)
    txtNombre.grid(column=2, row=2, padx=5)
    


    lblTelefono= Label(formPaciente, text="Telefono",pady=paddingForm, font=fontText)
    lblTelefono.grid(column=1,row=3)

    txtTelefono = Entry(formPaciente, font=fontText)
    txtTelefono.grid(column=2,row=3)
    
    lblCorreo= Label(formPaciente, text="Correo",pady=paddingForm, font=fontText)
    lblCorreo.grid(column=1,row=4)

    txtCorreo = Entry(formPaciente, font=fontText)
    txtCorreo.grid(column=2,row=4)


    btnAceptar= Button(formPaciente, text="Aceptar", command=lambda:mensajePrueba(txtNombre.get(),txtIdentificacion.get(), txtTelefono.get(),txtCorreo.get(),formPaciente), width=10)
    btnAceptar.grid(column=1, row=5, columnspan=2, pady=10)
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

#falta command
#consultar paciente
btnRevisarPaciente= Button(root, text="Consultar Paciente", command=ConsultarPaciente, width=14, height=5, font=fontText, padx=10, border=5, borderwidth=3)
btnRevisarPaciente.grid(column=3, row=1, padx=10)

#falta command
#Modificar Paciente
btnRevisarPaciente= Button(root, text="Modificar Paciente", width=14, height=5, font=fontText, padx=10, border=5, borderwidth=3)
btnRevisarPaciente.grid(column=4, row=1, padx=10)


root.mainloop()
