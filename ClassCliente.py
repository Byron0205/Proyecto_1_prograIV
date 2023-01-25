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
        self.IMC = 0

class ClienteMenor():
    #constructor para los niños
    def __init__(self, identificacion, nombre, apellido, telefono, correo, peso, altura, edad, sexo,telefonoP):
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
        self.IMC = 0