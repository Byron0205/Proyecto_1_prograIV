from tkinter import *
import tkinter.font as tkfont
import tkinter.messagebox as alert

paddingForm= 10


global nom,ced

def mensajePrueba():
    global nombre, ced, tel, correo
    nombre = txtNombre.get()
    ced= txtIdentificacion.get()
    tel = txtTelefono.get()
    correo = txtCorreo.get()

    alert.showinfo(title="datos",message= f"identificacion: {ced} nombre: {nombre} telefono: {tel} correo: {correo}")

    if alert.askokcancel(title="Confirmar", message="Desea guardar el paciente?"):
        #agregar proceso de guardado en lista de los registros
        formPaciente.destroy()

def nuevoPaciente():
    global txtNombre, txtIdentificacion, txtTelefono, txtCorreo, formPaciente
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


    btnAceptar= Button(formPaciente, text="Aceptar", command=mensajePrueba, width=10)
    btnAceptar.grid(column=1, row=5, columnspan=2, pady=10)
    formPaciente.mainloop()


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
btnRevisarPaciente= Button(root, text="Consultar Paciente", width=14, height=5, font=fontText, padx=10, border=5, borderwidth=3)
btnRevisarPaciente.grid(column=3, row=1, padx=10)

#falta command
#Modificar Paciente
btnRevisarPaciente= Button(root, text="Modificar Paciente", width=14, height=5, font=fontText, padx=10, border=5, borderwidth=3)
btnRevisarPaciente.grid(column=4, row=1, padx=10)


#Eliminar
def Eliminar(self,DatoparaEliminar):
    try:
        for line in self:
            if line == DatoparaEliminar: #Esto cambia dependiendo de como se ordene la lista
                self.pop(line) 
    except:
        print("No se eliminó")

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
root.mainloop()