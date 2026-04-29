import math

def biseccion(f, a, b, epsilon, delta):
    # Verificamos la condición inicial
    if f(a) * f(b) < 0:
        # Iniciamos el bucle: mientras el intervalo sea mayor a epsilon
        # o el valor de la función no sea lo suficientemente cercano a cero
        while abs(b - a) > epsilon and abs(f((a + b) / 2)) > delta:
            c = (a + b) / 2  # Calculamos el punto medio

            # Verificamos en qué lado está la raíz
            if f(a) * f(c) < 0:
                b = c
            elif f(a) * f(c) == 0:
                return c # Encontramos la raíz exacta
            else:
                a = c
        return (a + b) / 2
    else:
        print("Error: El intervalo no contiene una raíz o no hay cambio de signo.")
# Buscar la raíz de f(x) = sin(x) - x/2
resultado = biseccion(lambda x: math.sin(x) - math.exp(x), -5, -1, 0.001, 0.001)
print("La raiz es: " , resultado)