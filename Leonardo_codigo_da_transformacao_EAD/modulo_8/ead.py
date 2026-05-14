
class Carro:
    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
   
        print(f"Carro: {self.marca} {self.modelo}")

    def __str__(self):
   
        return f"{self.marca} {self.modelo}"


class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
   
        super().__init__(marca, modelo)

        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):

        print(f"Carro Elétrico: {self.marca} {self.modelo} | Autonomia: {self.autonomia_bateria}km")


meu_carro = Carro("Toyota", "Corolla")
meu_eletrico = CarroEletrico("Tesla", "Model 3", 500)

meu_carro.exibir_info()
meu_eletrico.exibir_info()
