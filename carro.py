#crear clase carro instanciarla, que contenga, marca, modelo, calidad de fgoma, precio, velocidad tope
class Carro:
    def __init__(self, modelo):
        self.marca = 'toyota'
        self.modelo = ''
        self.calidad_goma = 10
        self.precio = 100000
        self.velocidad_top = 100
        self.velociad_act = 0
        
    def mantenimiento(self):
        self.calidad_goma  += 1
        self.velocidad_top += 5
        self.precio += 1000
        print(f'El mantenimiento de su vehiculo ha sido completado, la goma ahora tiene una calidad de {self.calidad_goma}, la velocidad maxima ahora es de {self.velocidad_top} km/h y su precio ha aumentado a {self.precio}')
    def avanzar(self):
        self.velociad_act += 30
        print(f'su velocidad ha aumentado a {self.velociad_act}')
    def frenar(self):
        self.velociad_act = 0
        print(f'has frenado') 
    

if __name__ == "__main__" :
    vehiculo = Carro('corolla')
    vehiculo.mantenimiento()
    vehiculo.avanzar()
    vehiculo.frenar()