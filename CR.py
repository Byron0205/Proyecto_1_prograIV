from ClassCliente import Cliente, ClienteMenor
import tkinter.messagebox as alert
class Sistema():

  #Eliminar
  def Eliminar(self,DatoparaEliminar):
    try:
        for line in self:
            if line == DatoparaEliminar: #Esto cambia dependiendo de como se ordene la lista
                self.pop(line) 
    except:
        alert.showinfo(title='Error', message='No es posible eliminar el paciente')






