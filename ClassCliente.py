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
    
    #constructor para los niños
    def __init__(self, identificacion, nombre, apellido, telefonoM, telefonoP, correoM, correoP, peso, altura, edad, sexo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
        self.telefonoM = telefonoM
        self.telefonoP = telefonoP
        self.correoM = correoM
        self.correoP = correoP
        self.peso = peso
        self.altura = altura
        self.edad = edad
        self.sexo = sexo