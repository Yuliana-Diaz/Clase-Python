class Distancia:
    # Precondiciones + Postcondiciones de los casos de uso 
    # Atributos: Encapsulación
    __metros = 0.0
    __kilometros = 0.0
    __centimetros = 0.0
    __milimetros = 0.0

    # Metodos: 1 metodo por cada caso de uso 
    # def nombre caso de uso (self, parametros (precondiciones separadas con comas))
    def convertirMetrosAKilometros(self, metros):
        self.__metros = metros 
        self.__kilometros = self.__metros/1000
        return self.__kilometros
    def convertirMetrosACentimetros(self, metros):
        self.__metros = metros 
        self.__centimetros = self.__metros*100
        return self.__centimetros
    def convertirMetrosAMilimetros(self, metros):
        self.__metros = metros
        self.__milimetros = self.__metros*1000
        return self.__milimetros