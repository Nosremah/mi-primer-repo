import sympy as sp
import math

#Funcion que recibe como parámetro una función lambda y retorna
# una función simbolica con la misma estructura lógica. 
def funcion(f_lambda):
    x=sp.symbols('x')
    return sp.diff(f_lambda(x))

print(funcion(lambda x: 2*x))






