TablaIMCAdulto = [18.5,24.9,29.9]
TablaIMCNina = [13.8,16.8,18.8]
TablaIMCNino = [16.4,18.6,24.7,29.4]
#TablaIMC 
def TablaIMC(self,datos):
    try:
      if(self.edad>=20):
        if (datos <= TablaIMCAdulto[0]):
          return "Bajo peso"
        elif(datos < TablaIMCAdulto[0] or datos >= TablaIMCAdulto[1]):
          return "Peso normal"
        elif (datos< TablaIMCAdulto[1] or datos >=TablaIMCAdulto[2]):
          return "Sobrepeso"
        elif (datos>TablaIMCAdulto[3]):
          return "Obesidad"
      if (self.edad <=5 or self.edad >=10 and self.sexo == "F"):
        if (datos <= TablaIMCNina[0]):
          return "Bajo peso"
        elif(datos < TablaIMCNina[0] or datos >= TablaIMCNina[1] ):
          return "Peso normal"
        elif (datos< TablaIMCNina[1] or datos >=TablaIMCNina[2]):
          return "Sobrepeso"
        elif (datos>TablaIMCNina[2]):
          return "Obesidad"
        if (self.edad <=10 or self.edad >=19 and self.sexo == "M"):
          if (datos <= TablaIMCNino[0]):
            return "Bajo peso"
        elif(datos < TablaIMCNino[1] or datos >= TablaIMCNino[2] ):
          return "Peso normal"
        elif (datos< TablaIMCNino[2] or datos >=TablaIMCNino[3]):
          return "Sobrepeso"
        elif (datos>TablaIMCNino[3]):
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

def MostrarDatos():
  k=0
  while k < len(Personas):
    print(Personas[k].identificacion,Personas[k].nombre,Personas[k].apellido)
    k+=1


