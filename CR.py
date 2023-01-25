class Cliente:    
    #constructor para los Adultos
    def __init__(self, identificacion, nombre, apellido, telefono, correo, peso, altura, edad, sexo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.peso = peso
        self.altura = altura
        self.edad = edad
        self.sexo = sexo
    

class ClienteMenor():
    #constructor para los niños
    def __init__(self, identificacion, nombre, apellido, telefono, telefonoP, correo, peso, altura, edad, sexo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.telefonoP = telefonoP
        self.correo = correo
        self.peso = peso
        self.altura = altura
        self.edad = edad
        self.sexo = sexo
Personas = []
class Prueba(Cliente,ClienteMenor):
#TablaIMC 
  def TablaIMC(self,datos):
    try:
      if(self.edad>=20):
        if (datos < 18.5):
          return "Bajo peso"
        elif(datos <= 18.5 or datos >= 24.9 ):
          return "Peso normal"
        elif (datos<= 25.0 or datos >=29.9):
          return "Sobrepeso"
        elif (datos>=30.0):
          return "Obesidad"
      if (self.edad <=5 or self.edad >=10 and self.sexo == "F"):
        if (datos <= 13.8):
          return "Bajo peso"
        elif(datos <= 13.9 or datos >= 16.8 ):
          return "Peso normal"
        elif (datos<= 16.9 or datos >=18.8):
          return "Sobrepeso"
        elif (datos>=18.9):
          return "Obesidad"
        if (self.edad <=10 or self.edad >=19 and self.sexo == "M"):
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

  def AgregarDatos():
    identificacion = input("Digite identificacion:")
    nombre = input("Digite nombre:")
    apellido = input("Digite apellido:")
    telefono = input("Digite telefono:")
    correo = input("Digite correo:")
    peso = input("Digite peso:")
    altura = input("Digite altura:")
    edad = input("Digite edad:")
    sexo = input("Digite sexo:")
    per = Cliente(identificacion,nombre,apellido,telefono,correo,peso,altura,edad,sexo)
    Personas.append(per)
    print("Persona guardada con exito")
    Mostrar()

def Mostrar():
  k=0
  while k < len(Personas):
    print(Personas[k].nombre)
    k+=1
    
Prueba.AgregarDatos()


