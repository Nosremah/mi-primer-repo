import sympy as sp
import math
def newton(f_simb,xi):
    x = sp.Symbol('x')

    # Derivada simbolica
    f_derivada = sp.diff(f_simb, x)

    # Convertir las funciones simbolica a funciones lambda
    f = sp.lambdify(x, f_simb, 'numpy')
    df = sp.lambdify(x, f_derivada, 'numpy')

    # Definir errores e iteraciones para no sobrecargar 
    # de parametros la funcion 
    i=0
    e=0.00001 # e define el error epsilon en la preimagen
    d=0.00001 # d define el error delta en las imagenes
    
    xm = xi # xn es el termino n+1 de la sucesion recursiva
    while i<20: 
        #Evita división por cero     
        if abs(df(xm)) < 1e-15:
           print("El metodo falló. División por cero.")
           return None
        
        #formula de Newton Rapshon
        xn = xm-(f(xm)/df(xm))

        #Criterios de parada
        if abs(xn-xm) < e or abs(f(xn)) < d:
            return xn

        xm = xn
        i += 1

    return xm

x=sp.symbols('x')
raiz=newton(sp.sin(x) - sp.exp(x), -2)
print(raiz)