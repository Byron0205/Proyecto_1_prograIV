TablaIMCAdulto = [18.5,24.9,25.0,29.9,30.0]
TablaIMCNina = [12.7,18.5, 13.9,24.7, 16.9,29.4]
TablaIMCNino = [13.0,19.1, 14.1,24.8, 16.6,29.1]
#TablaIMC 
def TablaIMC(self,datos):
    try:
        if(self.edad>=20):
            if (datos <= TablaIMCAdulto[0]):
                return "Bajo peso"
            elif(datos > TablaIMCAdulto[0] and datos < TablaIMCAdulto[1]):
                return "Peso normal"
            elif (datos> TablaIMCAdulto[2] and datos < TablaIMCAdulto[3]):
                return "Sobrepeso"
            elif (datos>=TablaIMCAdulto[4]):
                return "Obesidad"
        if (self.edad < 5):
            return 'La edad no puede ser menor a 5'
        else:
            if (self.edad >5 and self.edad <=19 and self.sexo == "F"):
                if (datos >= TablaIMCNina[0] and datos <= TablaIMCNina[1]):
                    return "Bajo peso"
                elif(datos >= TablaIMCNina[2] and datos <= TablaIMCNina[3] ):
                    return "Peso normal"
                elif (datos >= TablaIMCNina[4] and datos <=TablaIMCNina[5]):
                    return "Sobrepeso"
                elif (datos>TablaIMCNina[5]):
                    return "Obesidad"

            if (self.edad > 5 and self.edad <=19 and self.sexo == "M"):
                if (datos >= TablaIMCNino[0] and datos <= TablaIMCNino[1]):
                    return "Bajo peso"
                elif(datos >= TablaIMCNino[2] and datos <= TablaIMCNino[3] ):
                    return "Peso normal"
                elif (datos >= TablaIMCNino[4] and datos <=TablaIMCNino[5]):
                    return "Sobrepeso"
                elif (datos>TablaIMCNino[5]):
                    return "Obesidad"
    except:
        print("El dato a comparar no corresponde")




