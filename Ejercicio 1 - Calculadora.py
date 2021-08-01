class Calculadora:
    def __init__(self, numero1, numero2):
        self.num1=numero1
        self.num2=numero2
        
    def suma(self):
        SumaTotal= self.num1 + self.num2
        print("La suma total de los numeros {} y {} es de: {}".format(self.num1,self.num2,SumaTotal))
    
    def resta(self):
        RestaTotal= self.num1 - self.num2
        print("La resta total de los numeros {} y {} es de: {}".format(self.num1, self.num2, RestaTotal))
    
    def multiplicacion(self):
        MultiplicaciónTotal= self.num1 * self.num2
        print("La multiplicación total de los numeros {} y {} es de: {}".format(self.num1,self.num2, MultiplicaciónTotal))
                
    def division(self):
        DivisionTotal=self.num1 / self.num2
        print("La division de los numeros es de: {}".format(DivisionTotal))
        
class CalEstandar(Calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        
        
    def multiplicacion(self):
        Resul= self.num1 * self.num2
        return Resul
    
    def exponente(self):
        ExponenteTotal = self.num1**self.num2
        print("Respuesta: ",ExponenteTotal)

    def valorAbsoluto(sefl,numero3):
        if numero3 < 0:
            numero3 = numero3 *- 1
        return numero3

    
class calCientifica(Calculadora):

    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        
    def circunferencia(self):
        pi = 3.1416
        Perimetro = 2 * pi * self.num1
        return Perimetro
    
    def areaCirculo(self):
        PI = 3.1416
        area = PI * (self.num1**2)
        return area
    
    def areaCuadrado(self):
        return self.num2 ** 2
    

calculadora = calCientifica(1,2,3,4)
print(calculadora.circunferencia())
print(calculadora.areaCirculo())
print(calculadora.areaCuadrado())