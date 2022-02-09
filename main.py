
#programa para graficar datos .

from distutils.log import error
from matplotlib.pyplot import plot, show
from pip import main
import statistics


class error_menor(Exception):
    pass
    def min(minimo):
        return minimo <= 0

def main():
    min=0
    list=[]
    contador=0
    intentos=int(input("Cuantos datos se van a graficar?  "))
    for intentos in range(intentos):
        while True:
            try:
                numero=float(input("Dame el numero a graficar"))
                if numero > min:
                    list.append(numero)
                    contador += 1
                else:
                    raise error_menor ("El valor ingresado debe ser mayor a 0")
                if contador >= intentos:
                    break
            
            except error_menor as error:
                print(error)
            except:
                print("dato no valido")
            finally:
                print("El promedio de los numeros graficados hasta el momento es de:")
                mean = statistics.mean(list)
                print(mean)
    plot(list)
    show()
main()


